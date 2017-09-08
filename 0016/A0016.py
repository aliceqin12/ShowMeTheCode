import json
import xlwt

def writeNumbersToExcel(numbers_data):
    wb = xlwt.Workbook()
    table = wb.add_sheet('numbers')

    i = 0
    for numbers in numbers_data:
        for j in range(len(numbers)):
            table.write(i, j, numbers[j])
        i += 1

    wb.save('numbers.xls')

if __name__ == '__main__':
    filename = 'numbers.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        numbers_data = json.load(f)
        writeNumbersToExcel(numbers_data)