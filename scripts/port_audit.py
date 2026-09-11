#!/usr/bin/env python3
"""UniFi switch port auditor — full inventory with anomaly detection.
Usage: port_audit.py <controller_url> <username> <password> [--errors-only]"""
import ssl, json, sys, urllib.request, http.cookiejar

def main():
    errors_only = "--errors-only" in sys.argv
    base = sys.argv[1].rstrip("/")
    user, pw = sys.argv[2], sys.argv[3]

    ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(jar),
        urllib.request.HTTPSHandler(context=ctx))
    opener.open(urllib.request.Request(base + "/api/auth/login",
        data=json.dumps({"username": user, "password": pw}).encode(),
        headers={"Content-Type": "application/json"}), timeout=10)

    devs = json.loads(opener.open(urllib.request.Request(
        base + "/proxy/network/api/s/default/stat/device",
        headers={"Accept": "application/json"}), timeout=30).read())["data"]

    for d in devs:
        if d.get("type") != "usw": continue
        print(f"=== {d['name']} ({d.get('model')}, {d.get('ip')}) ===")
        for p in d.get("port_table", []):
            errs = (p.get("rx_errors") or 0) + (p.get("tx_errors") or 0)
            drops = (p.get("rx_dropped") or 0) + (p.get("tx_dropped") or 0)
            flap = p.get("link_down_count") or 0
            is_problem = errs > 0 or drops > 1000 or flap > 10 or \
                         (p.get("up") and p.get("speed") == 10) or \
                         p.get("stp_state") == "blocking"
            if errors_only and not is_problem: continue
            if not p.get("up") and not errors_only:
                continue  # skip down ports in full mode too
            flag = " ⚠" if is_problem else ""
            print(f"  p{p.get('port_idx')}: up={p.get('up')} speed={p.get('speed')} "
                  f"errs={errs} drops={drops} flap={flap} "
                  f"poe={p.get('poe_power','—')}W{flag}")

if __name__ == "__main__":
    main()
