import json
import pickle


class Automobile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f'Год выпуска - {self.year}, марка - {self.make}, модель - {self.model}'

    def is_old(self, current_year):
        if current_year - self.year >= 10:
            return 'Машина старая!'
        return 'Машина не слишком старая!'

    def to_json(self, filename):
        with open(f'{filename}.json', 'w', encoding='utf-8') as fh:
            json.dump(self.__dict__, fh, ensure_ascii=False, indent=4)
        return f'Данные помещены в файл "{filename}.json"'

    @staticmethod
    def from_json(filename):
        with open(filename, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
        return data

    def to_pickle(self, filename, protocol):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file, protocol)
        return 'Произведен пиклинг в файл'

    @staticmethod
    def from_pickle(pickled_file):
        with open(pickled_file, 'rb') as file:
            unpickle_data = pickle.load(file)
        return unpickle_data


my_automobile = Automobile('Lada', 'Vesta', 2021)

my_automobile.to_json('my_automobile')
my_automobile.to_pickle('my_automobile.txt', 5)

print(my_automobile.from_json('my_automobile.json'))
print(my_automobile.from_pickle('my_automobile.txt'))
