class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        result = []
        for num in nums2:
            if freq[num] > 0:
                for _ in range(freq[num]):
                    result.append(num)
        return result


class ColoredPoint:
    def __init__(self, x: int, y: int, color: tuple[int] = (0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y, self.color}"

    def __str__(self):
        return f"{self.x, self.y}"

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(self.x * (-1), self.y * (-1), self.color)

    def __invert__(self):
        reverse_color = [255 - i for i in self.color]
        return ColoredPoint(self.y, self.x, tuple(reverse_color))


class Matrix:
    def __init__(self, rows, cols, value=0):
        self._rows = rows
        self._cols = cols
        self.value = value
        self.matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f'{self.__class__.__name__}{self._rows, self._cols}'

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += ' '.join(map(str, row)) + '\n'
        return f'{result}'

    def __pos__(self):
        new_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, self.get_value(i, j))
        return new_matrix

    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, -self.get_value(i, j))
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(j, i, self.get_value(i, j))
        return new_matrix

    def __round__(self, n=None):
        new_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.get_value(i, j)
                new_matrix.set_value(i, j, round(value, n) if n is not None else round(value))
        return new_matrix
