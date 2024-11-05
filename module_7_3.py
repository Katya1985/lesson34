import io
from pprint import pprint
name = 'test_file.txt'

class WordsFinder: # WordsFinder('file1.txt, file2.txt', 'file3.txt', ...)
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self): # подготовительный метод, который возвращает словарь
        all_words = {}
        for file_name in self.file_names:
            list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line_cls = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace(
                        '?', '').replace(';', '').replace(':', '').replace('-', '').split()
                    list.append(line_cls)
                all_words[self.file_names] = sum(list, [])
                return all_words
    def find(self, word):
        find_dict = {}

        for name, words in self.get_all_words().items():
            if word in words:
                find_dict[name] = words.index(word.lower()) + 1
            return find_dict

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_names, words in all_words.items():
            result[file_names] = words.count(word)
        return result

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего