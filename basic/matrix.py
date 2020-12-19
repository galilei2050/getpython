
class Matrix(object):

    def __init__(self, data=None):
        data = data if data else []
        self._data = data
        self._columns = len(data)
        self._rows = len(data[0]) if data else 0

    def __str__(self):
        rows = []
        for i in range(0, self._columns):
            row = ''
            for j in range(0, self._rows):
                cell = self._data[i][j]
                cell_formated = f'{cell: >3},'
                row = row + cell_formated
            rows.append(row)
        return '\n'.join(rows)

    def __lt__(self, other):
        return self._rows*self._columns < other._rows * other._columns

    def __eq__(self, other):
        return self._data == other._data

    def print(self, title="Matrix"):
        print(title)
        print(self)

    def multiply_by_number(self, number):
        for i in range(0, self._columns):
            for j in range(0, self._rows):
                self._data[i][j] *= number


def main():
    m1 = Matrix(data=[[1]])
    m2 = Matrix(data=[[1, 2], [2, 1]])
    if m1 == m1:
        print("matrix are equeal")
    biggest_matrix = m2 if m1 < m2 else m1
    biggest_matrix.print()


if __name__ == '__main__':
    main()
