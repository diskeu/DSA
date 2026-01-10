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

# Da die Adjecency List O(v^2) (v in dem fall anzahl an v) braucht zum herstellen (für jedes v -> vertex / node muss man anzahl an v dinge herstellen) ist die matrix nur besser wenn man viele operationen hat
# Adjecency List braucht nur O(v) zum herstellen

# wenn [A, B] dann ist die Kante einfach die Aussage das A und B gemeinsam in einer Liste stehen