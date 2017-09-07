import json
import xlrd
import xlwt

def writeCityDataToExcel(city_data):
    wb = xlwt.Workbook()
    table = wb.add_sheet('city')

    i = 0
    for number in city_data:
        city_name = city_data.get(number)

        table.write(i, 0, number)
        table.write(i, 1, city_name)
        i += 1

    wb.save('city.xls')

if __name__ == '__main__':
    filename = 'city.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        city_data = json.load(f)
        writeCityDataToExcel(city_data)