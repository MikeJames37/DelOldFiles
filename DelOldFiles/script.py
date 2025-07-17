import os
from _datetime import datetime, date, time
import sys

TODAY = datetime.today()
DAYS = 7
FOLDER_PATHS = ["C:\Кисляков\Скриншоты",
                "C:\Кисляков\Скриншоты—копия",
                "C:\Кисляков\Screen",]


def deleteObjectsInFolder(path: str):
    if os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            full_path = os.path.join(path, file)
            date_change = os.path.getmtime(full_path)
            file_day_life = abs(TODAY - datetime.fromtimestamp(date_change)).days
            if file_day_life > DAYS:
                os.remove(full_path)
    else:
        print(f"Путь {path} не найден!")

def cleanFolders(folders: list):
    for path in folders:
        correct_path = path.replace("\\", "/")
        print(correct_path)
        deleteObjectsInFolder(correct_path)


cleanFolders(FOLDER_PATHS)
