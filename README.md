## Termux API

A binding for Termux:API written in python.

If you don't know about Termux:API, visit [TermuxWiki](https://wiki.termux.com/wiki/Termux:API) for more details.

## Installation
In order to install this package you have to just run one command and you will be good to go.

Install via `pip`
> Maybe Unavailable Now.
```console
python3 -m pip install termux_api
```

Install via `git`
```console
git clone https://github.com/NurTasin/termux_api.git --depth=1
cd termux_api
python3 setup.py install
```

## API Functions
This package contains following functions. 
> To know more click on them
- [`is_api_installed`](#is_api_installed)
- [`install_api`](#install_api)
- [`get_battery_status`](#get_battery_status)
- [`get_camera_info`](#get_camera_info)
- [`get_camera_photo`](#get_camera_photo)
- [`get_clipboard`](#get_clipboard)
- [`set_clipboard`](#set_clipboard)
- [`get_contact_list`](#get_contact_list)
- [`get_location`](#get_location)
- [`set_brightness`](#set_brightness)
- [`dialog_confirm`](#dialog_confirm)
- [`dialog_speech`](#dialog_speech)
- [`dialog_spinner`](#dialog_spinner)
- [`dialog_radio`](#dialog_radio)
- [`dialog_counter`](#dialog_counter)
- [`dialog_date`](#dialog_date)
- [`dialog_checkbox`](#dialog_checkbox)
- [`dialog_sheet`](#dialog_sheet)
- [`dialog_time`](#dialog_time)
- [`dialog_text`](#dialog_text)
- [`show_dialog`](#show_dialog)
- [`download`](#download)
- [`list_sensors`](#list_sensors)
- [`get_sensor`](#get_sensor)
- [`show_toast`](#show_toast)
- [`vibrate`](#vibrate)
- [`toogle_torch`](#toogle_torch)
- [`get_tts_engines`](#get_tts_engines)
- [`tts_speak`](#tts_speak)
- [`get_telephony_deviceinfo`](#get_telephony_deviceinfo)
- [`get_telephony_cellinfo`](#get_telephony_cellinfo)
- [`telephony_call`](#telephony_call)
- [`get_call_log`](#get_call_log)
- [`biometric_auth`](#biometric_auth)
- [`transmit_ir`](#transmit_ir)

> Some functions may not work due to the Google's Restriction

## Function Details (Documentation)
Above functions will be found here documented.


### `is_api_installed`
**Syntax** : `is_api_installed()`

**Details** : Checks if Termux:API is installed or not.

**Returns** : `True` if Termux:API is properly installed. Otherwise it returns `False`

### `install_api`
**Syntax** : `install_api()`

**Details** : Tries to install the Termux:API cli tools.

**Returns** : `True` if installed successfully. Otherwise it prints the error and returns `False`

### `get_battery_status`
**Syntax** : `get_battery_status()`

**Details** : This function allows you to get the details about the device's battery.

**Returns** : A python dictionary that contains the detail.

The following code will print the percentage of the battery.
```python
from termux import *
bat_status=get_battery_status()
if bat_status["success"]:
    print("Percentage: ",bat_status["percentage"])
else:
    print("Something went wrong.")
```

### `get_camera_info`
**Syntax** : `get_camera_info()`

**Details** : This function will give you the details about all camera connected to the device.

**Returns** : A python dictionary where `data` key contains a list that holds the data about cameras.

### `get_camera_photo` 
**Syntax** : `get_camera_photo(filename:str,camera_id:int=0)`

**Details** : Access camera with id `camera_id` and captures a photo using it then saves it with name `filename`

**Returns** : A python dictionary that contains a `success` key with value `True` or `False`. That indicates if the operation was successful or not.

### `get_clipboard`
**Syntax** : `get_clipboard()`

**Details** : Tries to get whatever is in the clipboard of that device now.

**Returns** : A python dictionary that contains a key named `text` with the clipboard content.

The following code will print whatever in the clipboard is
```python
from termux import *
clipboard=get_clipboard()
if clipboard["success"]:
    print(clipboard["text"])
else:
    print("Something went wrong.")
```

### `set_clipboard`
**Syntax** : `set_clipboard(text:str)`

**Details** : Sets the string `text` to the clipboard.

**Returns** : A python dictionary that contains `success` key set to `True` if the operation was successful otherwise it is set to `False`

The following code will set the clipboard to the input string that you will give.
```python
from termux import *
stat=set_clipboard(str(input(">>")))
if stat["success"]:
    print("Clipboard updated successfully")
else:
    print("Something went wrong.")
```