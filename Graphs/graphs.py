# Graphs Edge Lists, Adjacency Matrix, Adjacency List, DFS, BFS

# Trees, Linked Lists, sind eine subklasse von Graphen

# Graph besteht aus G = (V, E)
# V = Mengen der Knoten -> Verices
# E -> Mengen der Kanten (Edges) -> verbindungen zwischen den Knoten

# In einem Vertex kann man jede Datentyp speichern
# ein vertex muss keine edges haben auch wenn es meistens so ist
# ein vertex = node

# Jede Linked List und jeder Tree ist ein Graph ein Graph hat weniger regeln fürs aussehen als linked list oder Trees

# Directed Graph
#    A -> B
#    ^    ^
#    |    |
#    C -> D
# Man kann nur in eine Richtung zwischen den Nodes gehen, A ist mit B verbunden aber B ist nicht mit A verbunden
# Undirected Graph
#    A --- B
#    |     |
#    C --- D
# Man kann in beide Richtungen zwischen den Nodes gehen

# Graphen können Loops entstehen lassen -> Cyclic -> heist es ist ein Zyklus im Graph
# Ein Graph ist zyklisch (cyclic), wenn man von einem Knoten starten und über Kanten wieder zum selben Knoten zurückkehren kann, ohne eine Kante zweimal zu benutzen.
# Zyklus muss mindestens 3 verschiedene Knoten involviert haben

# Graph kann in Edge List gespeichert werden zb Edge List = [[0, 1], [1, 2], [0, 3], [3, 7], [3, 6], [3, 4], [4, 2], [4, 5] [5, 2]]
# Die reihenfolge im Array macht keinen unterschied aber Linke node in der sublist ist immer von und rechte immer zu
# F -> T
# [0,  1]
# Directed [F, T] -> Struktur, wenn undirected nicht mehr einträge heist einfach von F kann man zu T gehen
# 0     ->      1       ->      2
#   \                         ^ ^
#    v                      /    \
#     3     ->            4    -> 5
#    / \
#   v   v
#   7   6
# Normalerweise interessiert einem beim Grafen nicht der gesamte graph sondern nurwo man von einer bestimmten Node hinkann
# Adjacency Matrix -> 2 dimensionale Matrix -> liste von listen (Nachbarschaftsmatrix)
# n rows und n columns
# ist eine tabelle die die verbindungen zwischen knoten eines graphen beschreibt
# 0 bedeuted kein edge 1 bedeuted edge

#     A   B   C   D

# A   0   1   1   0

# B   1   0   0   1

# C   1   0   0   1

# D   0   1   1   0
# Das sich ein Computer so einen Graphen merken kann gibt es zwei möglichkeiten
# 1). Adjacency Matrix -> Zeile -> Startknoten, spalte -> Zielknoten
# 2). Adjacency List -> statt eine ganze Tabelle zu machen schreibt man einfach nur wer mit wem verbunden ist -> man spart speicher da man nur die existierenden verbindungen speichert

# Um zu prüfen ob D mit A verbunden ist
# In einer Adjecency matrix muss man nicht die ganze matrix durchgehen man schaut einfach matrix[D][A] ist 0 oder 1 -> O(1)
# Bei list muss man in liste von D gehen und prüfen ob in [B, C] A enthalten ist O(V)

# =============BEISPIEL=============
# ===========================================================================================================================================================
# Man hat 10 Knoten, aber nur wenige verbindungen
# Knoten (vertices) -> A B C D E F G H I J
# Verbindungen (kanten / edges) ->
# A - B
# A - C
# B - D
# C - E
# In einer Adjecency List würde man nur das was wirklich exisitert, keine 0
# A: B, C
# B: A, D
# C: A, E
# D: B
# E: C
# F:
# G:
# H:
# I:
# J:
# In der Matrix würde man für jede verbindung die anzahl an verbindungen speichern 10 * 10 (O(v^2))
#     A B C D E F G H I J
# A   0 1 1 0 0 0 0 0 0 0
# B   1 0 0 1 0 0 0 0 0 0
# C   1 0 0 0 1 0 0 0 0 0
# D   0 1 0 0 0 0 0 0 0 0
# E   0 0 1 0 0 0 0 0 0 0
# F   0 0 0 0 0 0 0 0 0 0
# G   0 0 0 0 0 0 0 0 0 0
# H   0 0 0 0 0 0 0 0 0 0
# I   0 0 0 0 0 0 0 0 0 0
# J   0 0 0 0 0 0 0 0 0 0
# 96 Felder sind Leer und nur 4 davon besetzt

