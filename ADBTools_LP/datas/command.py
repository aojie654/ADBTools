# coding=utf-8
# @File  : command
# @Author: aojie654
# @Date  : 18-6-12 20:35
# @Desc  : Command

import os
from .status import device_status

overall_length = 90


def change_work_path():
    """Change The Work Path"""
    # Get the file path then go the parent folder
    cmd('cd ../..')
    wp = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/tmp'
    os.chdir(wp)


def print_format(message, addition='0', length=overall_length, overall_fill=' ', left_fill='', alignment='<', end='\n'):
    """Normal Format"""
    str_format = '{:' + overall_fill + alignment + str(length) + '}'
    str_var = '\033[' + addition + 'm' + left_fill + message + '\033[0m'
    print(str_format.format(str_var), end=end)


def print_menu(message):
    """Menu Format"""
    print_format(message, addition='0:32', overall_fill='=', alignment='^')


def print_command(message):
    """Command Format"""
    left_fill = '*' + (overall_length // 3 - 3) * ' '
    print_format(message, left_fill=left_fill, length=overall_length - 4, end='*\n')


def print_title():
    """Title Format"""
    cls()
    print('\n\n')
    message_var = "ADBTools is running... ^_^(v1.1.5 LP Beta)"
    addition_var = '1;34'
    print_format(message_var, addition=addition_var, alignment='^')
    print('\n')

def print_status():
    status = device_status()
    # Print devices status
    if status == 'null':
        print('No devices connected.')
    elif status == 'unauthorized':
        print("You devices has connected but unauthorized, authorize it at first.")
    else:
        print('At now, your devices is  in ' + status + '.')

def cmd(cmd0_v):
    """Using os model to excuse command"""
    os.system(cmd0_v)


def cls():
    """Clear Screen"""
    os.system('printf "\033c"')


def pause():
    """Using input to pause"""
    input('Press Enter to continue.')


def confirm(message):
    """Normal Confirm"""
    if input('Confirm to ' + message + '?(enter y to continue)') == 'y':
        return True
    else:
        return False


# Command Status
def command_error(ip):
    """Display error of has no that command"""
    cls()
    print(3 * '\n')
    print_format('Error: No command <' + ip.upper() + '> found!', addition='1;30;43', alignment='^', end=4 * '\n')
    pause()


def operation_finish():
    """Operation finished hint"""
    print('Operation finished.')
    pause()


def operation_error():
    """Display operate error info."""
    print_format("Operation failed.", addition='31;43', alignment='^', end=4 * '\n')
    pause()


def check_file(file):
    """Check file exist or not and permissions"""
    try:
        file = open(file)
        file.close()
    except FileNotFoundError:
        print("The file <" + file + "> is not found. Check the input please.")
        return False
    except PermissionError:
        print("You don't have permission to access to " + file + ". Change the permission please.")
        return False
    return True
