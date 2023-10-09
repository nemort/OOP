class Array3D:
    def __init__(self, dim1, dim2, dim3):
        self.dimensions = {
            "first": dim1,
            "second": dim2,
            "third": dim3
        }
        self.array = [None] * (dim1 * dim2 * dim3)

    def get_pointer(self, i, j, k):
        return i * self.dimensions["second"] * self.dimensions["third"] + j * self.dimensions["third"] + k

    def is_index(self, key):
        return isinstance(key, int) and key >= 0

    def get_value(self, i=None, j=None, k=None):
        if not self.is_index(i):
            i_range = range(self.dimensions["first"])
        else:
            i_range = range(i, i + 1)
        if not self.is_index(j):
            j_range = range(self.dimensions["second"])
        else:
            j_range = range(j, j + 1)
        if not self.is_index(k):
            k_range = range(self.dimensions["third"])
        else:
            k_range = range(k, k + 1)

        result = []
        for i in i_range:
            for j in j_range:
                sub_array = []
                for k in k_range:
                    sub_array.append(self.array[self.get_pointer(i, j, k)])
                if len(sub_array) == 1:
                    result.append(sub_array[0])
                else:
                    result.append(sub_array)
        if len(result) == 1:
            return result[0]
        else:
            return result

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
        if not isinstance(two_dim_array, list):
            raise ValueError("Cannot set non-array value as second dimension of Array3D")
        if len(two_dim_array) != self.dimensions["second"]:
            raise ValueError("Array size for setting second dimension is not equal to second dimension size")
        for j in range(self.dimensions["second"]):
            value = two_dim_array[j]
            if not isinstance(value, list):
                raise ValueError("Using one-dimensional array in setting values as a two-dimensional array")
            if len(value) != self.dimensions["third"]:
                raise ValueError("Array size for setting third dimension is not equal to third dimension size")
            self.set_values_01(value, i, j)

    def set_values_1(self, two_dim_array, j):
        if not isinstance(two_dim_array, list):
            raise ValueError("Cannot set non-array value as first dimension of Array3D")
        if len(two_dim_array) != self.dimensions["first"]:
            raise ValueError("Array size for setting first dimension is not equal to first dimension size")
        for i in range(self.dimensions["first"]):
            value = two_dim_array[i]
            if not isinstance(value, list):
                raise ValueError("Using one-dimensional array in setting values as a two-dimensional array")
            if len(value) != self.dimensions["third"]:
                raise ValueError("Array size for setting third dimension is not equal to third dimension size")
            self.set_values_01(value, i, j)

    def set_values_2(self, two_dim_array, k):
        if not isinstance(two_dim_array, list):
            raise ValueError("Cannot set non-array value as first dimension of Array3D")
        if len(two_dim_array) != self.dimensions["first"]:
            raise ValueError("Array size for setting first dimension is not equal to first dimension size")
        for i in range(self.dimensions["first"]):
            value = two_dim_array[i]
            if not isinstance(value, list):
                raise ValueError("Using one-dimensional array in setting values as a two-dimensional array")
            if len(value) != self.dimensions["second"]:
                raise ValueError("Array size for setting second dimension is not equal to second dimension size")
            self.set_values_02(value, i, k)

    def get_size(self):
        return self.dimensions

    def create_fill(self, value):
        for i in range(len(self.array)):
            self.array[i] = value


# Пример использования класса Array3D
array = Array3D(2, 3, 4)
print("Empty array demonstration:", array.get(), "\n")

# Заполнение через create_fill()
array.create_fill(10)
print("Create fill demonstration:", array.get(), "\n")

# Заполним массив значениями суммы индексов i+j+k
sizes = array.get_size()
for i in range(sizes["first"]):
    for j in range(sizes["second"]):
        for k in range(sizes["third"]):
            array.set_value(i + j + k, i, j, k)
print("i+j+k demonstration:", array.get(), "\n")

try:
    array.set_values_0([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], 0)
    array.set_values_1([[9, 9, 9, 9], [8, 8, 8, 8]], 2)
    array.set_values_2([[None, None, None], [None, None, None]], 3)
    array.set_values_01([5, 5, 5, 5], 1, 0)
    array.set_values_12([12, 12], 2, 0)
    array.set_values_02([99, 99, 99], 0, 1)
except ValueError as error:
    print(error)

print("set_values() demonstration:", array.get())
