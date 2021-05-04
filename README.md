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

## Function Details (Documentation)
Above functions will be found here documented.


### `is_api_installed`
** Syntax ** : `is_api_installed()`