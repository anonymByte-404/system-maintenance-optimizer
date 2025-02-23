monitor_cpu() {
  echo "CPU Usage:"
  top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print "CPU Load: " 100 - $1 "%"}'
}

monitor_memory() {
  echo "Memory Usage:"
  free -h | grep Mem | awk '{print "Used: " $3 "/" $2 " (" $3/$2 * 100.0 "%)"}'
}

monitor_disk() {
  echo "Disk Usage:"
  df -h | grep -E '^/dev/'
}

monitor_temperature() {
  if command -v sensors &>/dev/null; then
    echo "System Temperature:"
    sensors | grep "Core 0" | awk '{print "Core 0 Temperature: " $3}'
  else
    echo "Temperature monitoring not available (lm-sensors package not installed)"
  fi
}

monitor_cpu
monitor_memory
monitor_disk
monitor_temperature
