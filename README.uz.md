<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# UniFi port auditi

![Demo](screenshots/demo.svg)
[![CI](https://github.com/uMax-Cyber/PortLens/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/PortLens/actions/workflows/ci.yml)

UniFi tarmoqlarida svitch portlarini toʻliq inventarizatsiya qilish va anomaliyalarni aniqlash — kontroller API orqali. Flap qilayotgan portlar, xato hisoblagichlari, tezlikning pasayishi, PoE muammolari va VLAN nomuvofiqligini foydalanuvchilar shikoyat qilishidan oldin topadi.

## Nima aniqlanadi

| Anomaliya | Aniqlash usuli |
|-----------|----------------|
| Port flapi | `link_down_count > 10` |
| RX/TX xatolari | Aktiv portda `rx_errors + tx_errors > 0` |
| Tezlik pasayishi | Aktiv port 10Mbps da ishlashi (1Gbps+ boʻlishi kerak) |
| Haddan tashqari drop lar | `rx_dropped + tx_dropped > 1000` |
| STP blocking | `stp_state == "blocking"` (loop yoki notoʻgʻri sozlama boʻlishi mumkin) |
| PoE ishdan chiqishi | `poe_enable && !poe_good` |
| VLAN nomuvofiqligi | `native_networkconf_id` kutilgan qiymatga mos kelmasa |

## Skriptlar

| Skript | Vazifasi |
|--------|----------|
| `scripts/port_audit.py` | Anomaliya belgilari bilan toʻliq inventarizatsiya |
| `scripts/topology_map.py` | Qurilmalar daraxtini chizish (svitch → AP → klientlar) |

## Ishlatish

```bash
# Toʻliq audit (barcha svitchlar)
python3 scripts/port_audit.py --controller https://ctrl.example.local:8443

# Faqat muammolar
python3 scripts/port_audit.py --errors-only

# Hisobotni faylga chiqarish
python3 scripts/port_audit.py --output report.txt
```

## API tafsilotlari
UniFi ning eski (legacy) REST API sidan foydalanadi (`/proxy/network/api/s/default/stat/device`) — u har bir port uchun hisoblagichlari bilan toʻliq `port_table` beradi. Yangi Integration API maydonlarning faqat bir qismini qaytaradi, shuning uchun port ma'lumotlari uchun legacy API dan foydalaning.

## Litsenziya
MIT

## 📬 Aloqa

Savollaringiz bormi? Yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
