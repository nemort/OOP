class Array3D:
    def __init__(self, first_dim, second_dim, third_dim):
        self.dimensions = {
            "first": first_dim,
            "second": second_dim,
            "third": third_dim
        }
        self.array = [None] * (first_dim * second_dim * third_dim)

    def get_pointer(self, i, j, k):
        return i * self.dimensions["second"] * self.dimensions["third"] + j * self.dimensions["third"] + k

    def get_value(self, i=None, j=None, k=None):
        i_range = range(self.dimensions["first"]) if i is None else range(i, i + 1)
        j_range = range(self.dimensions["second"]) if j is None else range(j, j + 1)
        k_range = range(self.dimensions["third"]) if k is None else range(k, k + 1)

        result = []
        for i in i_range:
            inner_result = []
            for j in j_range:
                sub_array = []
                for k in k_range:
                    value = self.array[self.get_pointer(i, j, k)]
                    sub_array.append(value if value is not None else None)
                inner_result.append(sub_array[0] if len(sub_array) == 1 else sub_array)
            result.append(inner_result[0] if len(inner_result) == 1 else inner_result)
        return result[0] if len(result) == 1 else result

    def set_value(self, value, i, j, k):
        self.array[self.get_pointer(i, j, k)] = value

    def set_values_01(self, array, i, j):
        for k in range(self.dimensions["third"]):
            self.array[self.get_pointer(i, j, k)] = array[k]

    def set_values_02(self, array, i, k):
        for j in range(self.dimensions["second"]):
            self.array[self.get_pointer(i, j, k)] = array[j]

    def set_values_12(self, array, j, k):
        for i in range(self.dimensions["first"]):
            self.array[self.get_pointer(i, j, k)] = array[i]

    def set_values_0(self, two_dim_array, i):
        if len(two_dim_array) != self.dimensions["second"]:
            raise ValueError("Размер массива для задания второй размерности не равен размеру второй размерности")
        for j, sub_array in enumerate(two_dim_array):
            if len(sub_array) != self.dimensions["third"]:
                raise ValueError("Размер массива для задания третьего измерения не равен размеру третьего измерения")
            self.set_values_01(sub_array, i, j)

    def set_values_1(self, two_dim_array, j):
        if len(two_dim_array) != self.dimensions["first"]:
            raise ValueError("Размер массива для установки первой размерности не равен размеру первой размерности")
        for i, sub_array in enumerate(two_dim_array):
            if len(sub_array) != self.dimensions["third"]:
                raise ValueError("Размер массива для задания третьего измерения не равен размеру третьего измерения")
            self.set_values_01(sub_array, i, j)

    def set_values_2(self, two_dim_array, k):
        if len(two_dim_array) != self.dimensions["first"]:
            raise ValueError("Размер массива для установки первой размерности не равен размеру первой размерности")
        for i, sub_array in enumerate(two_dim_array):
            if len(sub_array) != self.dimensions["second"]:
                raise ValueError("Размер массива для задания второй размерности не равен размеру второй размерности")
            self.set_values_02(sub_array, i, k)

    def get_size(self):
        return self.dimensions

    def create_fill(self, value):
        self.array = [value] * len(self.array)

    def get(self):
        return self.array

    def __str__(self):
        result = "[\n"
        for i in range(self.dimensions["first"]):
            result += "  [\n"
            for j in range(self.dimensions["second"]):
                result += "    ["
                for k in range(self.dimensions["third"]):
                    value = self.array[self.get_pointer(i, j, k)]
                    result += " " + str(value) + ","
                result = result.rstrip(",") + " ],\n"
            result = result.rstrip(",\n") + "\n  ],\n"
        result = result.rstrip(",\n") + "\n]"
        return result


# Пример использования класса Array3D
array = Array3D(2, 3, 4)
print("Пустой массив:", array, "\n")

# Заполнение через create_fill()
array.create_fill(10)
print("Создаем заполнение:", array, "\n")

# Заполним массив значениями суммы индексов i+j+k
sizes = array.get_size()
for i in range(sizes["first"]):
    for j in range(sizes["second"]):
        for k in range(sizes["third"]):
            array.set_value(i + j + k, i, j, k)
print("i+j+k:", array, "\n")

try:
    array.set_values_0([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], 0)
    array.set_values_1([[3, 3, 3, 3], [4, 4, 4, 4]], 1)
    array.set_values_2([[None, None, None], [None, None, None]], 2)
    array.set_values_01([5, 5, 5, 5], 1, 0)
    array.set_values_12([6, 6], 2, 0)
    array.set_values_02([7, 7, 7], 0, 1)
except ValueError as error:
    print(error)

print("set_values():", array)
