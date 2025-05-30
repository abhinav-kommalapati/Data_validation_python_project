################# DATA Validation Module#######################

import re
import os

def nameValidation(name):
    if(len(name) > 0 and name.isalpha()):
        return "Valid Name"
    else:
        return "Invalid Name"


def mobNumValidation(mob):
    if(len(mob) == 10 and mob.isdigit()):
        return "Valid Number"
    else:
        return "Invalid Number"


def passwordValidation(pwd):
    caps = len(re.findall('[A-Z]', pwd))
    lows = len(re.findall('[a-z]', pwd))
    digs = len(re.findall('[0-9]', pwd))
    spec = len(re.findall('[^A-Za-z0-9]', pwd))
    pwdlen = len(pwd)

    if(caps > 0 and lows > 0 and digs > 0 and spec > 0 and pwdlen >= 8):
        return "Valid Password"
    else:
        return "Invalid password"


def ipaddressValidation(ipaddr):
    patip = '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
    res = re.findall(patip,ipaddr)
    if(res):
        return "Valid IP"
    else:
        return "Invalid IP"


def dateValidation(dt):
    patd = '[0-9]{2}[^A-Za-z0-9][0-9]{2}[^A-Za-z0-9][0-9]{4}'
    res = re.findall(patd,dt)
    if (res):
        return "Valid Date"
    else:
        return "Invaid Date"


def emailValidation(em):
    pate = '[A-Za-z0-9]{1,}[@][A-Za-z0-9]{1,}[.]com'
    res = re.findall(pate, em)
    if (res):
        return "Valid Email"
    else:
        return "Invaid Email"


def fileTypeValidation(filename):
    filetypes = {'excel' : '.xlsx',
                 'csv' : '.csv',
                 'text' : '.txt',
                 'log' : '.log'
                 }
    valid = 0
    for name,extn in filetypes.items():
        if(filename.endswith(extn)):
            valid = 1
            break
    if(valid == 1):
        return "Valid File"
    else:
        return "Invalid File"


def filesizeValidation(file):
    file_size = os.path.getsize(file)
    if(file_size > 5000):
        return "oversize"
    else:
        return "fileok"








