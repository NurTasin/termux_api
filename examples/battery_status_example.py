from termux import *

"""
battery_status() returns a python dictionary that contains fields below:
    1.health [str] : returns the health of the battery
    2.percentage [int] : returns the percentage of the battery
    3.plugged [str] : returns the plugged status
    4.temperature (°C) [float] : returns current temperature of the battery
    5.current [int] : returns how many current is flowing through the battery
    6.success [bool] : returns True if successfully got the battery status otherwise returns False
    7.error [str] : returns the error message if any error occured otherwise this field will be absent

for more details visit: https://wiki.termux.com/wiki/Termux-battery-status
"""


battery_st=get_battery_status()

if battery_st['success']:
    print ("Percentage: {}".format(battery_st["percentage"]))
    print ("Health: {}".format(battery_st["health"]))
    print ("Plugged: {}".format(battery_st["plugged"]))
    print ("Temperature: {}".format(battery_st["temperature"]))
    print ("Current: {}".format(battery_st["current"]))

else:
    print("An error occured!")
    print("[ERROR]\n{}".format(battery_st["error"]))