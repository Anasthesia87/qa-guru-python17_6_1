from xlrd import open_workbook
from script_xlsx import sheet

# открывает Excel-файл, позволяя работать с ним
workbook = open_workbook(r"tmp\file_example_XLS_10.xls")
# показывает общее количество листов в рабочей книге
print(workbook.nsheets)
# выводит имена всех листов в рабочей книге.
print(workbook.sheet_names())
# выбирает первый лист в рабочей книге
sheet = workbook.sheet_by_index(0)
# сообщает о количестве строк в выбранном листе.
print(sheet.nrows)
# Выводит количество столбцов в выбранном листе
print(sheet.ncols)
# Возвращает значение ячейки, расположенной на пересечении девятого ряда и третьего столбца
print(sheet.cell_value(rowx=9, colx=3))

#Позволяет эффективно обрабатывать данные Excel-файла, проходя по всем строкам листа и выводя их
for rx in range(sheet.nrows):
    print(sheet.row(rx))