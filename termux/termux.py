from json import loads,dumps
import subprocess
from typing import *

#constants

TERMUX_DIALOG_CONFIRM:Final[str]="confirm"
TERMUX_DIALOG_CHECKBOX:Final[str]="checkbox"
TERMUX_DIALOG_COUNTER:Final[str]="counter"
TERMUX_DIALOG_DATE:Final[str]="date"
TERMUX_DIALOG_RADIO:Final[str]="radio"
TERMUX_DIALOG_SHEET:Final[str]="sheet"
TERMUX_DIALOG_SPINNER:Final[str]="spinner"
TERMUX_DIALOG_SPEECH:Final[str]="speech"
TERMUX_DIALOG_TEXT:Final[str]="text"
TERMUX_DIALOG_TIME:Final[str]="time"

TERMUX_TOAST_POSITION_MIDDLE:Final[str]="middle"
TERMUX_TOAST_POSITION_TOP:Final[str]="top"
TERMUX_TOAST_POSITION_BOTTOM:Final[str]="bottom"

TTS_STREAM_MUSIC:Final[str]="MUSIC"
TTS_STTEAM_NOTIFICATION:Final[str]="NOTIFICATION"
TTS_STREAM_RING:Final[str]="RING"

#utilities

def is_api_installed() -> bool:
    obj,rc,err=execute(["termux-sensor","-h"])
    
    return rc==0

def install_api() -> bool:
    obj,rc,err=execute(["pkg","update"])
    if rc==0:
        obj,rc,err=execute(["pkg","install","termux-api","-y"])
        if rc==0:
            print("Now Install The Termux:API android app from Play Store.")
            return True
        else:
            print("Unable to install termux-api.")
            return False
    else:
        print("Unable to update packages.. Please Connect to the internet and try again.")
        return False
    return False

