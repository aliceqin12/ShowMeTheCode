def get_sensitive_words():
    file = open('filtered_words.txt', encoding='utf-8')

    sensitive_words = []
    for line in file:
        sensitive_words.append(line.rstrip())

    return sensitive_words

def get_filter_result(sentence):
    sensitive_words = get_sensitive_words()
    filter_sentence = ''
    for word in sensitive_words:
        filter_sentence = sentence.replace(word, '**')

    return filter_sentence

def main():
    print(get_filter_result('abc is jiangge'))

if __name__ == '__main__':
    main()