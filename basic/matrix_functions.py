def print_matrix(matrix, rows, columns, title="Matrix"):
    print(title)
    for i in range(0, columns):
        row = ''
        for j in range(0, rows):
            cell = matrix[i][j]
            cell_formated = f'{cell: >3},'
            row = row + cell_formated
        print(row)


def multiply_matrix_by_number(matrix, rows, columns, number):
    for i in range(0, columns):
        for j in range(0, rows):
            cell = matrix[i][j]
            cell = cell * number
            matrix[i][j] = cell


def generate_matrix(rows, columns):
    M = [[i*j for j in range(1, rows+1)]
         for i in range(1, columns+1)]

    return M


def null_rows_or_columns(matrix, rows, columns, null_rows=None, null_columns=None):
    null_rows = null_rows or []
    null_columns = null_columns or []

    for i in range(0, columns):
        for j in range(0, rows):
            if i in null_columns or j in null_rows:
                matrix[i][j] = 0


def main():
    rows, columns, n = 4, 4, 3
    M = generate_matrix(rows, columns)
    print(M)
    print_matrix(M, rows=rows, columns=columns)
    multiply_matrix_by_number(M, rows=rows, columns=columns, number=n)
    print_matrix(matrix=M, rows=rows, columns=columns, title=f"Matrix multiplied by {n}")
    null_rows_or_columns(matrix=M, rows=rows, columns=[1], null_columns=[1])
    print_matrix(matrix=M, rows=rows, columns=columns, title="Matrix after null")


main()
