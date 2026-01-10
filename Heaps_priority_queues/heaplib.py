class min_Heap():
    def __init__(self, arr: list):
        self.arr = arr

    def __str__(self):
        return str(self.arr)

    def heapify(self, node_Index: int) -> None:
        cur = node_Index # Index
        while True:
            L, R = None, None
            if cur * 2 + 1 <= len(self.arr) - 1: L = cur * 2 + 1 # wenn Left kleiner ist als länge arr definiere L
            if cur * 2 + 2 <= len(self.arr) - 1: R = cur * 2 + 2 # wenn Right kleiner ist als länge arr definiere R
            if L == None and R == None: return # kein heapify mehr möglich | 0 zählt als not

            if L == None and R != None: smallest_Num = R # kein Links aber Rechts / wenn zahl 0 ist dann == not
            elif R == None and L != None: smallest_Num = L # kein Rechts aber Links
            else:
                if self.arr[L] > self.arr[R]: smallest_Num = R 
                else: smallest_Num = L
            if self.arr[cur] > self.arr[smallest_Num]:
                # -> swap values
                self.arr[cur], self.arr[smallest_Num] = self.arr[smallest_Num], self.arr[cur]
            else: return # kein swap mehr nötig
            cur = smallest_Num

    def push(self, val: int) -> list:
        self.arr.append(val)
        self.heapify_Up(len(self.arr)-1)
    
    def heapify_Up(self, node_Index: int) -> list:
        cur = node_Index # index
        while True:
            if (cur - 1) // 2 >= 0: parent_Index = (cur - 1) // 2
            else: return

            if self.arr[parent_Index] > self.arr[cur]:
                self.arr[parent_Index], self.arr[cur] = self.arr[cur], self.arr[parent_Index]
                cur = parent_Index
            else: return

    def pop_Top(self) -> int:
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]

        val = self.arr.pop()
        self.heapify(0) # -> root
        return val
    
    def peek(self) -> int:
        return self.arr[0]
    
    def heap_Build(self):
        cur = (len(self.arr) - 2) // 2 # current index

        while cur >= 0:
            self.heapify(cur)
            cur -= 1

    def sort(self) -> list:
        new = [0] * len(self.arr)
        for i in range(0, len(self.arr)):
            val = self.pop_Top()
            new[i] = val
        return new