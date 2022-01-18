from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')  # Загрузить таблицу Excel из файла в переменную wb
sheet = wb['Data']  # Загрузить лист с именем "Data" в переменную sheet

def getvalue(x):
    return x.value

ListX = list(map(getvalue, sheet['A'][1:])) # Преобразовать содержимое колонки A в список, содержащий только значения
ListY1 = list(map(getvalue, sheet['C'][1:])) # Преобразовать содержимое колонки C в список, содержащий только значения
ListY2 = list(map(getvalue, sheet['D'][1:])) # Преобразовать содержимое колонки D в список, содержащий только значения


pyplot.plot(ListX, ListY1, label="График1") # Построить график по точкам, в ListX по оси X, ListY1 по оси Y
pyplot.plot(ListX, ListY2, label="График2") # Построить график по точкам, в ListX по оси X, ListY2 по оси Y
pyplot.show() # показать график
