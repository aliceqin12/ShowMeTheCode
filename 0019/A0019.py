import xlrd
import json
import html
from xml.dom.minidom import Document
from collections import OrderedDict

comment = '''
            数字信息
'''

def ReadExcelFileToList(excelpath):
    wb = xlrd.open_workbook(excelpath)
    ws = wb.sheets()[0]

    numbers_list = []
    for i in range(3):
        temp_list = []
        for j in range(3):
            temp_list.append(int(ws.cell(i, j).value))
        numbers_list.append(temp_list)
    return numbers_list

def writeDataToXml(numbers_list, xmlpath):
    doc = Document()
    root_node = doc.createElement('root')
    doc.appendChild(root_node)

    stu_node = doc.createElement('numbers')
    root_node.appendChild(stu_node)

    note_node = doc.createComment(comment)
    stu_node.appendChild(note_node)

    dict_node = doc.createTextNode(json.dumps(numbers_list, ensure_ascii=False, indent=4))
    stu_node.appendChild(dict_node)

    with open(xmlpath, "w", encoding='utf8') as file:
        transform = html.unescape(doc.toprettyxml(indent=''))
        file.write(transform)

if __name__ == '__main__':
    excelpath = 'numbers.xls'
    xmlpath = 'numbers.xml'
    numbers_list = ReadExcelFileToList(excelpath)
    writeDataToXml(numbers_list, xmlpath)
