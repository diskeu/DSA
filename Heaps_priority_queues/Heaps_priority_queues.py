# Heaps Priority Queues

# Heap -> binärbaum mit diesen eigenschaften
# -> Max Heap -> jede node ist größer oder gleich wie seine childs
# -> Min Heap -> jede node ist kleiner oder gleich wie seine childs
# der baum ist ein complete tree und alle ebenen sind voll bis auf der letzten von links nach rechts aufgefüllt
# Höhe eines heaps log(n) / space complexity O(log(n)) -> höhe des baums / wie oft muss ich n durch 2 teilen bis ich 1 habe -> höhe des baumes

# Heap und Priority Queue ist die gleiche Datenstruktur

#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 8   -1
#   / \ /
#  7  6 9
# als array dargestellt (geht nur wenn leere werte mit None markiert werden und die fehlenden werte von links nach rechts gehen)
# -> [1, 2, 3, 4, 5, 8, -1, 7, 6, 9]
#     0  1  2  3  4  5   6  7  8  9
# Für jeden wert gilt -> L = 2 * i + 1 R = 2 * i + 2

# um zb einen Tree in einen min Heap umzuwandeln -> min heapify
# min Heap
#         1
#       /   \
#      3     2
#     / \   / \
#    7   6 4   5
# jede node ist kleiner als sein L und sein R
# bei Heap pop nimmt man den obersten wert des heaps und löscht ihn der heap muss sich von selbst reperieren das er wieder ein min heap ist
#                          5                            2
#       /   \            /   \                         / \
#      3     2      ->  3     2                       3   4
#     / \   / \        / \   / \                     / \   \
#    7   6 4   5      7   6 4                       7   6   5
# 1). bei heap.pop() bei einem min heap löscht man die wurzel da sie das kleinste element ist
# 2). dann wird letzte element in der letzten ebene nach oben geschoben
# 3). Heapify -> (nach unten korrigieren) -> man vergleicht neue wurzel 5 mit kindern 2 und 3 -> kleinster wert ist 2 also tausch mit 5 und 2
# -> dann prüft man wieder 5 mit seinen kindern und tauscht es
# da man bei pop immer einen weg den tree runter geht und es immer ein complete tree ist, ist time complexity O(log(n))
#    -> Höhe (wie oft n durch 2 um zu 1 zu gelangen)
# Heap pop -> extract min

# Heap insert / push
# man nimmt eine zahl und fügt sie zur letzten ebene an letzter position -> dadurch können die heap eigenschaften verletzt werden
# wenn die zahl kleiner ist als parent -> dann tauscht man zahl mit parent
# darum O(log(n) da man maximal die höhe des baums durchgeht

# Heapify up -> bei insert man vergleicht von unten nach oben
# Heapify down -> bei pop man vergleicht nach unten

# Ein Heap wird normalerweise als array implementiert darum kann man sich parents berechnen und braucht keine pointer

# Heap peek
# erstes element peeken -> arr[0] -> O(1)

# Heap = priority queue -> die nodes mit höherer priorität werden als erstes behandelt bei min heap sind es die kleinsten werte bei max heap die größten
# parrallelen zu queues die werte mit höherer priorität (die zuerst da waren) werden als erstes behandelt -> heap pop insert und peek so ähnlich wie bei queues

# Heap sort -> Sortieralgorythmus
# man popt wiederhohlt das erste element vom heap es wird ans ende des arrays geschoben und ist dort fixiert und kein teil mehr vom heap dann macht man heapify
# man muss das n mal machen bis das heap leer ist (n-1 da letztes element automatisch richtig liegt) die zeit pro pop beträgt O(log(n))
# man könnte annehmen das Time complexity O(n^2) ist da man für jedes n array einmal durchgehen muss, aber da man nur log(n) gehen muss
# ist time complexity O(n * O(log(n)) was ihn zu einem der schnellsten sortieralgorythmen macht
# auch wenn n immer kleiner wird schreibst man O(n * log(n))
# 	•	Space Complexity = Gesamtspeicher, den eine Datenstruktur oder ein Algorithmus benötigt, in Abhängigkeit von der Eingabegröße
# space complexity beis heap sort ist
# 	•	Heap selbst: wir verwenden das gleiche Array, kein zusätzliches Array → kein O(n) extra
# 	•	Temporäre Variablen (z. B. für Tauschen, i, end) → O(1)
# 	•	Heapify-Up / Heapify-Down läuft iterativ oder rekursiv
# 	•	Iterativ: O(1)
# 	•	Rekursiv: O(log n) wegen Rekursionsstack
# Gesamt: O(1) extra Speicher (iterativ) oder O(log n) bei rekursiver Heapify) -> wenn man neues array macht mit den werten O(n)

