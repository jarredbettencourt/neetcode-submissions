class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dyn_array = [-1] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.dyn_array[i]

    def set(self, i: int, n: int) -> None:
        self.dyn_array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == len(self.dyn_array):
            self.resize()
        self.dyn_array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        val = self.dyn_array[self.length - 1]
        self.dyn_array[self.length - 1] = -1
        self.length -= 1
        return val

    def resize(self) -> None:
        new_array = [-1] * (2 * len(self.dyn_array))
        for i in range(self.length):
            new_array[i] = self.dyn_array[i]
        self.dyn_array = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return len(self.dyn_array)