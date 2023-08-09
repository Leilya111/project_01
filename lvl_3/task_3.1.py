# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)class Matrix:


class Matrix:
    def __init__(self, rows, columns, value):
        self.columns = columns
        self.rows = rows
        self.value = value
        self.field = [[value for i in range(columns)] for i in range(rows)]
        print(* self.field, sep = '\n')
       
    def change(self, row, column,  val):
        self.field[row][column] = val
        print(* self.field, sep = '\n')

    def count(self):
        print(f'Число столбцов: {self.columns}, число строк: {self.rows}')

table_columns = int(input('Введите число столбцов  ='))
table_rows = int(input('Введите число строк  ='))
table_values = int(input('Введите значение матрицы  ='))

my_table = Matrix(table_rows, table_columns, table_values)

change_columns = int(input('Введите номер столбца  ='))
change_rows = int(input('Введите номер строки  ='))
change_values = int(input('Введите значение ячейки  ='))

my_table.change(change_rows-1, change_columns-1, change_values)

my_table.count()

