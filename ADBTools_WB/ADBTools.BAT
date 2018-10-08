Setlocal enabledelayedexpansion
::CODER BY aojie POWERD BY iBAT
@echo off
cd /d %~dp0
mode con cols=110 lines=30

:menu
cls
title ADBTools Is Running... ^^_^^ (v1.0.4 Beta)
color 0d
cls
echo.
echo.
adb devices -l
fastboot devices
echo Press any key to main menu...
pause>nul
cls
echo.
echo.
echo =========================================MENU====================================================
echo *					REBOOT 							*
echo *												*
echo * [RN]Normal		[RR]Recovery		[BL]Bootloader		[BI]Boot Image		*
echo *												*
echo *					FLASH							*
echo *												*
echo * [SF]Sideload-Flash	[OM]OpenMobileAPI	[FR]Flash Recovery	[NA]NFC-All(NX549J)	*
echo *												*
echo *					Else							*
echo *												*
echo * [CP]Clear Password	[OC]Open CMD		[RS]Restart		[RM]Read ME		*
echo =================================================================================================
echo.
echo.
echo.
set /p p=Please enter the number: 
if /i %p%=="" goto menu
if /i %p%==rn goto rn
if /i %p%==rr goto rr
if /i %p%==bl goto bl
if /i %p%==bi goto bi
if /i %p%==sf goto sf
if /i %p%==om goto om
if /i %p%==fr goto fr
if /i %p%==na goto na
if /i %p%==cp goto cp
if /i %p%==oc goto oc
if /i %p%==rs goto rs
if /i %p%==rm goto rm
else goto er

:er
cls
title Error  0.0
color 04
echo.
echo.
echo.
echo No fuctions found, press any key to menu...
pause>nul
goto menu

:dn
echo.
echo.
echo  	Operate finished, press anykey to menu.
echo.
pause>nul
goto menu

:rn
cls
title Reboot As Normal...
color 04
echo.
echo.
echo.
set /p rns=Enter Y to reboot as normal:
if /i %rns%==Y (
echo.
echo --- Reboot as normal...
@start fastboot reboot
@start adb reboot
goto dn) else goto menu

:rr
cls
title Reboot To Recovery...
color 04
echo.
echo.
echo.
set /p rrs=Enter Y to reboot to recovery:
if /i %rrs%==Y (
echo.
echo.
echo --- Reboot to recovery ...
@start adb reboot recovery 
goto dn) else goto menu

:bl
cls
title Reboot To Bootloader...
color 0f
echo.
echo.
echo.
set /p bls=Enter Y to reboot to bootloader:
if /i %bls%==Y (
echo.
echo --- Reboot to bootloader ...
@start adb reboot-bootloader
goto dn) else goto menu

:bi
cls
title Boot image...
color 08
echo.
echo.
set /p bti=Please enter the image name (without ".img" included):
echo.
if not exist tmp/img/%bti%.img (echo %bti%.img is not in folder /tmp/img/, press anykey to menu & pause>nul & goto menu)
set /p bis=Enter Y to boot %bti%.img:
if /i %bis%==Y (
echo.
echo.
echo ---  Booting %bti%.img...
fastboot boot tmp/img/%bti%.img
goto dn) else goto menu

:sf
cls
title Flash by Sideload...
color 0a
echo.
echo.
set /p rom=Please enter the ROM name (without ".zip" included):
if not exist tmp/rom/%rom%.zip (echo %rom%.zip is not in folder /tmp/rom/, press anykey to menu & pause>nul & goto menu)
set /p sfs=Enter Y to flash %rom%.zip:
if /i %sfs%==Y (
echo.
echo.
echo ---  Flashing %rom%.zip by sideload...
adb sideload tmp/rom/%rom%.zip
goto dn) else goto menu