def execute(cmd:List[str], encoding:str='UTF-8', timeout:Union[int,None]=None, shell:Union[str,bool]=False):
    proc = subprocess.Popen(cmd, stdin=subprocess.DEVNULL,
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
    output, error = proc.communicate(timeout=timeout)
    # rstrip('\n') may be more accurate, actually nothing may be better
    output = output.decode(encoding).rstrip()
    error = error.decode(encoding).rstrip()
    rc = proc.returncode
    return (output, rc, error)


#api bindings

def get_battery_status() -> dict:
    obj,rc,err=execute(["termux-battery-status"])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj


def get_camera_info() -> dict:
    obj,rc,err=execute(["termux-camera-info"])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj={"data":loads(obj)}
    jsonobj["success"]=True
    return jsonobj

def get_camera_photo(filename:str,camera_id:int=0) -> dict:
    obj,rc,err=execute(["termux-camera-photo","-c",camera_id,filename])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj={}
    jsonobj["success"]=True
    return jsonobj

def get_clipboard() -> dict:
    obj,rc,err=execute(["termux-clipboard-get"])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj={}
    jsonobj["text"]=obj
    jsonobj["success"]=True
    return jsonobj

def set_clipboard(text:str) -> dict:
    obj,rc,err=execute(["termux-clipboard-set",text])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj={}
    jsonobj["text"]=text
    jsonobj["success"]=True
    return jsonobj

def get_contact_list() -> dict:
    obj,rc,err=execute(["termux-contact-list"])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj={}
    jsonobj["data"]=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def get_location(provider:str="gps", req_type:str="once") -> dict:
    obj,rc,err=execute(["termux-location","-p",provider,"-r",req_type])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def set_brightness(level:int) -> dict:
    obj,rc,err=execute(["termux-brightness",str(level)])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj



def dialog_confirm(title:str,hint:str="") -> dict:
    obj,rc,err=execute(["termux-dialog","confirm","-t",title,"-i",hint])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_speech(title:str,hint:str="") -> dict:
    obj,rc,err=execute(["termux-dialog","speech","-t",title,"-i",hint])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj
    
def dialog_spinner(title:str,options:List[str]) -> dict:
    value=','.join(options)
    
    obj,rc,err=execute(["termux-dialog","spinner","-v",value,"-t",title])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_radio(title:str,options:List[str]) -> dict:
    value=','.join(options)
    
    obj,rc,err=execute(["termux-dialog","radio","-v",value,"-t",title])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_counter(title:str,minimum:int,maximum:int,start:int) -> dict:
    value="{},{},{}".format(minimum,maximum,start)
    
    obj,rc,err=execute(["termux-dialog","counter","-r",value,"-t",title])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_date(title:str,format:str="dd-MM-yyyy k:m:s") -> dict:
    obj,rc,err=execute(["termux-dialog","date","-t",title,"-d",format])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_checkbox(title:str,options:List[str]) -> dict:
    value=','.join(options)
    
    obj,rc,err=execute(["termux-dialog","checkbox","-v",value,"-t",title])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_sheet(title:str,options:List[str]) -> dict:
    value=','.join(options)+'"'
    
    obj,rc,err=execute(["termux-dialog","sheet","-v",value,"-t",title])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_time(title:str) -> dict:
    obj,rc,err=execute(["termux-dialog","time","-t",title])
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def dialog_text(title:str,hint:str="",multiple:bool=True,number:bool=False,password:bool=False) -> dict:
    if number and multiple:
        multiple=False
    
    command=["termux-dialog","text","-t",title]
    
    if multiple:
        command.append("-m")
    
    if number:
        command.append("-n")
    
    if password:
        command.append("-p")
        
    obj,rc,err=execute(command)
    
    if not rc==0:
        return {'success':False,"error":err}
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj


def show_dialog(mode:str,**conf):
    if mode==TERMUX_DIALOG_CONFIRM:
        return dialog_confirm(**conf)
    elif mode==TERMUX_DIALOG_CHECKBOX:
        return dialog_checkbox(**conf)
    elif mode==TERMUX_DIALOG_COUNTER:
        return dialog_counter(**conf)
    elif mode==TERMUX_DIALOG_DATE:
        return dialog_date(**conf)
    elif mode==TERMUX_DIALOG_RADIO:
        return dialog_radio(**conf)
    elif mode==TERMUX_DIALOG_SHEET:
        return dialog_sheet(**conf)
    elif mode==TERMUX_DIALOG_SPINNER:
        return dialog_spinner(**conf)
    elif mode==TERMUX_DIALOG_SPEECH:
        return dialog_speech(**conf)
    elif mode==TERMUX_DIALOG_TEXT:
        return dialog_text(**conf)
    elif mode==TERMUX_DIALOG_TIME:
        return dialog_time(**conf)
    else:
        raise ValueError(f"Dialog Mode {mode} is undefined.")


def download(url:str,path:str,title:str="Downloading file",description:str="") -> dict:
    obj,rc,err=execute(["termux-download","-t",title,"-d",description,"-p",path,url])
    if obj=="":
        return {
            "success":True,
        }
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    try:
        jsonobj=loads(obj)
    except:
        jsonobj={}
    
    jsonobj["success"]=True
    return jsonobj

def list_sensors() -> dict:
    obj,rc,err=execute(["termux-sensor","-l"])
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    return jsonobj

def get_sensor(sensor_name:str) -> dict:
    obj,rc,err=execute(["termux-sensor","-s",sensor_name,"-n","1"])
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    jsonobj=loads(obj)
    jsonobj['success']=True
    return jsonobj

def show_toast(text:str,bg:str="gray",fg:str="white",position:str=TERMUX_TOAST_POSITION_BOTTOM,short:bool=False)->dict:
    command:List[str]=["termux-toast","-b",bg,"-c",fg,"-g",position]
    if short:
        command.append("-s")
    
    obj,rc,err=execute(command)
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    return {
        "success":True
    }

def vibrate(duration:int=100,force:bool=True) -> dict:
    command:List[str]=["termux-vibrate","-d",str(duration)]
    if force:
        command.append("-f")
    
    obj,rc,err=execute(command)
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    return {
        "success":True
    }

def toogle_torch(on:bool):
    obj,rc,err=execute(["termux-torch","on" if on else "off"])
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    return {
        "success":True
    }

def get_tts_engines() -> dict:
    obj,rc,err=execute(["termux-tts-engines"])
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    
    return jsonobj

def tts_speak(text:str,engine:str,rate:float=1.0,pitch:float=1.0,stream:str=TTS_STREAM_MUSIC) -> dict:
    command:List[str]=["termux-tts-speak","-e",engine,"-r",str(rate),"-p",str(pitch),"-s",stream,text]
    obj,rc,err=execute(command)
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    return {
        "success":True
    }

def get_telephony_deviceinfo() -> dict:
    obj,rc,err=execute(["termux-telephony-deviceinfo"])
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    
    return jsonobj

def get_telephony_cellinfo()->dict:
    obj,rc,err=execute(["termux-telephony-cellinfo"])
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    
    return jsonobj

def telephony_call(phone:str) -> dict:
    obj,rc,err=execute(["termux-telephony-call",phone])
    
    if not rc==0:
        return {
            "success":True,
            "error":err
        }
    
    return {
        "success":True
    }

def get_call_log(limit:int=10,offset:int=0) -> dict:
    obj,rc,err=execute(["termux-call-log","-l",str(limit),"-o",str(offset)])
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    
    return jsonobj


def biometric_auth() -> dict:
    obj,rc,err=execute(["termux-fingerprint"])
    
    if not rc==0:
        return {
            "success":False,
            "error":err
        }
    
    jsonobj=loads(obj)
    jsonobj["success"]=True
    
    return jsonobj

def transmit_ir(pattern:List[int]) -> dict:
    value=','.joint(pattern)
    obj,rc,err=execute(["termux-infrared-transmit","-f",value])
    
    if not rc==0:
        return {
            "success":True,
            "error":err
        }
    
    return {
        "success":True
    }
