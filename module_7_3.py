class WordsFinder: # WordsFinder('file1.txt, file2.txt', 'file3.txt', ...)
    def __init__(self, *name_files):
        self.name_files = name_files


    def get_all_words(self): # подготовительный метод, который возвращает словарь
        all_words = {}
        for name_file in self.name_files:
            list = []
            with open(name_file, encoding='utf-8') as file:
                for line in file:
                    line_cls = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace(
                        '?', '').replace(';', '').replace(':', '').replace('-', '').split()
                    list.append(line_cls)
                all_words[name_file] = sum(list, [])
                return all_words
    def find(self, word):
        find_dict = {}

        for name, words in self.get_all_words().items():
            if word in words:
                find_dict[name] = words.index(word.lower()) + 1
            return find_dict


    def count(self, word):
        word_number = {}
        search_word = search_words.lower()
        for name_file, words in self.get_all_words().items():
            word_number[name_file] = words.count(search_word)
        return word_number


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
