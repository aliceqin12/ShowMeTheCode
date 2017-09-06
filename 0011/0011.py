def get_sensitive_words():
    file = open('filtered_words.txt', encoding='utf-8')

    sensitive_words = []
    for line in file:
        sensitive_words.append(line.rstrip())

    return sensitive_words

def get_filter_result(sentence):
    sensitive_words = get_sensitive_words()
    is_sensitive = False
    for word in sensitive_words:
        if word in sentence:
            is_sensitive = True
            break

    if is_sensitive:
        return 'Freedom'
    else:
        return 'Human Rights'

def main():
    print(get_filter_result('abc'))

if __name__ == '__main__':
    main()