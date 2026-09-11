<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Аудитор портов UniFi

![Демо](screenshots/demo.svg)
[![CI](https://github.com/uMax-Cyber/PortLens/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/PortLens/actions/workflows/ci.yml)

Полная инвентаризация портов коммутаторов и поиск аномалий в сетях UniFi через API контроллера. Находит флапающие порты, счётчики ошибок, деградацию скорости, проблемы PoE и несоответствия VLAN — раньше, чем это заметят пользователи.

## Что детектируется

| Аномалия | Метод обнаружения |
|----------|-------------------|
| Флапинг порта | `link_down_count > 10` |
| Ошибки RX/TX | `rx_errors + tx_errors > 0` на активном порту |
| Деградация скорости | Активный порт на 10Mbps (ожидается 1Gbps+) |
| Чрезмерные потери | `rx_dropped + tx_dropped > 1000` |
| STP blocking | `stp_state == "blocking"` (возможна петля или мисконфиг) |
| Сбой PoE | `poe_enable && !poe_good` |
| Несоответствие VLAN | `native_networkconf_id` не совпадает с ожидаемым |

## Скрипты

| Скрипт | Назначение |
|--------|------------|
| `scripts/port_audit.py` | Полная инвентаризация с флагами аномалий |
| `scripts/topology_map.py` | Построение дерева устройств (коммутатор → AP → клиенты) |

## Использование

```bash
# Полный аудит (все коммутаторы)
python3 scripts/port_audit.py --controller https://ctrl.example.local:8443

# Только проблемы
python3 scripts/port_audit.py --errors-only

# Экспорт в файл
python3 scripts/port_audit.py --output report.txt
```

## Детали API
Используется legacy REST API UniFi (`/proxy/network/api/s/default/stat/device`), который возвращает полную `port_table` со счётчиками по каждому порту. Новый Integration API отдаёт ограниченный набор полей — для данных по портам используйте legacy.

## Лицензия
MIT

## 📬 Контакты

Вопросы? Пишите: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
