# Binary Trees

# Binär Baum besteht aus Knoten (Nodes) und ist wie ein Baum angeordnet
# jede Node kann maximal zwei Kinder haben
#       - left child
#       - right child
# Knoten ohne Kinder ist Leafe node
# oberster Knoten ist Wurzel / root
# jeder Knoten kann wie ein eigenständiger binärbaum behandelt werden indem Node eine eigenständige root ist
# jeder Knoten kann alles mögliche speichern
# Node besteht aus wert, linkes child und rechtes child

class Node(): # -> beispiel implementierung
    def __init__(self, val: any) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __str__(self): # wenn etwas geprinted wird returnt es den wert
        return str(self.val)

# bei leafe nodes ist left und right None und signalisiert ein ende vom zweig

# man hat bei jedem binary tree eine eigentliche root aber wenn man z.B. zu einer Node geht kann man diese als eigenen subtree behandeln die ihre eigene root hat
# die eigentliche root -> global root
# root bei einem subtree -> local root

#       A
#     /  \
#    B    C
#   /\    /
#  D  E  F 
# D E F sind leaves

# verbindungen ziwshen Nodes also left und right können als branch bezeichnet werden
# Parents sind wenn man auf eine Node sich bezieht die darüberstehende Node, in Leetcode wird aber ohne Parents gearbeitet

# Binary Trees sind subkategorie von graphen -> directed graphs weil ihre branches in eine richtung zeigen, man kann zb von Node C zu Node F aber nicht von F zu C

# Verschiedene typen von Trees:
# Complete Tree -> jede ebene ist ganz ausgefüllt bis vielleicht auf die letzte, die von links nach rechts gefüllt sein muss ohne löcher
# Perfect Tree -> jede ebene ist ganz ausgefüllt
# jeder Perfect Tree ist ein Complete Tree

# Man kann binary Trees wie arrays behandeln
# z.B. arr = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# um zu dem linken children von jeder Node zu kommen muss man den index * 2 rechnen
# beim rechten children index * 2 + 1
# man kann wenn man binary tree in array speichert jede node ohne left und right speichern was speicher spart
# da indexe meist bei 0 anfangen auch L = i * 2 + 1, R = i * 2 + 2
#        A
#      /   \
#     B     C
#    / \   / \
#   -   D E   F
# wenn tree nicht complete müsste man um ihn in einem array darzustellen die fehlenden werte mit z.B. None ersetzen
# arr = [A, B, C, None, D, E, F,]
	# •	Arrays für Binary Trees: praktisch für Complete Binary Trees
	# •	Unvollständige Bäume: besser mit Zeigern/Referenzen (Node-Objekte)
# Bei complete tree speichert man die Knoten level für level von links nach rechts
# Level 0: A
# Level 1: B C
# Level 2: D E F G
	# •	Jede Ebene hat 2ⁿ Knoten, wobei n die Ebene ist (0 = Wurzel)

# Height = maximum depth
# maximale tiefe
# jeder subtree hat auch eine höhe
	# •	Die Höhe eines Baums ist die Anzahl der Knoten auf dem längsten Weg von der Wurzel zu einem Blatt.

# Depth first Search (DFS)
# man geht zuerst komplett runter üb
	# •	Bei DFS geht man so tief wie möglich in einen Ast des Baums, bevor man zurückkehrt und andere Äste untersucht.
	# •	Man „taucht“ also in die Kinder eines Knotens, rekursiv oder mit Stack, bis man ein Blatt erreicht, dann geht es zurück.
# man geht z.B. A, B -> dann nach Links -> None und danach nach rechts -> wenn dann B fertig ist geht man bei B zum nächsten um B fertigzustellen
# wenn B fertig ist zurück zu A dann um A fertigzustellen bei A geht man dann nach C bei C wieder nach E wenn E returnt
# dann um C fertizustellen nach F und von C dann wieder nach A und A zurück zum Hauptprogramm sowie bei rekursion beim Call stack

# 3 unterkategorien bei DFS
# Preordered traversal -> man begutachtet zuerst node, dann links und dann rechts -> gilt für jede Node arr = [1, 2, 4, 5, 3, 6, 7]
# inordered traversal -> man geht zuerst links, dann begutachtet man und dann rechts -> für jede node arr = [4, 2, 5, 1, 6, 3, 7]
# Post ordered traversal -> man geht zuerst links, dann rechts, und dann begutachtet man -> für jede Node arr = [4, 5, 2, 6, 7, 3, 1]
# bei Preordered root ist das erste was begutachtet wird, bei post ordered letzte
# für jede Node macht man genau die reihenfolge und merkt sich was man schon gemacht hat

