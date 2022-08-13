class Heap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert(self, item):
        items = self.items

        items.append(item)
        self.size += 1

        index = self.size - 1
        parent = (index - 1) // 2

        while index >= 0 and items[index] > items[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index-1) // 2

    def _swap(self,first, second):
        self.items[first], self.items[second] = self.items[second], self.items[first]

    def print(self):
        for i in range(self.size):
            print(self.items[i], end=" ")
def main():
    heap = Heap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(2)
    heap.insert(4)
    heap.insert(8)
    heap.insert(7)

    heap.print()

if __name__ == "__main__":
    main()
    print("Done")

#         10
#     20      30
#   2    4  8    7