:om
cls
title Flashing OpenMobileAPI...
color 01
echo.
echo.
echo Are you sure to flash OpenMobileAPI?
echo.
set /p oms=Enter Y to flash OpenMobileAPI:
if /i %oms%==Y (
echo.
adb push tmp/system/etc/permissions/org.simalliance.openmobileapi.xml /system/etc/permissions/
adb shell chmod 644 /system/etc/permissions/org.simalliance.openmobileapi.xml
adb push tmp/system/framework/org.simalliance.openmobileapi.jar /system/framework/
adb shell chmod 644 /system/framework/org.simalliance.openmobileapi.jar
adb shell mkdir /system/priv-app/SmartcardService
adb shell chmod 755 /system/priv-app/SmartcardService
adb push tmp/system/priv-app/SmartcardService/SmartcardService.apk /system/priv-app/SmartcardService/
adb shell chmod 644 /system/priv-app/SmartcardService/SmartcardService.apk
goto dn) else goto menu

:fr
cls
title Flashing Recovery...
color 07
echo.
set /p rcv=Please enter the recovery image name (without ".img" included):
if not exist tmp/img/%rcv%.img (echo %rcv%.img is not in folder /tmp/img/, press anykey to menu & pause>nul & goto menu)
set /p frs=Enter Y to flash recovery image:
if /i %frs%==Y (
echo.
echo.
echo ---  Flashing %rcv%.img...
@fastboot flash recovery tmp/img/%rcv%.img
goto dn) else goto menu

:na
cls
title Enabling All Functions Of NFC for Nubia NX549J...
color 05
echo.
echo.
set /p nas=Enter Y enable all functions of NFC for Nubia NX549J:
if /i %nas%==Y (
adb push tmp/system/etc/libnfc-brcm.conf /system/etc
adb push tmp/system/etc/libnfc-brcm-20797b00.conf /system/etc
adb shell chmod 755 /system/etc/libnfc-brcm.conf
adb shell chmod 755 /system/etc/libnfc-brcm-20797b00.conf
goto dn) else goto menu

:cp
cls
title Cleaning Password...
color 0c
echo.
echo.
set /p cps=Enter Y to clear password:
if /i %cps%==Y(
echo Cleaning password...
adb shell rm /data/system/gatekeeper.pattern.key
adb shell rm /data/system/gatekeeper.password.key
goto dn) else goto menu

:oc
cls
title Using CMD...
color 04
echo.
echo After you done, you can enter "exit" in CMD to back to ADBTools.
echo.
echo.
set /p ocs=Enter Y to open CMD in current folder:
if /i %ocs%==Y (
cls
call cmd
goto menu) else goto menu

:rs
cls
adb kill-server
start ADBTools.bat
exit

:rm
cls
title Read ME
color 04
echo.
echo.
echo In this part, you can knows something about this tools.
echo.
echo 1. Sometimes you had entered nothing and pressed enter, then the programe will exit with no reason.
echo.
echo 2. Somethime you used the other tools just like MiFlash, adb will be shutdown by it, or the adb server
echo.
echo     went some wrong, so you need to restart adb server.
echo.
echo 3. When you using reboot to normal or reboot to bootloader, it will pop's two CMD windows, if your device
echo.
echo    had reboot success, then close the other CMD windows as fast as you can.
echo.
echo 4. Before you using the functions that related to img or zip files you should put them in folder ./tmp/img/ 
echo.
echo    or ./tmp/rom/ at first.
echo.
echo 5. Before you going flash with sideload, clear password, flash OpenMobileAPI or enable all functions 
echo.
echo    of NFC, you should mount or remount system partition on you phone in recovery at first maybe.
echo.
echo 6. The programe is still in testing, so if you discovered some bugs, try to get touch with me and report
echo.
echo    it(or them ;-P).
echo.
echo.
echo Press anykey to About ME
pause>nul
cls
title About Me.
color 0d
echo.
echo =================================================
echo *	Script		aojie654		*
echo *	Editor		aojie654		*
echo *	E-Mail		aojie654@live.cn	*
echo *			aojie815@gmail.com	*
echo *	Edit Time	2018-5-21 11:31:24	*
echo *	Version		1.0.4 Beta		*
echo =================================================
echo.
echo  	Press anykey to menu.
echo.
pause>nul
goto menu