# BFS -> Breadth first search -> Breitensuche (Level order traversal)
# man begutachtet zuerst jede ebene komplett bevor man weiter runter geht

# DFS -> Priorität = depth -> wird mit Stack implementiert
# BFS -> Priorität = breite -> wird mit queue implementiert

# um DFS mit stack zu implementieren, macht man zuerst stack = [root] und visited = []
# dann wärend stack nicht leer ist, popt man zuerst element -> processed es und appended es zu visited, wenn es ein node.right hat node.right zum stack
# und wenn es ein node.left hat fügt man node.left zum stack -> man schaut zuerst ob es ein node.right gibt um dann node.left oberhalb vom stack zu haben
# dann proccesed man das oberste vom stack popt es und appended es zu visited
# dann schaut man wieder ob man R hat appended es dann ob man L hat und appended es
def preorder_stack(root): # preordered travarsial
    stack = [root]
    visited = [] # -> already visited nodes
    while stack:                                                                   # PROCESSING NODE
        node = stack.pop() # -> pop() gibt das element das wir löschen zurück      # |
        visited.append(node)                                                       # |
        if node.right: stack.append(node.right) # -> zuerst rechts da am stack aufs oberste element zugegriffen wird und es damit left ist
        if node.left: stack.append(node.left)
    return visited

def pre_order(node):
    if not node: return
    print(node)
    pre_order(node.left)
    pre_order(node.right)
# Preorder mit einem Stack ist ein „echtes“ (wahres) Preorder-Traversal.

# node = s.pop()
# if node.r: s.apnd(node.r)
# if node.l: s.apnd(node.l)

# Postorder ist NICHT definiert dadurch, wann ein Knoten verarbeitet wird,
# sondern dadurch, wann er ausgegeben wird.

def post_ordered(root): # post ordered travarsal | links -> rechts -> node
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)

    while visited:
        print(visited.pop())

def post_order_Recursion(node):
    if not node: return
    post_order_Recursion(node.left)
    post_order_Recursion(node.right)
    print(node)
# stack 2 algorithmus simuliert kein echtes postorder, er erzeugt sequenz Root → Right → Left und wenn man diese inventeirt kommt posorder sequenz
# Postorder entsteht als Nebenprodukt der Umkehrung,
# Postorder ist definiert durch die Reihenfolge der Ausgabe, nicht durch die interne Logik
# rekursive postorder -> folgt direkt der echten postorder struktur
# stack posorder mathematischer trick

# search mit stack in einem post ordered system ist grundsätslich problematisch
# traversal -> alle knoten in bestimmter reihenfolge besuchen
# search -> abbrechen bei einer bestimmten bedinung
# Warum post order für search schlecht ist -> links -> rechts -> node ist schlecht da node erst verarbeitet wird wenn alle kinder besucht sind
	# •	Du kannst die Wurzel nicht prüfen, bevor
	# •	der komplette linke UND rechte Teilbaum durchlaufen ist
# pre ordered ist hingegen für search gut da man zuerst node verarbeitet bevor man kinder besucht
# in praxis ist DFS fast immer pre order

def inorder(node): # -> links -> node -> rechts
    if not node: return
    inorder(node.left)
    print(node)
    inorder(node.right)
# processed in reihenfolge -> 4, 2, 5, 1, 6, 3, 7
# rekursiv inorder
# inorder(node):
#   inorder(node.left)
#   visit(node)
#   inorder(node.left)
def inorder_stack(root): # -> links -> node -> rechts
    stack = []
    visited = []
    cur = root
    while cur or stack: # erst abbrechen wenn stack leer ist
        while cur: # -> nach ganz links gehen
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        visited.append(cur.val) # -> process cur

        cur = cur.right # nach rechts wenn man ganz nach links gegangen ist
    return visited
# knoten wird erst ausgegeben sobald linker subtree fertig ist aber bevor rechter beginnt
# wahre inorder läuft in der richtigen reihenfolge ab

