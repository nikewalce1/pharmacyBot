import csv
import os.path

class ReadCatalog():
    def __init__(self):
        pass

    def read_five_row(self, name_catalog):
        check_file = os.path.exists(f"Catalog\\{name_catalog}")
        if check_file == True:
            with open(f"Catalog\\{name_catalog}", encoding='utf-8') as r_file:
                list_catalog = []
                # Создаем объект DictReader, указываем символ-разделитель ","
                file_reader = csv.DictReader(r_file, delimiter=",")
                # Счетчик для подсчета количества строк и вывода заголовков столбцов
                count = 0
                # Считывание данных из CSV файла
                for row in file_reader:
                    list_catalog.append({
                        'Название':row["Название"],
                        'Цена':row["Цена"],
                        'Ссылка на изображение':row["Ссылка на изображение"]
                    })
                    count += 1
                    if count == 5:
                        return list_catalog
                return None
        else:
            return None
