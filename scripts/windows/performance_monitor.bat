@echo off
echo Performance Monitoring - Windows

echo CPU Usage:
wmic cpu get loadpercentage

echo Memory Usage:
systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"

echo Disk Usage:
wmic logicaldisk get caption, freeSpace, size

echo CPU Temperature (If supported):
wmic /namespace:\\root\wmi path MSAcpi_ThermalZoneTemperature get CurrentTemperature

echo.
echo Performance monitoring completed.
pause
