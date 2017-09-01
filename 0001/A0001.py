#!/usr/bin/python
#encoding=utf-8
import uuid

def generate_activation_code(count, length = 33):
    """
    :param count: the number of activation_code you want to get
    :param length: the length of each activation_code and length <= 33
    """
    code_list = []
    for i in range(count):
        temp = str(uuid.uuid4()).replace('-', '')[:length]
        if temp not in code_list:
            code_list.append(temp)
    return code_list

def main():
    count = 200
    length = 10
    code_list = generate_activation_code(count, length)
    for i in range(count):
        print(code_list[i])

if __name__ == '__main__':
    main()