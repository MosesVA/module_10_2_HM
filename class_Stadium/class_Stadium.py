import json
import pickle


class JSONDataAdapter:

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Stadium):
            with open('my_stadium.json', 'w', encoding='utf-8') as fh:
                json.dump({
                    'name': obj.name,
                    'area': obj.area,
                    'capacity': obj.capacity
                }, fh, indent=4)
            return 'Файл успешно создан.'

    @staticmethod
    def from_json(filename):
        with open(filename, 'r', encoding='utf-8') as fh:
            obj = json.load(fh)

        try:
            stadium = Stadium(obj['name'], obj['area'], obj['capacity'])
            return stadium
        except AttributeError:
            print('Неверная структура!')


class Stadium:

    def __init__(self, name, area, capacity):
        self.name = name
        self.area = area
        self.capacity = capacity

    def __repr__(self):
        return f'Name {self.name}, Area {self.area}, Capacity {self.capacity}'

    def open_stadium(self):
        return f'Стадион {self.name} открыт!'

    def close_stadium(self):
        return f'Стадион {self.name} закрыт!'

    def to_pickle(self, filename, protocol):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file, protocol)
        return 'Произведен пиклинг в файл'

    @staticmethod
    def from_pickle(pickled_file):
        with open(pickled_file, 'rb') as file:
            unpickle_data = pickle.load(file)
        return unpickle_data


my_stadium = Stadium('Uragan', 60000, 50000)

my_stadium.to_pickle('my_stadium.txt', 5)
print(my_stadium.from_pickle('my_stadium.txt'))
print()

print(my_stadium)
json_stadium = JSONDataAdapter.to_json(my_stadium)
print(json_stadium)
print()

stadium_obj = JSONDataAdapter.from_json('my_stadium.json')
print(stadium_obj)
