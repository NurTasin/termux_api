from termux import *

print(
    "Your choice was: ",show_dialog(TERMUX_DIALOG_CONFIRM,title="Confirm Dialog Title",hint="Are you 18 or older?")["text"])
print("Your choice was: ",
show_dialog(TERMUX_DIALOG_CHECKBOX,title="Checkbox Dialog Title",
    options=["Tor","Buzz","Foo"]
)["text"]
)
print("Your choice was: ",show_dialog(TERMUX_DIALOG_COUNTER,title="select a number",minimum=10,maximum=20,start=15)['text'])