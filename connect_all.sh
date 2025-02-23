echo "Starting the system maintenance tasks..."
echo "Please choose an option:"
echo "1. Clean up system"
echo "2. Monitor system performance"
echo "3. Clean up system and monitor performance"
echo "4. Exit"

read -p "Enter your choice (1-4): " choice

OS=$(uname -s)

case $choice in
  1)
    if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
      echo "Detected Linux/macOS"
      bash ./scripts/linux/auto_cleanup.sh
    elif [[ "$OS" == *"CYGWIN"* || "$OS" == *"MINGW"* || "$OS" == *"MSYS"* ]]; then
      echo "Detected Windows"
      runas /user:Administrator "cmd.exe /c ./scripts/windows/auto_cleanup.bat"
      if [ $? -eq 0 ]; then
        echo "auto_cleanup.bat ran successfully."
      else
        echo "Error running auto_cleanup.bat. Access Denied."
      fi
    else
      echo "Unsupported OS detected. Exiting..."
      exit 1
    fi
    ;;

  2)
    if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
      echo "Detected Linux/macOS"
      bash ./scripts/linux/performance_monitor.sh
    elif [[ "$OS" == *"CYGWIN"* || "$OS" == *"MINGW"* || "$OS" == *"MSYS"* ]]; then
      echo "Detected Windows"
      runas /user:Administrator "cmd.exe /c ./scripts/windows/performance_monitor.bat"
      if [ $? -eq 0 ]; then
        echo "performance_monitor.bat ran successfully."
      else
        echo "Error running performance_monitor.bat. Access Denied."
      fi
    else
      echo "Unsupported OS detected. Exiting..."
      exit 1
    fi
    ;;

  3)
    if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
      echo "Detected Linux/macOS"
      bash ./scripts/linux/auto_cleanup.sh
      bash ./scripts/linux/performance_monitor.sh
    elif [[ "$OS" == *"CYGWIN"* || "$OS" == *"MINGW"* || "$OS" == *"MSYS"* ]]; then
      echo "Detected Windows"
      runas /user:Administrator "cmd.exe /c ./scripts/windows/auto_cleanup.bat"
      runas /user:Administrator "cmd.exe /c ./scripts/windows/performance_monitor.bat"
      if [ $? -eq 0 ]; then
        echo "Both batch files ran successfully."
      else
        echo "Error running one of the batch files. Access Denied."
      fi
    else
      echo "Unsupported OS detected. Exiting..."
      exit 1
    fi
    ;;

  4)
    echo "Exiting..."
    exit 0
    ;;

  *)
    echo "Invalid choice. Please enter a number between 1 and 4."
    exit 1
    ;;

esac

echo "System maintenance tasks completed."
