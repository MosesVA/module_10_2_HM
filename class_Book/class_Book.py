import json
import pickle


class BookEncoder(json.JSONEncoder):

    def default(self, obj):
        return {
            'title': obj.title,
            'author': obj.author,
            'year': obj.year,
            'methods': {
                'display_info': obj.display_info(),
                'is_classic': obj.is_classic()
            },
            'classname': obj.__class__.__name__
        }


class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"'{self.title}', автор {self.author}, {self.year} год."

    def is_classic(self):
        current_year = 2024
        return current_year - self.year > 50

    def to_json(self, filename):
        with open(f'{filename}.json', 'w', encoding='utf-8') as fh:
            json.dump(self, fh, cls=BookEncoder, ensure_ascii=False, indent=4)
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


my_book = Book('Очем я говорю, когда говорю о беге', 'Харуки Мураками', 2007)

my_book.to_json('my_book')
my_book.to_pickle('my_book.txt', 5)

print(my_book.from_pickle('my_book.txt'))
print(my_book.from_json('my_book.json'))