# Heapify -> bei heapify down oder heapify up O(log(n)) -> höhe
# in einem build heap -> unsortiertes array entspricht nicht min / max heap eigenschaften macht man um es den heap eigenschaften getreu zu machen
# bei jeder nicht blatt node heapify down -> vorgehensweise -> letzten nicht blatt node finden und dann von der aus rückwerts immer heapify down
# Build-Heap -> O(n) weil viele Heapify-Downs nur kurz sind
# Heap Sort -> O(n log n) weil wir n-1 Mal Root entfernen und jede Heapify-Down jetzt fast log n Schritte haben
# space complexity bei heapify down / up ist O(1) man erstellt keinen neuen array und man arbeitet nur mit indexen aktuelle nodes -> es werden keine zusätzlichen struktureen / arrays angelegt, bei reukrsiven heapify ist es O(log(n)) wegen call stack -> worst case tiefe liegt auf dem call stack

# Heaps sind sehr nützlich wenn man eine sequenz
# A: 1
# B: 2
# C: 3
# D: 4
# E: 5
# F: 6
#           (1, A)
#          /       \
#        (2, B)    (3, C)
#        /    \      /
#     (4, D) (5, E) (5, F) -> man speichert werte in diesem fall auf min heap die eine priorität haben x[0] und daten x[1] in einem heap prinzip
# effizient wenn man daten hat mit priorität -> wie z.B. bei einer Drucker queue und man speichert immer ihre priorität mit den druckdaten z.B.
# man kann dan daten runternehmen in O(log(n)) oder sortieren in O(n * log(n))

# Um Parents von einer Node im Heap zu bekommen nimmt man formel L = 2 * Eltern_Node_Index + 1/2 -> umgeformt ist es dann Eltern_Node_Index = (I-1) // 2

# Um die letzten index mit kinder zu finden, braucht man größten index i für den das gilt
# Ein Knoten hat ein linkes Kind, wenn 2*i + 1 < n - 1
# wenn der Knoten kein Linkes kind hat hat er sicherlich kein rechtes -> Links vor Rechts
# damit linkses kind existiert gilt -> 2*i + 1 ≤ n − 1
# dann stellt man um auf 2*i ≤ n − 2 -> i ≤ (n − 2) / 2 und weil index ganze zahl sein muss i ≤ (n − 2) // 2
# wenn index <= ist dann hat es ein kind wenn index genau i = (n − 2) // 2 ist hat es kein kind

# wenn man bei heap sort wiederhohlt das größte element runternimmt und weiter sortiert nach dem größten dann sortiert das den heap

# !!! warum nicht queue statt heap -> Jedes Element hat eine eigene Priorität → unabhängig von der Ankunftszeit, bei queue ist das nicht so, priorität ist abhängig von ankunftszeit

def min_Heapify(node_Index: int, arr: list) -> list:
        cur = node_Index # Index
        new_arr = arr
        while True:
            L, R = None, None
            if cur * 2 + 1 <= len(new_arr) - 1: L = cur * 2 + 1 # wenn Left kleiner ist als länge arr definiere L
            if cur * 2 + 2 <= len(new_arr) - 1: R = cur * 2 + 2 # wenn Right kleiner ist als länge arr definiere R
            if L == None and R == None: return new_arr # kein heapify mehr möglich | 0 zählt als not

            if L == None and R != None: smallest_Num = R # kein Links aber Rechts / wenn zahl 0 ist dann == not
            elif R == None and L != None: smallest_Num = L # kein Rechts aber Links
            else:
                if new_arr[L] > new_arr[R]: smallest_Num = R 
                else: smallest_Num = L
            if new_arr[cur] > new_arr[smallest_Num]:
                # -> swap values
                new_arr[cur], new_arr[smallest_Num] = new_arr[smallest_Num], new_arr[cur]
            else: return new_arr # kein swap mehr nötig
            cur = smallest_Num
print(min_Heapify(0, [89, 3, 12, 9, 8, 4, 3]))

def max_Heapify(node_Index: int, arr: list) -> list:
    cur = node_Index

    while True:
        L, R = None, None
        if cur * 2 + 1 <= len(arr) - 1: L = cur * 2 + 1 # wenn Left kleiner ist als länge arr definiere L
        if cur * 2 + 2 <= len(arr) - 1: R = cur * 2 + 2 # wenn Right kleiner ist als länge arr definiere R

        if L == None and R == None: return arr
        if L == None and R != None: maxim = R
        elif L != None and R == None: maxim = L
        else:
            if arr[R] > arr[L]: maxim = R
            else: maxim = L
        if arr[cur] < arr[maxim]:
            arr[cur], arr[maxim] = arr[maxim], arr[cur]
        else: return arr

        cur = maxim
