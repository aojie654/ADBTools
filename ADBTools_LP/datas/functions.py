# coding=utf-8
# @File  : functions
# @Author: aojie654
# @Date  : 2018.06.13 11:24
# @Desc  : Functions

from .command import cls, confirm, cmd, operation_finish, check_file, operation_error, operation_finish, pause, print_menu
from .status import device_status


# Reboot
def reboot_normal():
    """Reboot to normal mode"""
    cls()
    status = device_status()
    message = 'reboot'

    if status in ['normal', 'recovery', 'fastboot']:
        if confirm(message):
            if status == 'fastboot':
                command = 'fastboot reboot'
            else:
                command = 'adb reboot'
            cmd(command)
            operation_finish()
    else:
        status_hint("reboot", "normal, recovery or fastboot")


def reboot_recovery():
    """Reboot to recovery mode"""
    cls()
    status = device_status()
    message = 'reboot to recovery'
    if status in ['normal', 'recovery']:
        if confirm(message):
            command = 'adb reboot recovery'
            cmd(command)
            operation_finish()
    else:
        status_hint("reboot to recovery", "normal or recovery")


def reboot_bootloader():
    """Reboot to bootloader mode"""
    cls()
    status = device_status()
    message = 'reboot to bootloader'
    if status in ['normal', 'recovery', 'fastboot']:
        if confirm(message):
            if status == 'fastboot':
                command = 'fastboot reboot bootloader'
            else:
                command = 'adb reboot bootloader'
            cmd(command)
            operation_finish()
    else:
        status_hint("reboot to bootloader", "normal, recovery or fastboot")


def reboot_9008():
    """Reboot to EDL mode"""
    cls()
    status = device_status()
    message = 'reboot to 9008 mode'
    if status in ['normal', 'recovery']:
        if confirm(message):
            command = 'adb reboot edl'
            cmd(command)
            operation_finish()
    else:
        status_hint("reboot to Qualcomm 9008", "normal or recovery")


# Boot Image
def boot_image():
    """Boot image"""
    cls()
    status = device_status()
    if status == 'fastboot':
        file = './img/' + input('Input your boot image name:(without ".img" include.)')
        file += '.img'
        if check_file(file):
            message = 'boot image <' + file + '>'
            if confirm(message):
                command = 'fastboot boot ' + file
                cmd(command)
                operation_finish()
        else:
            operation_error()
    else:
        status_hint("boot image", "fastboot")


# Flash
def sideload_flash():
    """Flash rom via sideload mode"""
    cls()
    status = device_status()
    if status == 'sideload':
        file = './rom/' + input('Input your boot ROM name:(without ".zip" include)')
        file += '.zip'
        if check_file(file):
            message = 'sideload <' + file + '>'
            if confirm(message):
                command = 'adb sideload ' + file
                cmd(command)
                operation_finish()
        else:
            operation_error()
    else:
        status_hint("sideload flash ROM", "sideload")


def open_mobile_api():
    """Flash open mobile api to support sim-nfc"""
    cls()
    status = device_status()
    message = 'reboot to recovery'
    if status in ['normal', 'recovery']:
        if confirm(message):
            command = """ 
adb push system/etc/libnfc-brcm.conf /system/etc
adb push system/etc/libnfc-brcm-20797b00.conf /system/etc
adb shell chmod 755 /system/etc/libnfc-brcm.conf
adb shell chmod 755 /system/etc/libnfc-brcm-20797b00.conf
                        """
            cmd(command)
            operation_finish()
    else:
        status_hint("flash open mobile API", "recovery")


def flash_recovery():
    """Flash recovery image via fastboot"""
    cls()
    status = device_status()
    if status == 'fastboot':
        file = 'img/' + input('Input your recovery image name:(without ".img" include.)')
        file += '.img'
        if check_file(file):
            message = 'flash recovery image <' + file + '>'
            if confirm(message):
                command = 'fastboot flash recovery ' + file
                cmd(command)
                operation_finish()
        else:
            operation_error()
    else:
        status_hint("flash recovery", "fastboot")


def flash_boot():
    """Flash boot image via fastboot"""
    cls()
    status = device_status()
    if status == 'fastboot':
        file = './img/' + input('Input your boot image name:(without ".img" include.)')
        file += '.img'
        if check_file(file):
            message = 'flash boot image <' + file + '>'
            if confirm(message):
                command = 'fastboot flash boot ' + file
                cmd(command)
                operation_finish()
        else:
            operation_error()
    else:
        status_hint("flash boot image", "fastboot")


def enable_nfc_all():
    """Enable all functions of NFC of NX549J"""
    cls()
    status = device_status()
    if status == 'recovery':
        message = 'enable all nfc functions for nubia NX549J'
        if confirm(message):
            command = """ 
adb push ./system/etc/libnfc-brcm.conf /system/etc
adb push ./system/etc/libnfc-brcm-20797b00.conf /system/etc
adb shell chmod 755 /system/etc/libnfc-brcm.conf
adb shell chmod 755 /system/etc/libnfc-brcm-20797b00.conf
                            """
            cmd(command)
            operation_finish()
    else:
        status_hint("enable all nfc functions", "recovery")


# Else Functions
def clear_password():
    """Clear Password"""
    cls()
    status = device_status()
    if status == 'recovery':
        message = 'clear password'
        if confirm(message):
            command = """ 
    adb shell rm /data/system/gatekeeper.pattern.key
    adb shell rm /data/system/gatekeeper.password.key
            """
            cmd(command)
        operation_finish()
    else:
        status_hint("clear password", "recovery")


def status_hint(action, modes):
    """Remind user to make phone in the right status."""
    print(2 * '\n' + "Phone can only " + action + " when it as in " + modes + " mode." + 2 * '\n')
    pause()


def manual_command():
    """Call Bash"""
    cls()
    print('After you finished, you can enter "exit" in bash to back to main menu.')
    pause()
    cmd('bash')


def restart_adb():
    """Restart ADB Server"""
    cls()
    cmd('adb kill-server')


def read_me():
    """Read ME"""
    cls()
    print_menu("READ ME")
    string = """
In this part, you can knows something about this tools.

1.  Sometimes you had entered nothing and pressed enter, then the program will
    exit with no reason.

2.  Sometimes you used the other tools just like MiFlash, adb will be shutdown
    by it, or the adb server went some wrong, so you need to restart adb server.

3.  When you using reboot to normal or reboot to bootloader, it will pop's two 
    CMD windows, if your device reboot success, then close the other CMD windows
    as fast as you can.
    (P.S.   In python edition, this problem has been fixed. ^_^)

4.  Before you using the functions that related to img or zip files you should
    put them in folder ./tmp/img/ or ./tmp/rom/ at first.
    
There are two points in next page.
    """
    print(string)
    pause()
    string = """
    
5.  Before you going flash with sideload, clear password, flash OpenMobileAPI 
    or enable all functions of NFC, you should mount or remount system partition
    on you phone in recovery at first maybe.
    
6.  The program is still in testing, so if you discovered some bugs, try to get
    touch with me and report it(or them ;-P).
    print(string)
=========================================
*   Script      aojie654                *
*   Editor      aojie654		*
*   E-Mail      aojie654@live.cn	*
*       	aojie815@gmail.com	*
*   Edit Time   2018-6-25 21:31:03	*
*   Version	1.1.5 LP Beta 		*
=========================================
    """
    print(string)
    pause()