# Unterschied
# Welche nachbern hat A
# in der matrix würde man in spalte A alle werte durchsehen und prüfen ob sie 1 sind O(v)
# in der liste wenn man sie so wie dict behandelt dann würde man einfach matrix[A] machen und sieht direkt die nachbern

# Ist H mit I verbunden
# in der matrix würde man zur zeile H gehen und in der zeile zur spalte I -> eine operation
# in der liste würde man zu H gehen (1 operation) und sehen ob I enthalten ist, wenn H aber n verbindungen hat im worst case dann O(E)

# Ist A mit J verbunden
# Matrix mann muss wieder nur zur zeile A und schauen ob wert 0 oder 1 bei J ist
# liste mann müsste zu A gehen und jeden wert in A prüfen ob I darinnen ist

# meistens benutzt man für graph dict
# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "E"],
#     "D": ["B"],
#     "E": ["C"],
#     "F": [],
#     "G": [],
#     "H": [],
#     "I": [],
#     "J": []
# }
# graph[A] -> O(1) -> Hash Table

# in python könnte man statt "A": ["B", "C"] einfach "A": {"B", "C"} machen und zugriff würde jedesmal nur zwei operationen brauchen
# dafür braucht die version auch mehr speicher -> hash sets / tables haben keine reihenfolge liste schon

# Matrix
# matrix = {
#     "A": {"A": 0, "B": 1, "C": 1, "D": 0},
#     "B": {"A": 1, "B": 0, "C": 0, "D": 1},
#     "C": {"A": 1, "B": 0, "C": 0, "D": 1},
#     "D": {"A": 0, "B": 1, "C": 1, "D": 0},
# }
# Ist A mit D verbunden? matrix["A"]["D"] == 1 braucht immer O(1)

# Ein dictionary mit sets ersetzt matrix fast überall, man speichert keine unnötigen 0 und ist genauso schnell
# der grund wieso es dei matrix trotzdem gibt -> mathematische algorythmen brauchen echte matrixen
# Nachteil an vielen dict -> Speicher = Key + Hash + Pointer + Value und sie muss immer größer sein als die anzahl an elementen sonst zu viele kollisionen
# ===========================================================================================================================================================
# ===========================================================================================================================================================

# Da die Adjecency Matrix O(v^2) (v in dem fall anzahl an v) braucht zum herstellen (für jedes v -> vertex / node muss man anzahl an v dinge herstellen) ist die matrix nur besser wenn man viele operationen hat
# Adjecency List braucht nur O(v+e) zum herstellen

# wenn [A, B] dann ist die Kante einfach die Aussage das A und B gemeinsam in einer Liste stehen

# wenn man bei adjecency matrix bei einer reihe prüfen muss welche verbindungen es gibt müsste man durch die ganze zeile udrchgehen um zu prüfen auch wenn die zeile keine verbindungen hat
# von einer node die edges sind ihre neighbours

# Adjecency List ist am einfachsten als hashmap mit list als verbindungen
graph = {
    "A": ["B"],      # A zeigt auf B
    "B": ["C"],      # B zeigt auf C
    "C": ["F", "D"], # C zeigt auf D und F
    "D": ["A", "E"], # D zeigt auf A und E
    "E": ["F"],      # E zeigt auf F
    "F": ["C"],      # F zeigt auf C
}

# man könnte auch werte als klasse speichern jede node ist eine klassenobjekt und die verbindungen sind in einer liste von anderen klassen objekten
class Node:
    def __init__(self):
        self.val = None
        self.neighbours = []

    def __str__(self):
        return f"Node({self.val})"
    
    def display(self):
        connections = [node.val for node in self.neighbours]
        return connections
    
A = Node ('A')
B = Node ('B')
C = Node('C')
D = Node ('D')
A.neighbors.append(B)
B.neighbors.append(A)
C.neighbors.append(D)
D.neighbors.append(C)

