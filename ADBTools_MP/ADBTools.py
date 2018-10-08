# coding=utf-8
# @File  : ADBTools
# @Author: aojie654
# @Date  : 2018.06.12 12:11
# @Desc  : ADB Tools

from datas.print_info import menu_info_main
from datas.command import change_work_path

esc = True

change_work_path()
while esc:
    esc = menu_info_main()
