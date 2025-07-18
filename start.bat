@echo off
setlocal enabledelayedexpansion

:: Параметры по умолчанию
set DEFAULT_DAYS=7
set DEFAULT_FOLDERS="C:\Users\User\Pictures\Saved Pictures"

:: Чтение количества дней (первый параметр)
set DAYS=%1

:: Если дни не указаны, используем значение по умолчанию
if "%DAYS%"=="" (
    set DAYS=%DEFAULT_DAYS%
    shift
) else (
    shift
)

:: Собираем все оставшиеся параметры как пути
set FOLDERS=
:loop
if "%1"=="" goto endloop
set FOLDERS=!FOLDERS! "%1"
shift
goto loop
:endloop

:: Если пути не указаны, используем значения по умолчанию
if "!FOLDERS!"=="" set FOLDERS=%DEFAULT_FOLDERS%

:: Запуск Python-скрипта с параметрами
python DelOldFiles\script.py --days !DAYS! --folders !FOLDERS!
