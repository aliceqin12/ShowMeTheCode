import os
import re
import  collections

ignore_words=['a','an','is','it','are','of','by','the','and','for','in','to']

def get_important_words(file):
    try:
        f = open(file, encoding='utf8')
        words_counter = collections.Counter()

        for line in f:

            words = re.findall('[a-zA-Z]+', line.lower())
            words_counter.update(words)

        f.close()

        most_important_words = []
        min_count = 2
        for (word, count) in words_counter.most_common():
            if word not in ignore_words:
                if count >= min_count:
                    most_important_words.append(word)
                    min_count = count
                else:
                    break
            else:
                continue

        print(most_important_words)

    except IOError as error:
        print(error)

if __name__ == '__main__':
    filepath = os.path.abspath('.')
    for dirpath, dirname, dirfiles in os.walk(filepath):
        for file in dirfiles:
            if file.endswith('.txt'):
                abspath = os.path.join(dirpath, file)
                if os.path.isfile(abspath):
                    get_important_words(abspath)