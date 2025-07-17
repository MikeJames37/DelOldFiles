import os
from _datetime import datetime, date, time
import sys

TODAY = datetime.today()
MAX_DAY_LIFE = 300
print(TODAY)
folder_path = r"C:\Кисляков\Скриншоты"
if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    print(f"Работаем с папкой: {folder_path}, в ней {len(files)} файлов")
    for file in files:
        full_path = os.path.join(folder_path, file)
        date_change = os.path.getmtime(full_path)
        file_day_life = abs(TODAY - datetime.fromtimestamp(date_change)).days
        print(f'{file} create {datetime.fromtimestamp(date_change)}, {file_day_life} ago')
        if file_day_life > MAX_DAY_LIFE:
            print(f'{file} create {datetime.fromtimestamp(date_change)}, {file_day_life} ago')
            os.remove(full_path)
            print(len(files))
    print(f"Работаем с папкой: {folder_path}, в ней {len(files)} файлов")

else:
    print("Папка не найдена!")