# BFS -> level ordered traversal -> wird mit queue implementiert
# Queue -> das erste das reinkommt ist das erste das verarbeitet wird -> wichtig da man als erstes jede ebene durchgehen muss
from collections import deque # double ended queuer / effizient da deque in O(1) geht leichtgewichtig darum für BFS besser -> schnelle datenstruktur
from queue import Queue # effizient und threadsicher hat auch max size, kann blockierend sein, wartet bis element verfügbar ist -> q.get()
def BFS(root): # -> gut um dinge zu suchen wenn man zuerst jede breite durchsucht | level ordered travarsial
    q = deque()
    q.appendleft(root)
    visited = []
    while q:
        cur = q.popleft() # -> node die man gerade proccesed
        visited.append(cur.val)
        if cur.left: q.appendleft(cur.left)
        if cur.right: q.appendleft(cur.right)
    return visited # -> [1, 3, 7, 6, 2, 5, 4]


# zuerwst hat man q = [1], dann popt man 1, wenn 1 ein L hat -> appnd L, wenn R, appnd R, dadurch hat man dan q = [2, 3]
# dann wieder node = dequeue, dann appnd L und R, also ist q = [3, 4, 5], dann wieder node = dequeue, dann appnd L, R,
# dann ist q = [4, 5, 6, 7] und dann noch so lange schauen ob es für die jeweilige node ein left und right gibt bis das q leer ist darum while q:
# rekursion ist von natur aus DFS LIFO artig hingegen braucht DFS ein first in first out verhalten

# um einen tree zu durchsuchen DFS oder BFS

# Time Space Complexity
# bei BFS und DFS ist Time complexity O(n) da man alle werte durchsuchen muss im worst case
# bei DFS ist space complexity O(tiefe des baumes), da man immer einen stack hat entweder call stack bei rekursion oder explizit der stack bei iteration
# im worst case ist der baum linear und auf jeder ebene ist nur eine node, dann wäre tiefe = n und darum O(n)
# da man bei big O immer worst case nimmt ist der worst case der im speicher des stacks ist immer die tiefe darum kann man für den stack auch ein static array nehmen man weis immer die maximale größe
# Bei perfect tree ist die anzahl der nodes durch n = (2^h) -1 definiert was umgeformt h = log(n+1) ist also ist space complexity O(log(n+1))
# log_2(x) fragt im Prinzip:
# „Wie oft muss ich durch 2 teilen, bis ich 1 erreiche?“ -> bei binary search halbiert man O(log(n)) schritte bis man eins erreicht / base case
# umkehrung logarythmus -> exponentialfunktion / 2^n

# Bei BFS -> Time complexiy -> O(n)
# bei BFS ist space complexity die anzahl an nodes auf der eltzten ebene
# 	•	Die maximale Anzahl von Knoten, die gleichzeitig in der Queue liegen, tritt in der tiefsten Ebene auf, weil die letzte Ebene die meisten Knoten hat.
# man bekommt die anzahl der nodes auf der letzten ebene durch 2^(h-1) also 2^(log(n+1)-1)
# !!! 2^(log(n+1)-1) ergibt zirka umgerechnet n/2 !!! -> weil die letzte Ebene hat fast genauso viele Knoten wie alle vorherigen zusammen
# die letzte ebene hat maximal n/2 nodes da man in bigO die konstante fallen lässt ist die space complexity auch O(n)

# EINFACH GESAGT
# DFS -> Time complexite O(n) -> Space Complexity O(n) (worst case linearer tree)
# BFS -> Time complexite O(n) -> Space Complexity O(n) (konstanten fallen weg)

# Binary Tree verdoppelt nodes auf jeder ebene
# !!! weil Tree sich auf jeder ebene verdoppelt hat man auf der letzten die hälfte des gesamten trees maximal -> 1 2 4 8 16 32 64 -> 64 -32 = 32 auf der letzten ebene maximal 32 nodes

# baum mit n nodes hat n-1 branches


# Binary Search Tree
# WENN -> Für jede Node sind die komplett linke seite vom Tree / subtree kleiner als alle werte auf der rechten seite
#          50
#        /    \
#      30      70
#     /  \    /  \
#    20  40  60  80
# 50 -> Root

def search_Tree(root, val): # time complexity -> O(n) da worst case es linear ist | space complexity O(n) -> nicht höhe da im worst case linear
    cur = root
    visited = []
    while cur:
        visited.append(cur.val)
        if cur.val == val: return True, visited
        elif cur.val > val: cur = cur.left
        else: cur = cur.right
    return False, visited
# kein DFS und kein BFS
# BST durchsuchen ist wie binary search nur mit tree
# DFS und BFS sind in erster Linie Bewegungs- / Traversierreihenfolgen.
# Sie werden erst dann zu Suchalgorithmen, wenn du nach etwas Konkretem suchst.
# BFS DFS ist eine systematische Besuchsstrategie
# !!! werden erst zu suchalgorithmen wenn man baum durchläuft und währendessen etwas sucht

