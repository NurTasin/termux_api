## Termux API

A binding for Termux:API written in python.

If you don't know about Termux:API, visit [TermuxWiki](https://wiki.termux.com/wiki/Termux:API) for more details.

## Installation
In order to install this package you have to just run one command and you will be good to go.

Install via `pip`
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
- [`is_api_installed`](#is_api_installed)
- [`install_api`](#install_api)
- [`get_battery_status`](#get_battery_status)
- [`get_camera_info`](#get_camera_info)
- [`get_camera_photo`](#get_camera_photo)
- [`get_clipboard`](#get_clipboard)
- [`set_clipboard`](#set_clipboard)
- [`get_contact_list`](#get_contact_list)
