import xml.etree.ElementTree as ET

tree = ET.parse('database/database.xml')
root = tree.getroot()

def database(x, y):
    info = []
    f = open('database/database.info', 'r')
    for i in range(4):
        l = f.readline()
        if i != 0: info.append(int(l.strip("\n").split("=")[1]))
    f.close()

    lesson = []
    for i in range(info[1]):
        lesson.append([])
        for q in range(info[0]):
            lesson[i].append([])

    row = 0
    column = 0
    nule = 0

    for i in root[-1][0]:
        if i.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Row":
            for z in range(len(i)):
                if i[z].attrib['{urn:schemas-microsoft-com:office:spreadsheet}StyleID'] != 's62':
                    for q in i[z]:
                        lesson[row][z].append(q.text)
                        nule = 0
                    else:
                        nule += 1
                        if nule > 1:
                            lesson[row][z].append(" ")
                    if z == info[0]-1: column += 1
                    if column == info[2] and row < info[1]-1:
                        column = 0
                        row += 1
    return lesson[x][y]