# Höhenbalanciert / Height balanced -> wenn er zirka links gleiche weit nach unten wie rechts geht
# für jede node muss h(linker subtree) - h(rechter subtree) <= 1
# bei BST ist lookup wenn der tree höhen balanciert ist log(n) und space complexity O(1) -> immer nur ein pointer speichern
# -> man halbiert jedesmal direkt eine hälfte des trees / subtrees darum logarythmus da er definiert wie oft man durch 2 teilen muss bis man 1 erreicht

# Wenn man einen Binary Search Tree mit inorder durchgeht (links -> node -> rechts) dann geht man den tree sortiert durch
# def inorder_BST(root):
#     stack = []
#     visited = []
#     cur = root
#     while cur or stack:
#         while cur:
#             stack.append(cur) # -> nach ganz links bei jedem cur gehen
#             cur = cur.left
#         cur = stack.pop() # -> processing
#         visited.append(cur)
#         cur = cur.right # -> nach rechts gehen
#     return visited

# def inorder_BST_recursion(node):
#     if not node: return
#     inorder_BST_recursion(node.left) # -> zuerst nach ganz links
#     print(node) # -> node proccessen
#     inorder_BST_recursion(node.right) # -> nach rechts

# das geht darum das man zuerst nach ganz links geht wo die kleinste node des baums ist, man printed die node und dann geht man nach rechts wo die zweit kleinste ist

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)

Node8 = Node(5)
Node9 = Node(3)
Node10 = Node(9)
Node12 = Node(4)
Node13 = Node(8)
Node14 = Node(14)

bst_arr = [Node8, Node9, Node10, None, Node12, Node13, Node14]
for i, node in enumerate(bst_arr):
    if not len(bst_arr)-1 < 2 * i + 1: node.left = bst_arr[2 * i + 1]
    if not len(bst_arr)-1 < 2 * i + 2: node.right = bst_arr[2 * i + 2]

arr = [Node1, Node2, Node3, Node4, Node5, Node6, Node7]
for i, node in enumerate(arr):
    if not len(arr)-1 < 2 * i + 1: node.left = arr[2 * i + 1]
    if not len(arr)-1 < 2 * i + 2: node.right = arr[2 * i + 2]

root = Node1

# preorder search (DFS) Time: O(n), Space: O(n)
def check_Value(node, val):
    if not node: return False
    if node == val: return True
    return check_Value(node.left, val) or check_Value(node.right, val)

print(check_Value(root, 2))
    
print("preorder stack")
print(preorder_stack(root)) # preorderd traversal stack
print("preorder recursion")
pre_order(root) # preorder traversal recursion
print(inorder_stack(root)) # -> inorder traversal
post_ordered(root) # -> post ordered traversal stack
post_order_Recursion(root) # post ordered traversal recursion
print(BFS(root)) # -> breath first search

print(search_Tree(Node8, 3)) # -> binary search tree
inorder(Node8) # -> recursiv inordered search
print(inorder_stack(Node8)) # -> iterativ stack inordered search

# !!! in order -> in_order !!!

# Man speichert graphen meist in array wenn man einen vollständigen tree wie bei einen heap hat, man speichert mit objekten in unvollständigen trees wie zb bei linked lists, da man sonst zu viele nulls speichert
# init:
# -> Initialisierungen können als sofortige Zuweisungen begriffen werden, die unmittelbar nach/bei dem Anlegen eines Objekts im Speicher vorgenommen werden.
# -> Alle statischen Objekte sind/werden nur einmal beim Programmstart initialisiert, und zwar typgerecht mit Null, falls keine explizite Initialisierung vorhanden ist.

# Erklärung warum bei heap sort man nicht sift up verwendet gefunden auf stack owerflow
# The number of operations required for siftDown and siftUp is proportional to the distance the node may have to move.
# For siftDown, it is the distance to the bottom of the tree, so siftDown is expensive for nodes at the top of the tree.
# With siftUp, the work is proportional to the distance to the top of the tree, so siftUp is expensive for nodes at the bottom of the tree.
# Although both operations are O(log n) in the worst case, in a heap, only one node is at the top whereas half the nodes lie in the bottom layer.
# So it shouldn't be too surprising that if we have to apply an operation to every node, we would prefer siftDown over siftUp.