# Bei Graphen will man sie normalerweise durchgehen (traversal) man kann es zb mit einer dfs oder bfs machen
# A → B
# ↑   |
# |   v
# D ← C
# |   |
# v   v
# E → F
# Directed Graph - DFS -> Rekursiv (Call stack)
# Depth first search probiert auf tiefe zugehen also zuerst einen pfad runterzugehen
# zuerst in dem obigen beispiel A dann B dann C dann F, wenn man dan auf nichts weiteres stoßt geht man zurück und macht dort weiter
# wenn es andere nodes gibt die mit F verbunden sind würde man F dann nicht nochmal durchgehen auch wenn F zb nachbern wie J und K hätte,
# da man diese nachbern beim ersten besuch von F sowieso schon gesehen hätte
# um zu wissen welche dieser nodes man schon gesehen hat speichert man ein hash set wo alle besuchten werte drinnen sind, hash set da man dann in O(1) überprüfen kann
# A -> seen = [A] -> B [A, B] -> [A, B, C, F], dann C, dann D, [A, B, C, F, D], dann merkt man das man A schon gesehen hat also geht man zu E [A, B, C, F, D, E]
# Output = A B C F D E
# DFS besucht nur das was vom startknoten aus erreichbar ist egal ob es kanten hat oder nicht
# Iteratives DFS mit stack funktioniert genauso
seen = set()
def dfs_recursiv(node, adjecency_List): # Time Complexity: O(V + E) -> für alle erreichbaren minimal eine operation und alle edges werden durchgangen Space Complextiy: O(v) alle verticies werden einmal in seen gespeichert und der längste weg kann maximal O(v) im call stack speichern wie zb bei linked list
    print(node, end=" ")
    for vertex in adjecency_List[node]:
        if vertex not in seen:
            seen.add(vertex)
            dfs_recursiv(vertex, adjecency_List)

dfs_recursiv("A", graph)
def dfs_iterativ(start_Node, adjecency_List): # Time complexity: O(V + E) für jeden knoten geht man all seine nachbern durch, Space Complexity: Man speichert im stack einmal alle verticies im worst case und einmal in seen also O(v)
    seen = {start_Node}
    print("")
    stack = [start_Node]
    while stack:
        cur = stack.pop() # if node in seen: return wäre hier ineffizient da man ja schon davor prüfen kann ob man den wert überrhaupt im stack nochmal behandeln will
        print(cur, end=" ")
        for vertex in adjecency_List[cur]:
            if vertex not in seen: # if vertex not in seen ist eine operation
                stack.append(vertex)
                seen.add(vertex) # wenn man cur nicht gleich in seen macht kann es sein das ein wert im stack liegt z.B. [B, C] und dann kommt C dran aber die nodes von C enthalten auch B aber B ist noch nicht drangekommen und darum noch nicht in seen

dfs_iterativ("A", graph)

# Während auf dem Stack etwas liegt heist das es gibt eine Node noch zum Processen

# Auch wenn man bei DFS am stack alle nachbern von der derzeitigen node auf den stack legt geht man immer nur den pfad von einer node weiter
# Die reihenfolge kommt darauf an in welcher reihenfolge werte gespeichert hat

# In Breadth first search benutzt man wie bei binary trees queue
def bfs(start, adjecency_list):
    print("")
    from collections import deque
    queue = deque([start])
    seen = set()
    while queue:
        cur = queue.popleft()
        print(cur, end = " ")
        seen.add(cur)
        for vertex in adjecency_list[cur]:
            if vertex not in seen: queue.append(vertex)

bfs("A", graph)
# Man geht nie in einem pfad tiefer als wie in einem anderen

# DFS und BFS im obigen Beispiel würde auch für undirected Graph funktionieren wenn man die werte korrekt in der adjecency list einträgt

