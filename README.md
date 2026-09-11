[English](README.md) | [Русский](README.ru.md)

# UniFi Port Auditor
[![CI](https://github.com/uMax-Cyber/PortLens/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/PortLens/actions/workflows/ci.yml)

Full switch port inventory and anomaly detection for UniFi networks via controller API. Finds flapping ports, error counters, speed degradation, PoE issues, and VLAN mismatches — before users notice.

## What It Detects

| Anomaly | Detection Method |
|---------|-----------------|
| Port flapping | `link_down_count > 10` |
| RX/TX errors | `rx_errors + tx_errors > 0` on active port |
| Speed degradation | Active port at 10Mbps (should be 1Gbps+) |
| Excessive drops | `rx_dropped + tx_dropped > 1000` |
| STP blocking | `stp_state == "blocking"` (potential loop or misconfig) |
| PoE failure | `poe_enable && !poe_good` |
| VLAN mismatch | `native_networkconf_id` doesn't match expected |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/port_audit.py` | Full inventory with anomaly flags |
| `scripts/topology_map.py` | Build device tree (switch → AP → clients) |

## Usage

```bash
# Full audit (all switches)
python3 scripts/port_audit.py --controller https://ctrl.example.local:8443

# Only problems
python3 scripts/port_audit.py --errors-only

# Export to file
python3 scripts/port_audit.py --output report.txt
```

## API Details
Uses UniFi legacy REST API (`/proxy/network/api/s/default/stat/device`) which returns full `port_table` with counters per port. The newer Integration API returns limited fields — use legacy for port data.

## License
MIT
