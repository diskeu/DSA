# Recursion

# Fibonacci nummern -> jede neue Zahl wird mit den Zwei zahlen davor addiert -> [0, 1, 1, 2, 3, 5, 8, 13]...
# f = []
# f[0] = 0      -> bei erster Zahl
# f[1] = 1      -> bei zweiter Zahl
# f[n] = f[n-1] + f[n-2]      -> bei jeder Zahl danach
c = 0
def F(n):
    global c
    c += 1
    if n == 0: return 0
    elif n == 1: return 1
    else:
        print(f"F({n-1})+F({n-2})")
        return F(n-1) + F(n-2) # -> Recursiv Funktion ruft sich selber wieder in der funktion auf | DOUBLING EFFECT genau an dieser Stelle

print(F(5)) # -> 5
print(c)

# !! f(n) fibonacci zahl an position n
# Python macht zuerst komplett F(n-1) fertig bis zu den basisfällen, erst dann wird der rechte Ast mit F(n-2) abgearbeitet
# Ist Recursiv Tree, die Leaves sind die Werte die die Funktion nicht noch einmal aufrufen
# Innere Knoten sind die Werte die Kinder erzeugen
# 8
# ├─ 4
# │  ├─ 2
# │  │  └─ 1
# │  └─ 2
# │     └─ 1
# └─ 4
#    ├─ 2
#    │  └─ 1
#    └─ 2
#       └─ 1
# Alle leaves sind in dem Fall 1, die Inneren Knoten sind 8, 4, 2, 2, 4, 2, 2
# Call stack -> Call -> Function Call stack
# ist ein Stack der sich merkt welche Funktion gerade aufgerufen wurde
# bei jeder neuen Funktion wird zum stack appended und wenn die Funktion ein ende erreicht hat wird vom stack gepoppt und Computer weis dann was die darüberliegende Funktion war
	# 1.	Jeder Funktionsaufruf wird auf den Stack gelegt.
	# •	Dabei merkt sich der Computer: „Welche Funktion wird gerade ausgeführt, welche Parameter wurden übergeben, wo muss ich nach der Rückkehr weitermachen?“
	# 2.	Wenn die Funktion eine weitere Funktion aufruft (wie bei Rekursion), wird ein neuer Eintrag oben auf den Stack gelegt.
	# 3.	Wenn die Funktion fertig ist (Return erreicht), wird der Eintrag vom Stack entfernt (pop), und die Kontrolle geht zurück zur vorherigen Funktion.

# z.B. bei F(4)
# Call Stack: -> liegt gemeinsam im Speicher

# ===================================================================
# F(1) n = 1, return adress = F(2) weiter | C, adress = F(1) Code | D                                   -> Base Case
# ===================================================================
# F(2) n = 2, return adress = F(3) weiter | B, adress = F(2) Code | C
# ===================================================================
# F(3) n = 3, return adress = F(4) weiter | A, adress = F(3) Code | B                                   -> kommt als erstes zu F(2) also muss es zuerst F(2) wossen
# ===================================================================
# F(4) n = 4, return adress = nächste Anweisung im Hauptprogramm, adress = F(4) Code | A                -> kommt als erstes zu F(3) also muss es zuerst F(3) wissen

# Dann wenn man zu Base Case kommt return der Base case zu seiner return adress seinen Wert und löscht sich vom stack, die return adresse merkt sich dann das es ihn schon gerufen hat
# und er den wert x zurückgegeben hat -> also F(1) = 1, da F(2) sich danach komplett ausführt und noch nicht weis was der wert bei F(0) ist geht es zu F(0), F(0) merkt sich wieder die
# return adresse und gibt dann F(0) = 0 zurück und löscht sich vom stack, dann führt sich F(2) komplett aus und returnt F(1) + F(0), also F(2) = 1 und löscht sich vom stack und returnt den wert davon zu seiner return adresse und so weiter

# Platz von F(n-1) und F(n-2) ist wichtig damit es weis was zuerst auseführt wird

# Doubling Effect -> Anzahl der aufgerufenen Funktionen verdoppelt sich auf jeder Ebene
# Höhe des Baums ist zirka meistens n da man ja F() so oft aufrufen muss bis man zu 0 oder 1 kommt
# F(4) -> F(3) -> F(2) -> F(1)
# Höhe eines Baums = die längste Strecke von der Wurzel bis zu einem Blatt (Anzahl der Kanten oder Knoten).
# Jeder Aufruf reduziert n um 1 oder 2.
# •	Der längste Pfad im Baum ist also die Folge von F(n) → F(n-1) → F(n-2) → … bis Base Case.
# Wichtiger Punkt: Höhe ≠ Anzahl aller Knoten, nur die längste Strecke

# Bei der Time complexity nimmt man die maximale anzahl an aufrufen der Funktion, z.B. bei Fibonacci spielt es keine Rolle das eine Seite weniger Aufrufe macht, es bleibt trotzdem O(2**n)
# Pro Ebene das doppelte an Knoten zuvor
# 2 kommt davon das jeder knoten 2 neue macht

# Space Complexity
# Ist O(n) da am call stack nie mehr werte sein können als n, da es immer einen weg geht und dann erst zurück und den nächsten
# Es braucht speicher da jeder aufruf der Funktion speicher braucht nicht nur die Haupt Funktion,
# beim call stack können aber nie mehr funktionen als n liegen darum O(n)
# Es können nie mehr Wege aufeinmal gewählt werden nie Links und Rechts gleichzeitig

# Rekursiv bei Funktionen -> eine Funktion ruft sich selber auf
# Bedeuted immer „Ein Problem wird mithilfe eines kleineren Problems derselben Art beschrieben.“
# Bei Linked List, jede node zeigt auf ein kleineres Problem
	# •	Die Struktur ist rekursiv (next → Liste)
	# •	Die Funktion ist rekursiv (length ruft length auf)

# Eine Linked List ist rekursiv definiert, weil jeder Knoten auf einen kleineren Teil derselben Struktur verweist.
# Eine Funktion kann rekursiv auf die Liste zugreifen, weil das Problem („Liste bearbeiten“) sich auf das kleinere Problem (Rest der Liste) reduzieren lässt.
# "Rekursiv" bedeutet, dass etwas sich selbst wiederholt oder sich auf eine selbstähnliche Weise definiert, indem es ein Problem in kleinere, gleichartige Teilprobleme zerlegt, bis ein einfacher Basisfall erreicht ist

def q(n):
    if n == 1 or n % 2 == 1: return n
    else:
        print(f"q({int(n)/2})")
        return q(int(n)/2)

print(q(2**7))
print(2**12) # -> 16

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

Head = Node1

def rev(H: object) -> object:
    cur: object = H
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def r(node): # Time = O(n) Space = O(n)
    if not node:
        return
    else:
        r(node.next)
    print(node.val)

# next = None 5 1
# r(40) 4 2
# r(30) 3 3
# r(20) 2 4
# r(10) 1 5
r(Head)

h = rev(Head)
cur = h
while cur:
    print(cur.val)
    cur = cur.next



def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0: return False
    if n == 1: return True
    elif n % 2 != 0: return False
    return self.isPowerOfTwo(n//2)

def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev

def reverseList(self, head):
    prev = None
    cur = head
    def rev(prev, cur):
        if not cur: return prev
        cur_next = cur.next
        cur.next = prev
        return rev(cur, cur_next)
    return rev(prev, cur)
