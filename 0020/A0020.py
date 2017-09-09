import xlrd
import re

def get_total_call_time(excelPath):
    wb = xlrd.open_workbook(excelPath)
    ws = wb.sheet_by_index(0)

    i = 9
    hours, minutes, seconds = 0, 0, 0
    while True:
        time_str = ws.cell(rowx=i, colx=4).value
        i += 1
        if time_str == '':
            break
        results = re.findall('\d+', time_str)
        if len(results) == 3:
            hours += int(results[0])
            minutes += int(results[1])
            seconds += int(results[2])
        elif len(results) == 2:
            minutes += int(results[0])
            seconds += int(results[1])
        else:
            seconds += int(results[0])

    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60

    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 50

    return hours, seconds, seconds

if __name__ == '__main__':
    hours, minutes, seconds = get_total_call_time('detailBill.xls')
    print('通话时间： %s:%s:%s' % (hours, minutes, seconds))