print(max_Heapify(0, [-2, 3, 12, 9, 8, 4, 3]))

def heap_pop(arr: list, min_Heap: bool = False) -> tuple:
    arr[0], arr[-1] = arr[-1], arr[0]

    val = arr.pop()
    if min_Heap: arr = min_Heapify(0, arr)
    if not min_Heap: arr = max_Heapify(0, arr)
    return val, arr
print(heap_pop([12, 7, 8, 3, 2, -2, 4], min_Heap=False))
print(heap_pop([-2, 2, 4, 3, 7, 8, 12], min_Heap=True))

def min_Heapify_Up(node_Index: int, arr: list) -> list:
    cur = node_Index # index
    while True:
        if (cur - 1) // 2 >= 0: parent_Index = (cur - 1) // 2
        else: return arr

        if arr[parent_Index] > arr[cur]:
            arr[parent_Index], arr[cur] = arr[cur], arr[parent_Index]
            cur = parent_Index
        else: return arr

def max_Heapify_Up(node_Index: int, arr: list) -> list:
    cur = node_Index # index
    while True:
        if (cur - 1) // 2 >= 0: parent_Index = (cur - 1) // 2
        else: return arr

        if arr[parent_Index] < arr[cur]:
            arr[parent_Index], arr[cur] = arr[cur], arr[parent_Index]
            cur = parent_Index
        else: return arr

def heap_push(arr: list, val: int, min_Heap: bool = False) -> list:
    arr.append(val)

    if min_Heap: arr = min_Heapify_Up(len(arr)-1, arr)
    if not min_Heap: arr = max_Heapify_Up(len(arr)-1, arr)

    return arr
print(heap_push([-2, 2, 4, 3, 7, 8, 12], 3, min_Heap=True))
print(heap_push([20, 15, 18, 8, 10, 17, 5], 14, min_Heap=False))

def heap_peek(arr: list) -> any:
    return arr[0]
print(heap_peek([20, 15, 18, 8, 10, 17, 5])) # O(1)

def heap_Sort(arr: list, min_Heap: bool = False) -> list:
    # end = len(arr) # bis zu end darum kein end
    # if min_Heap:
    #     while end > 0:
    #         cur, _ = heap_pop(arr, min_Heap=True) # heap pop und heapify
    #     for i in range(0, n):
    #         new_List[i] = cur
    #     return new_List
    ...
print(heap_Sort([-2, 2, 4, 3, 7, 8, 12], min_Heap=True)) # Time: O(n * log(n)), Space: O(n) es ist möglich space O(1) zu machen

def build_Heap(arr: list, min_Heap: bool = False) -> list: # for i = letzter Elternknoten bis 0: heapify-down(i), Space: O(1)
    cur = (len(arr) - 2) // 2 # current index
    if min_Heap:
        while cur >= 0:
            arr = min_Heapify(cur, arr)
            cur -= 1
        return arr
    while cur:
        arr = max_Heapify(cur, arr)
        cur -= 1
    return arr
print(build_Heap([12, 7, 8, 3, 4, 2, -2], min_Heap=True))


import heapq
arr = [-2, 3, 4, 12, 3, 6, 23, -3, 4]
print("=========================================")
# Build min Heap (Heapify) Time: O(n), Space O(1)
heapq.heapify(arr) # / heapq.heapify_max(arr)
print(arr) # arr = heap

# Pop smallest element Time: O(log(n)), Space: O(1)
min = heapq.heappop(arr)
print(min, arr)

# Heap push Time: O(log(n)), Space: O(1)
heapq.heappush(arr, 2)
print(arr)

# Heap push pop, Time: O(log(n)), Space: O(1)
heapq.heappushpop(arr, 21)
print(arr)

# Build Heap, Time: O(n * log(n)), Space: O(n)
nums = [1, 3, 4, 2, 5, 2, 4, 1, 21]
heap = []
for num in nums: # inefizienter als heap build O(n)
    heapq.heappush(heap, num)
    print(heap)

# Tuples von items auf den heap
d = [1, 2, 2, 3, 3, 4, 2, 1, 2, 1, 3, 3]
from collections import Counter
counter = Counter(d)
print(counter) # von 2 x items, von 1 x items ... sortiert nach vorkommenheit

# wenn man tuple pusht dann wird es nach dem ersten wert im tuple gepusht
heap = []
for k, v in counter.items():
    heapq.heappush_max(heap, (v, k)) # items die am öftesten vorkommen haben höhere priorität
print(heap)



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

# heap = min_Heap([1, 2, 3, 4, -2, 3, 2])
# heap.heap_Build()
# print(heap)
# heap.push(1)
# print(heap)
# print(heap.peek())
# heap.pop_Top()
# print(heap)
# print(heap.sort())