# V -> nummer von verticies auch n, die time complexity im graphen ist nicht O(V*E), da dies heisen würde das man für jeden vertex im graphen alle gesamten verbindungen durchsucht
# richtig wäre man besucht alle verticies einmal und alle edges einmal man besucht die edges da man for vertex in adjecency_list[cur]: macht was zu E führt, auch wenn man dann nur die verbindungen von den noch nicht gesehenen durchgeht, man schat sich troztdem einmal alle edges einmal an
# man sieht nicht alle edgeses pro vertex sondern dem vertex seine edges pro vertex
# for vertex in adjacency_list[cur]:
#     stack.append(vertex)
# 	•	Du gehst durch alle Nachbarn (also durch alle Edges)
# 	•	Und das kostet Zeit
# Eine Edge ist also nicht nur „physisch“, sondern sie ist ein Eintrag in der datenstrukur
# Time complexity bleibt bei dfs und bfs gleich, operationen dauern gleich lange auser man benutzt für die queue ein array und nicht eine double ended queue
# deque hat intern keine direkte Index-Adressierung wie eine Liste

# Space complexity ist O(V), da man seen baut das auch O(V) ist und dann muss man auch noch alle werte in entweder einen stack speichern wo im worst case O(v) werte sind oder in einem call stack wo auch maximal O(v) werte drinnen sind
# Wenn man die liste selbst mitzählt ist die space complexity O(V + E) da man in der liste auch alle edges speichern muss

# Trees im Kontext von Graphen sind einfach Graphen mit bestimmter vorgabe
# Trees haben im standart kontext parents, in leetcode wird es aber oft auch ohne parents dargestellt
# acyclic -> kein zyklus im graphen
# Trees sind acyclic da sie wegen ihrer definition keine zyklen haben können
# Trees sind connected das heist man kommt von überall überall hin, sie sind acyclic connected -> man kommt von überall überall hin aber es sind keine zyklen möglich
# Unconnected wäre directed graph bei denen nicht verbundene nodes zulässig sind oder undirected graphs bei denen nicht verbundenne nodes zulässig sind
# Wenn man bei einen Tree n nodes / v verticies dann sind die edges gleich n - 1, da wenn man einen connected acyclic graphen hat es nur einen weg gibt von einem ort zum anderen zu kommen darum ist es auch acyclic bei cyclic graphen würde es mehrere wege geben von einem punkt zum nächsten zu gelangen
# bei einem undirected graph gibt es in der adecency list doppelt so viele einträge aber nicht doppelt so viele kanten da die verbindung von einer kante trotzdem eine bleibt A -- B ist genausoviel edges wie A -> B
# bis ein graph connected ist braucht er mindestens v - 1 knoten, basis = v = 1, E = 0, bei einem vertex gibt es keine verbindungen, nach der basis dann immer v = 3, E = 2, darum hat er immer v - 1 edges
# wenn man weniger als v - 1 vetivies hat dann ist es nicht möglich den graphen zu connecten ohne das er ein graph bleibt

# Array von Edges (directed) [Start -> End]
n = 8
arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]] # -> Edge list
def convertToList(arr:list) -> dict: # -> T: O(n), S: O(V + E)
    """Converts Edge List to Adjecency List"""

    from collections import defaultdict # -> wenn wert noch nicht existiert wird er erstellt, so keine if wert in dict prüfung
    print("")
    adjecencyList = defaultdict(list) # -> first argument must be callable or None
    for u, v in arr: # -> unpack tuples
        adjecencyList[u].append(v)
        # adjecencyList[v].append(u) -> wenn direkted
    
    return adjecencyList

print(convertToList(arr))

def convertToMatrix(arr:list) -> dict: # T: O(V^2 + E), S: O(V^2)
    """Converts Edge List to Adjecency Matrix"""

    global n
    n += 1
    adjecencyMatrix = []
    for _ in range(n): adjecencyMatrix.append([0]*n) # O(V^2)
    for u, e in arr: # -> u -> Start, e -> end
        adjecencyMatrix[u][e] = 1 # jede kante wird einmal durchgegangen O(E)

        # adjecencyMatrix[u][e] = 1 -> wenn undirected

    # adjecencyMatrix = {r: adjecencyMatrix[r] for r, _ in arr} # schnellerer zugriff, troztdem noch nicht schnellster zugriff
    return adjecencyMatrix

print(convertToMatrix(arr))

dfs_iterativ(0, convertToList(arr))
dfs_recursiv(0, convertToList(arr))
# Bei einer adjacency matrix müsste man zuerst jedem wert einen index zuordnen und die matrix immer so groß wie alle werte machen