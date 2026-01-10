# Stacks and Queues

# Stacks
# Gennant Stack weil es eigentlich wie ein Stapel ist, in CS nicht oben und unten sondern links und rechts
# Man kann es als array implementieren, aber man macht sich eigentlich nur Gedanken über das Letzte Element der Liste
# l = [1, 2, 3, 4], in theore: man kann bei einem stack nicht auf die werte 1, 2, 3 zugreifen, wenn schon da z.B. es in Python als
# array implimentiert wird ist es kein stack
# man kann jeden datenTyp in Stack machen
# Operationen:
# append -> man legt etwas auf den Stapel, ganz rechte Seite des Arrays - Append ist *O(1) da es immer auf den letzten Wert appended
# im Worst case muss man aber trodem wenn speicher des dynamic arrays leer ist alle werte in ein neues einfügen
# Stack kann aber auch z.B. eine Linked list sein, bei der appenden O(1) ist, aber nur wenn man den Tail gegeben hat
# pop -> wert ganz oben weggeben, ganz rechte seite des dynamic arrays, ist bei dynamic array immer O(1) da man einfach letzten wert frei machen muss
# bei doubly linked list auch immer O(1) wenn man tail gegeben hat, bei singly linked list wenn man nur tail hat O(n), da man vom prev next nicht setzen kann
# peek -> letztes element ansehen, immer O(1) bei dynamic array, bei linked list auch immer O(1) wenn man tail hat
# Is empty -> auch immer O(1) da man einfach schauen muss ob peek wert hat -> return True if s
# In der Theorie schaut man auf peek(), bei Python-Listen kann man len oder not stack benutzen, weil Python die Länge intern kennt.
# bei Linked list O(1) wenn man tail hat, sonst O(n)
# man kann bei Linked list auch als top element vom stack head nehmen
# Ist LIFO -> Last in first Out

# Queues
# Ist FIFO -> First in first out
# Wie warteschlange der als erstes kommt erster der bedient wird, neues Element kommt immer hinten hinzu, zugegriffen wird immer auf das erste
# z.B. bei q = [1, 2, 3, 4] 1 wird als erstes behandelt also daher nach reiehnfolge wann sie hinzugefügt wurden
# man hat immer nur acces aufs erste element sonst kein queue
# Operationen:
# Enqueue -> fügt element hinten an queue an, bei arrray *O(1), bei linked list O(1) wenn man Tail hat und es doubly linked list ist sonst O(n)
# Dequeue -> erstes element löschen, bei array O(n) da man alles verschieben muss, bei linked list immer O(1)

# Stacks
stack = []

# append
stack.append(3)
stack.append(2)
stack.append(4)

# pop
x = stack.pop(-1)
x = stack.pop() # returnt das entfernte element

# peek
stack[-1]

# is empty
try:
    stack[-1]
except IndexError:
    True
else:
    False 

# oft auch len, entspricht aber nicht mehr stack prinzip
if len(stack) == 0:
    True
else:
    False

# Queues
# nur eine schnelle Queue oder Stack → deque.
# Thread-sichere Queue für Producer/Consumer → queue.Queue.
# queue verwendet intern deque
# ähnlich wie doubly linked list
from collections import deque # -> doubly ended queue

q = deque()

# enqueue - append zur rechten seite
q.append(2)
q.append(3)
q.append(3)
print(q)

# dequeue - pop von linker seite
x = q.popleft() # q.pop() würde es wie stack behandeln

# peek
q[0] # q[-1] würde wie stack peeken

def isValid(s: str) -> bool:
    dctn = {"(":")", "[":"]", "{":"}"}
    stack = []
    for x in s:
        if x in dctn.keys(): stack.append(x)
        else:
            if stack and dctn[stack[-1]] == x: stack.pop()
            else: return False

    return True if not stack else False

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min: self.min.append(val)
        else:
            if self.getMin() >= val:
                self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin(): self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
    


# class MyCircularQueue:

#     def __init__(self, k: int):
#         import array
#         self.circular_Buffer = array.array("i", [-1 for _ in range(k)]) # festes array, zeigt bei jedem leeren wert auf -1

#         self.write_Pointer = 0 # stellt index da wo zuletzt eingefügt wurde
#         self.read_Pointer = 0 # stellt index vom ältesten wert der Queue da
        
#         self.length = k # stellt fäste länge des arrays da

#         self.elmnts = 0

#     def enQueue(self, value: int) -> bool:
#         self.elmnts += 1
#         # wert bei dem eingefügt werden soll
#         appnd_position = self.write_Pointer

#         if appnd_position >= self.length: appnd_position = 0 # >= da index immer bei 0 startet
#         if appnd_position == self.read_Pointer:
#             if self.read_Pointer +1 >= self.length:
#                 self.read_Pointer = 0
#             else:
#                 self.read_Pointer += 1
#         self.circular_Buffer[appnd_position] = value
#         self.write_Pointer = appnd_position+1 # updated zum letzten eingefügten wert
#         print(f"Write_Pointer = Index: {self.write_Pointer}")

#     def deQueue(self) -> bool:
#         self.elmnts -= 1
#         if self.read_Pointer + 1 <=  self.write_Pointer:
#             if self.read_Pointer +1 >= self.length:
#                     self.read_Pointer = 0
#             else:
#                 self.read_Pointer += 1
#             return True
#         else: return False

#     def Front(self) -> int:
#         return self.circular_Buffer[self.write_Pointer]

#     def Rear(self) -> int:
#         return self.circular_Buffer[self.read_Pointer]

#     def isEmpty(self) -> bool:
#         if self.elmnts == 0: return True
#         else: return False

#     def isFull(self) -> bool:
#         if self.elmnts == self.length: return True
#         else: return False



class MyCircularQueue:

    def __init__(self, k: int):
        import array
        self.circular_Buffer = array.array("i", [-1 for _ in range(k)]) # festes array, zeigt bei jedem leeren wert auf -1

        self.write_Pointer = 0 # stellt index da wo zuletzt eingefügt wurde
        self.read_Pointer = 0 # stellt index vom ältesten wert der Queue da
        
        self.length = k # stellt fäste länge des arrays da

        self.elmnts = 0

    def enQueue(self, value: int) -> bool:
        if self.elmnts < self.length:
            self.elmnts += 1
            if self.write_Pointer >= self.length: self.write_Pointer = 0 # zuerst write pointer definieren falls nötig
            self.circular_Buffer[self.write_Pointer] = value # dann wert einfügen
            self.write_Pointer += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.elmnts != 0:
            self.elmnts -= 1
            if self.read_Pointer >= self.length: self.read_Pointer = 0
            self.circular_Buffer[self.read_Pointer] = -1
            self.read_Pointer += 1
            return True
        return False

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.circular_Buffer[self.read_Pointer]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.circular_Buffer[self.write_Pointer-1]

    def isEmpty(self) -> bool:
        if self.elmnts == 0: return True
        else: return False

    def isFull(self) -> bool:
        if self.elmnts == self.length: return True
        else: return False

q = MyCircularQueue(6)

print(q.circular_Buffer)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.enQueue(7)
print(q.Front())
print(q.Rear())
print(q.circular_Buffer)
print("===================")
print(q.read_Pointer)



