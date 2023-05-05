class DynamicArray:

    def __init__(self):
        self.static_arr_len = 1
        self.curr_index = 0
        self.static_array = [None]*self.static_arr_len

    def add(self, e):
        if self.curr_index >= self.static_arr_len:
            self.static_arr_len += 1
            new_static_array = [None]*self.static_arr_len
            self.curr_index = len(self.static_array)
            for i in range(0,self.curr_index):
                new_static_array[i] = self.static_array[i]
            self.static_array = new_static_array
            new_static_array[self.curr_index] = e
        self.static_array[self.curr_index] = e
        self.curr_index += 1
        return self.static_array

    def len(self):
        return len(self.static_array)

    def print(self):
        print(self.static_array)
        print(f"current index: {self.len()}")

    def remove_at(self, index):
        temp_arr = [None] * (self.len() - 1)
        j=0
        for i in range(0, self.len()):
            if i == index:
                j -= 1
            temp_arr[j] = self.static_array[i]
            j += 1
        self.static_array = temp_arr
        return self.static_array

    def remove(self, e):
        for i in range(0, self.len()):
            if self.static_array[i] == e:
                self.remove_at(i)
                break
        return self.static_array

    def reverse(self):
        # using temp array
        # temp = [None]*self.len()
        # j = 0
        # for i in range(self.len()-1, -1, -1):
        #     temp[j] = self.static_array[i]
        #     j += 1
        # self.static_array = temp

        # without using temp array
        n = self.len()
        for i in range(0, int(n/2)):
            temp = self.static_array[i]
            self.static_array[i] = self.static_array[n-i-1]
            self.static_array[n - i - 1] = temp
        return self.static_array


if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(0,30):
        arr.add(i)
    # arr.print()
    arr.remove_at(0)
    arr.remove_at(10)
    # arr.print()
    arr.remove(15)
    arr.remove(19)
    arr.reverse()
    arr.print()