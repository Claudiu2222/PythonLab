### EX 1 ###


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item_to_push):
        self.items.append(item_to_push)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def test_stack():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    print(stack.peek())  # 4
    print(stack.pop())  # 4
    print(stack.pop())  # 3
    print(stack.pop())  # None
    print(stack.peek())  # None


test_stack()

### EX 2 ###


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item_to_push):
        self.items.append(item_to_push)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


def test_queue():
    queue = Queue()
    queue.push(3)
    queue.push(4)
    print(queue.peek())  # 3
    print(queue.pop())  # 3
    print(queue.pop())  # 4
    print(queue.pop())  # None
    print(queue.peek())  # None


test_queue()


### EX 3 ###


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for i in range(m)] for j in range(n)]

    def set_val(self, i, j, val):
        if i < self.n and i >= 0 and j < self.m and j >= 0:
            self.matrix[i][j] = val
        else:
            print("Index out of bounds")

    def get_val(self, i, j):
        if i < self.n and i >= 0 and j < self.m and j >= 0:
            return self.matrix[i][j]
        print("Index out of bounds")
        return None

    def transpose(self):
        self.matrix = [
            [self.matrix[j][i] for j in range(self.n)] for i in range(self.m)
        ]
        self.m, self.n = self.n, self.m

    def multiply(
        self, second_matrix
    ):  # Matrixes can be multiplied <=> nr columns first matrix = nr rows second matrix
        if self.m != second_matrix.n:
            print("Matrixes can't be multiplied")
            return None
        result_matrix = Matrix(self.n, second_matrix.m)
        for i in range(self.n):
            for j in range(second_matrix.m):
                value_to_add = 0
                for k in range(self.m):
                    value_to_add += self.get_val(i, k) * second_matrix.get_val(k, j)
                result_matrix.set_val(i, j, value_to_add)
        return result_matrix

    def apply_function(self, function):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = function(self.matrix[i][j])

    def print_matrix(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.matrix[i][j], end=" ")
            print()


def test_matrix():
    matrix_1 = Matrix(3, 2)
    for i in range(3):
        for j in range(2):
            matrix_1.set_val(i, j, i * 2 + j)
    print("Matrix 1:")
    matrix_1.print_matrix()
    matrix_1.transpose()
    print("Transposed matrix 1:")
    matrix_1.print_matrix()
    matrix_2 = Matrix(3, 2)
    for i in range(3):
        for j in range(2):
            matrix_2.set_val(i, j, i * 2 + j)
    print("Matrix 2:")
    matrix_2.print_matrix()
    matrix_1.apply_function(lambda x: x + 1)
    print("Matrix 1 after applying function:")
    matrix_1.print_matrix()
    print("Matrix 1 * Matrix 2:")
    matrix_3 = matrix_1.multiply(matrix_2)
    matrix_3.print_matrix()


test_matrix()
