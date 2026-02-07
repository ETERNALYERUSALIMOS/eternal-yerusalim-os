#!/data/data/com.termux/files/usr/bin/bash
termux-wifi-enable f
# 1. Bluetooth: Установи termux-api-app из F-Droid (разреши)
pkg install termux-api  # Уже OK

# 2. ADB: Wireless debug (Настройки → Система → Developer → Wireless debugging ON)
adb pair IP:PORT code  # Затем повтори #4

# 3. termux-location -p: Флаг -p не нужен, тест:
termux-location  # GPS+proxy (разреши в app)

# 4. Полная блокировка сканов (без root):
settings put secure location_changer_mode 0
settings put global wifi_scan_always_enabled 0
settings put global ble_scan_always_enabled 0

# 5. Мониторинг (повтори):
termux-wifi-scaninfo
termux-location  # Координаты Мытищ?

# 6. Quantum geo скрипт (исправь):
nano quantum_geo.sh
# Вставь:
termux-location > ~/geo_log.txt
echo "Geo чист! [$(date)]"
