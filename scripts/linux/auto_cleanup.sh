TEMP_DIRS=(
  "/tmp"
  "/var/tmp"
  "$HOME/.cache"
)

LOG_DIRS=(
  "/var/log"
)

cleanup_temp_files() {
  echo "Cleaning temporary files..."
  for dir in "${TEMP_DIRS[@]}"; do
    if [ -d "$dir" ]; then
      echo "Cleaning $dir..."
      sudo rm -rf "$dir"/*
    else
      echo "$dir does not exist or is not a directory."
    fi
  done
}

cleanup_log_files() {
  echo "Cleaning log files..."
  for dir in "${LOG_DIRS[@]}"; do
    if [ -d "$dir" ]; then
      echo "Cleaning logs in $dir..."
      sudo find "$dir" -type f -name "*.log" -exec rm -f {} \;
    else
      echo "$dir does not exist or is not a directory."
    fi
  done
}

cleanup_package_cache() {
  echo "Cleaning package manager cache..."
  if command -v apt-get &>/dev/null; then
    sudo apt-get clean
  elif command -v yum &>/dev/null; then
    sudo yum clean all
  elif command -v pacman &>/dev/null; then
    sudo pacman -Scc --noconfirm
  else
    echo "No recognized package manager found."
  fi
}

cleanup_old_kernels() {
  echo "Cleaning old unused kernels..."
  if command -v dpkg &>/dev/null; then
    sudo apt-get autoremove --purge -y
  elif command -v rpm &>/dev/null; then
    sudo package-cleanup --oldkernels --count=1
  fi
}

cleanup_temp_files
cleanup_log_files
cleanup_package_cache
cleanup_old_kernels

echo "System cleanup complete."
