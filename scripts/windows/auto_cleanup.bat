@echo off
echo Auto Cleanup - Windows

echo Cleaning temporary files...
del /q /f /s %TEMP%\*
del /q /f /s C:\Windows\Temp\*

echo Emptying the Recycle Bin...
rd /s /q C:\$Recycle.Bin

echo Cleaning Windows Update files...
rd /s /q C:\Windows\SoftwareDistribution\Download

echo Cleaning Microsoft Edge cache...
rd /s /q "%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache"
rd /s /q "%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cookies"

echo Cleaning Internet Explorer cache...
rd /s /q "%LOCALAPPDATA%\Microsoft\Windows\INetCache"

echo Cleaning system logs...
del /q /f /s C:\Windows\Logs\*

echo Cleaning Windows Error Reporting files...
rd /s /q C:\ProgramData\Microsoft\Windows\WER\*

echo Deleting old system restore points (requires administrator permissions)...
vssadmin delete shadows /all /quiet

echo Cleaning Prefetch files...
del /q /f /s C:\Windows\Prefetch\*

echo Cleaning old event logs...
wevtutil.exe cl Application
wevtutil.exe cl System
wevtutil.exe cl Security

echo Cleaning Google Chrome cache...
rd /s /q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"
echo Cleaning Mozilla Firefox cache...
rd /s /q "%APPDATA%\Mozilla\Firefox\Profiles\*\cache2"

echo Cleaning font cache...
del /f /s /q C:\Windows\ServiceProfiles\LocalService\AppData\Local\FontCache\*

echo Auto cleanup completed.
pause
