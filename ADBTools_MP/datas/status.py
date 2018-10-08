# coding=utf-8
# @File  : status
# @Author: aojie654
# @Date  : 2018.06.12 21:03
# @Desc  : Status

from subprocess import getoutput as spgop

"""Check Status Of Phone"""
adc = 'adb devices'
fbc = 'fastboot devices'


def device_status():
    status = spgop(adc)

    # Judge devices status via end of stings.
    if status[-9:] != 'attached\n':
        if status[-13:] == 'unauthorized\n':
            status = 'unauthorized'
        elif status[-7:] == 'device\n':
            status = 'normal'
        elif status[-9:] == 'recovery\n':
            status = 'recovery'
        elif status[-9:] == 'sideload\n':
            status = 'sideload'
    else:
        status = spgop(fbc)
        if status[-8:] == 'fastboot':
            status = 'fastboot'
        else:
            status = 'null'
    return status


def print_status():
    status = device_status()
    # Print devices status
    if status == 'null':
        print('No devices connected.')
    elif status == 'unauthorized':
        print("You devices has connected but unauthorized, authorize it at first.")
    else:
        print('At now, your devices is  in ' + status + '.')
