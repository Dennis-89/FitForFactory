# Fit for Factory

Installation:
--------------
Clone this repository:
```
git clone https://github.com/Dennis-89/FitForFactory.git
```
Next make `install.sh` and `uninstall.sh` executable:
```
chmod +x install.sh
chmod +x uninstall.sh
```
Note: Execute the file with `sudo` you need permissions to install all requirements.
```
sudo ./install.sh
```
Run Application:
---------------
Make sure Bluetooth is enabled. See example Commands and the [Documentation](https://www.bluez.org/)
```
sudo systemctl status bluetooth 
sudo systemctl start bluetooth
sudo systemctl enable bluetooth 
bluetoothctl power on
```
You can run the application via the Desktop-Icon.

Uninstall:
```
sudo ./uninstall.sh
```