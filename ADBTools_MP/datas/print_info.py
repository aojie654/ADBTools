# coding=utf-8
# @File  : print_info
# @Author: aojie654
# @Date  : 2018.06.12 21:44
# @Desc  : Print Info

from .functions import read_me, restart_adb, reboot_normal, reboot_recovery, reboot_bootloader, reboot_9008, \
    boot_image, sideload_flash, open_mobile_api, flash_recovery, flash_boot, enable_nfc_all, clear_password, \
    manual_command
from .command import print_command, print_format, print_menu, print_title, print_status,command_error

# Print Functions


def menu_info_main():
    """Print Main Menu"""
    print_title()
    print_status()
    print_menu("MENU")
    print_command("[RB]REBOOT and BOOT IMAGE")
    print_command("[FL]FLASH")
    print_command("[EL]ELSE")
    print_command("[RM]Read ME")
    print_command("[RS]Restart")
    print_menu('=')
    print()
    esc = action_menu()
    return esc


def action_menu():
    """Actions of Main Menu"""
    # Input
    input_var = input("Please enter the command: (use 'q' to exit.)").lower()

    if input_var == 'rb':
        menu_info_reboot()
    elif input_var == 'fl':
        menu_info_flash()
    elif input_var == 'el':
        menu_info_else()
    elif input_var == 'rm':
        read_me()
    elif input_var == 'rs':
        restart_adb()
    elif input_var == 'q':
        return False
    else:
        command_error(input_var)
    return True


# Print REBOOT
def menu_info_reboot():
    """Print menu of reboot"""
    print_title()
    print_status()
    print_menu("REBOOT and BOOT IMAGE")
    print_command("[RN]Reboot Normal")
    print_command("[RR]Recovery")
    print_command("[BL]Bootloader")
    print_command("[QM]Qualcomm 9008")
    print_command("[BI]Boot Image")
    print_command("[MN]Back Menu")
    print_menu('=')
    print()
    action_reboot()


def action_reboot():
    """Actions of reboot"""
    # Input
    input_var = input("Please enter the command: ").lower()

    if input_var == 'rn':
        reboot_normal()
    elif input_var == 'rr':
        reboot_recovery()
    elif input_var == 'bl':
        reboot_bootloader()
    elif input_var == 'qm':
        reboot_9008()
    elif input_var == 'bi':
        boot_image()
    elif input_var == 'mn':
        menu_info_main()
    else:
        command_error(input_var)


# Print FLASH
def menu_info_flash():
    """Print Flash Menu"""
    print_title()
    print_status()
    print_menu("FLASH")
    print_command("[SF]Sideload-Flash")
    print_command("[OA]OpenMobile API")
    print_command("[FR]Flash Recovery")
    print_command("[FB]Flash Boot")
    print_command("[EN]Enable NFC All")
    print_command("[MN]Back Menu")
    print_menu('=')
    print()
    action_flash()


def action_flash():
    """Actions of flash"""
    # Input
    input_var = input("Please enter the command: ").lower()

    if input_var == 'sf':
        sideload_flash()
    elif input_var == 'oa':
        open_mobile_api()
    elif input_var == 'fr':
        flash_recovery()
    elif input_var == 'fb':
        flash_boot()
    elif input_var == 'en':
        enable_nfc_all()
    elif input_var == 'mn':
        menu_info_main()
    else:
        command_error(input_var)


# Print ELSE
def menu_info_else():
    """Print Else Menu"""
    print_title()
    print_status()
    print_menu("ELSE")
    print_command("[CP]Clear Password")
    print_command("[MC]Manual Command")
    print_command("[MN]Back Menu")
    print_menu('=')
    print()
    action_else()


def action_else():
    """Actions of Else"""
    # Input
    input_var = input("Please enter the command: ").lower()

    if input_var == 'cp':
        clear_password()
    elif input_var == 'mc':
        manual_command()
    elif input_var == 'mn':
        menu_info_main()
    else:
        command_error(input_var)
