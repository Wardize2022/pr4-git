EPS = 1e-9
MAX_SIZE = 25


def input_size(prompt):
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue
        if not 1 <= value <= MAX_SIZE:
            print(f"Ошибка: размер должен быть от 1 до {MAX_SIZE}.")
            continue
        return value


def input_matrix(n, m):
    matrix = []
    for i in range(n):
        while True:
            parts = input(f"Строка {i + 1} ({m} чисел через пробел): ").replace(",", ".").split()
            if len(parts) != m:
                print(f"Ошибка: в строке должно быть ровно {m} чисел.")
                continue
            try:
                row = [float(x) for x in parts]
            except ValueError:
                print("Ошибка: элементы матрицы должны быть числами.")
                continue
            matrix.append(row)
            break
    return matrix


def is_equal(a, b):
    return abs(a - b) < EPS


def zero_columns(matrix):
    result = []
    for k in range(len(matrix[0])):
        all_zero = True
        for row in matrix:
            if not is_equal(row[k], 0):
                all_zero = False
                break
        result.append(all_zero)
    return result


def descending_rows(matrix):
    result = []
    for row in matrix:
        ordered = True
        for j in range(len(row) - 1):
            if row[j] <= row[j + 1]:
                ordered = False
                break
        result.append(ordered)
    return result


def symmetric_rows(matrix):
    result = []
    for row in matrix:
        symmetric = True
        for j in range(len(row) // 2):
            if not is_equal(row[j], row[-1 - j]):
                symmetric = False
                break
        result.append(symmetric)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{x:8.2f}" for x in row))


def print_vector(title, vector):
    print(title)
    print("  [" + ", ".join(str(x) for x in vector) + "]")


def main():
    print("Построение логических векторов по вещественной матрице")
    n = input_size("Введите количество строк n: ")
    m = input_size("Введите количество столбцов m: ")
    matrix = input_matrix(n, m)

    print("\nИсходная матрица:")
    print_matrix(matrix)
    print()
    print_vector("1) Все элементы k-го столбца нулевые:", zero_columns(matrix))
    print_vector("2) Элементы k-й строки упорядочены по убыванию:", descending_rows(matrix))
    print_vector("3) k-я строка симметрична:", symmetric_rows(matrix))


if __name__ == "__main__":
    main()
