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
    

def heapify(arr, i, n):
    largest = i # index
    left = 2 * i + 1 # index
    right = 2 * i + 2 # index
    # n = length of arr

    if right < n and arr[right] > arr[largest]: largest = right # index richtig und links ist größer als largest
    if left < n and arr[left] > arr[largest]: largest = left # if left = n ! error

    if largest != i:
        arr[i], arr[largest] =  arr[largest], arr[i] # largest bleibt index von links oder rechts
        heapify(arr, largest, n) # recursiv
    return

def heapify_efficient(arr, i, n): # T bleibt gleich, S: O(1) gleich viele pointer in der iteration
    largest = i # index
    while True:
        prev_Largest = largest
        left = 2 * largest + 1 # index
        right = 2 * largest + 2 # index
        # n = length of arr

        if right < n and arr[right] > arr[largest]: largest = right # index richtig und links ist größer als largest
        if left < n and arr[left] > arr[largest]: largest = left # if left = n ! error

        if largest != prev_Largest: #wen schon hat sich nichts verändert
            arr[prev_Largest], arr[largest] =  arr[largest], arr[prev_Largest] # largest bleibt index von links oder rechts
        else: break

def sort(arr):
    # heap bauen T: O(n), S: O(log(n/2)) immer nur die elemente ab vorletzter ebene zirka im call stack | mit efficient T: O(n), S: O(1)
    n = len(arr)
    cur = (n - 2) // 2 # index
    while cur >= 0: # index 0
        heapify_efficient(arr, cur, n)
        cur -= 1
    # heap sortieren T: O(n * log(n)) maximal log(n) mal rekursiv aufgerufen / durchgänge S: O(log(n)) | mit efficient T: O(n * log(n)), S: O(1)
    for i in range(n-1, 0, -1): # letzter wert ist schon sortiert
        arr[0], arr[i] = arr[i], arr[0] # i tauscht mit der root
        heapify_efficient(arr, 0, i) # array ist nurmehr i groß und es ist immer 0 dran

arr = [9, 7, 4, 5, 2, 1, 2, 1, 21, 2, 32, 3, 2, 1]
sort(arr)
print(arr)
# wenn man wiederhohlt das größte element runterhohlt und die root ist ja immer das größte und dann die neue root macht was wieder das größte element ist hat man am schluss ein sortiertes array
nums = [3,2,1,5,6,4]
sort(nums)
print(nums[2-1])