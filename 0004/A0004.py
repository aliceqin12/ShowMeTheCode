import re
import os

def get_txt_word_num(filename):
    if not os.path.exists(filename):
        return

    try:
        file = open(filename, 'r')
        text = file.read()
        pattern = re.compile('[a-zA-Z]+')
        words = re.findall(pattern, text)
        print(words)
        return len(words)
    except IOError as err:
        print(err)
    finally:
        file.close()

def main():
    print(get_txt_word_num('On Friendship.txt'))

if __name__ ==  '__main__':
    main()