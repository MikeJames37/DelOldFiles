import os
from _datetime import datetime, date, time
import sys
import argparse

TODAY = datetime.today()
DAYS = 7
FOLDER_PATHS = ["C:\Кисляков\Скриншоты",
                "C:\Кисляков\Скриншоты—копия",
                "C:\Кисляков\Screen",]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--days", help="Введите количество дней", type=int)
    parser.add_argument("-f", "--folders", help="Введите пути к папкам с файлами",  nargs='+', required=True)
    return parser.parse_args()

def delete_old_files_in_folder(path: str, days: int):
    path = path.strip('"').replace("\\", "/")
    if os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            full_path = os.path.join(path, file)
            date_change = os.path.getmtime(full_path)
            file_day_life = abs(datetime.now() - datetime.fromtimestamp(date_change)).days
            if file_day_life > days:
                os.remove(full_path)
    else:
        print(f"Путь {path} не найден!")

def main():
    args = parse_args()
    print(f"Удаление файлов старше {args.days} дней")
    print(f"Папки для очистки: {args.folders}")
    for folder in args.folders:
        delete_old_files_in_folder(folder, args.days)



if __name__ == "__main__":
    main()
