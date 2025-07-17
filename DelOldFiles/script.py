import os
from _datetime import datetime, date, time
import sys

TODAY = datetime.today()
print(TODAY)
folder_path = r"C:\Кисляков\Скриншоты"
if os.path.exists(folder_path):
    print(f"Работаем с папкой: {folder_path}")
    files = os.listdir(folder_path)
    for file in files:
        full_path = os.path.join(folder_path, file)
        date_change = os.path.getmtime(full_path)
        print(f'{file} create {datetime.fromtimestamp(date_change)}')
        print(abs(TODAY - datetime.fromtimestamp(date_change)).da)
else:
    print("Папка не найдена!")


