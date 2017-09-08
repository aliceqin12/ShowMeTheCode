import xlrd
import json
import html
from xml.dom.minidom import Document
from collections import OrderedDict

comment = '''
            城市信息
'''

def ReadExcelFileToDict(excelpath):
    wb = xlrd.open_workbook(excelpath)
    ws = wb.sheets()[0]

    city_dict = OrderedDict()
    for i in range(3):
        id = ws.cell(i, 0).value
        city = ws.cell(i, 1).value
        city_dict[id] = city

    return city_dict

def writeDataToXml(city_dict, xmlpath):
    doc = Document()
    root_node = doc.createElement('root')
    doc.appendChild(root_node)

    stu_node = doc.createElement('students')
    root_node.appendChild(stu_node)

    note_node = doc.createComment(comment)
    stu_node.appendChild(note_node)

    dict_node = doc.createTextNode(json.dumps(city_dict, ensure_ascii=False, indent=4))
    stu_node.appendChild(dict_node)

    with open(xmlpath, "w", encoding='utf8') as file:
        transform = html.unescape(doc.toprettyxml(indent=''))
        file.write(transform)

if __name__ == '__main__':
    excelpath = 'city.xls'
    xmlpath = 'city.xml'
    city_dict = ReadExcelFileToDict(excelpath)
    writeDataToXml(city_dict, xmlpath)
