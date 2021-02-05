import random

def generation_matrix(a,b):   #  Генерируем матрицу
    M=[[random.randint(-10,10) for i in range(1,a)] for j in range(1,b)]
    return (M)


def print_matrix(matrix):   #  Печать матрицы с форматом строки
    for i in range(0,4):
        row = " "
        for j in range(0,4):
            cell = matrix[i][j]
            cell_formated  = f"{cell:>4}"
            row = row + cell_formated
        print(row)

def Null_rows_and_Null_columns(matrix,m,n):  #   зануляем строку и столбец
    print('------------------------------')
    print(f" Зануляем строку {m} и столбец  {n}")
    for i in range(0,4):
        M[m][i] = 0
        M[i][n] = 0
    print(" Преобразованная матрица :")


def martix_control_of_Null_rows_and_columns(matrix):
    s=0 #   Если s не равно нулю  то имеется нулевая ячейка
    for i in range(0,4):
        for j in range(0,4):
            if M[i][j] == 0 :
                m = i # Запомнили строку m-строка
                n = j  # Запомнили столбец  n- столбец
                s=+1
                print (f"строка {i} столбец {j}  это нулевая ячейка ")
    if s==0:
        print(" В Матрице нет нулевых ячеек")
    else:
        Null_rows_and_Null_columns(M,m,n)


M=generation_matrix(5,5)
print(" Исходная матрица ")
print_matrix(M)
print("==================================")
print( "Проверка матрицы на наличие нулевых ячеек")
martix_control_of_Null_rows_and_columns(M)
print_matrix(M)
print("==================================")
print(" FINISH  PROGRAMM ")



#        ВСЁ РАБОТАЕТ )))
