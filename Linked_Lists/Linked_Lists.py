# Singly Linked Lists, Doubly Linked Lists‚

# (1) -> (2) -> (3) -> [ ], 3 zeigt zu nichts, also ende der Linked List.
# Man nennt es Single Linked List, da es eine verbindung zwischen den Elementen gibt (->)
# [ Wert | next ] -> [ Wert | next ] -> None
#   Wert = gespeicherte Information
# 	next = zeigt auf die nächste Node
#   None = Ende der Liste

# Array zusammenhängender Block speicher
# linked List, flexibel kein zusammenängender Block von Speicher
# Vorteil - hat dynamische größe, kein vorab reservieren wie bei Array
# Einfaches einfügen und Löschen am Anfang
# Nachteil - zugriff auf bestimmte Elemente ist Langsam, da die ganze verkettung nachgegangen werden muss
# mehr speicherbedarf da die einzelnen Zeiger speicher brauchen

# Jedes element wird Node gennant, der einen wert und einen zeiger auf das nächste element hat
# Jedes Element wird Dynamisch irgendwo gespeichert
# Ein Node kennt nur seinen Nachfolger, aber nicht die Position im Speicher von Node 5, 10 usw.
# Deshalb musst du von Anfang (head) iterativ weitergehen, um das n-te Element zu erreichen.

# Bei insert kostet durchlaufen O(n) weil du vom head bis zum nten Element musst. Das einfügen selbst ist nur O(1), da nichts verschoben werden muss
# Letzte element bei linked list ist Null/None

# In python kein eingebautes Linked List, jedes Objekt der Linked List ist ein class objekt, node.next = node1 dann zeigt variable node.next auf nächste Node
# self.value ist immer der Wert des Objektes der Linked List

# Aufgebaut wie Kette, Elemente haben keinen Index
# Linked Lists haben keine festen Positionen weil bei Löschen Position sich sowieso verändern würde, um Element einzufügen, müsste man wert wo eingefügt werden soll kennen
# Löschen wäre auch O(n) zuerst bis zum wert durchgehen und dann next verschieben
# Inspecten wäre auch O(n)
# Lookup ist auch O(n)
# Wert am anfang Löschen, O(1)
# Wert am anfang einfügen, O(1)
# Vorletzten Wert löschen, O(n) mit Double linked list O(1) wenn tail zeiger vorhanden

# Double Linked List, jeder Note zwei Zeiger, next → zeigt auf den nächsten Node, prev → zeigt auf den vorherigen Node
# prev erlaubt es, auch rückwärts zu traversieren.
# head.prev = None und tail.next = None

# Szenario 1: tail-Zeiger vorhanden
# tail zeigt direkt auf das letzte Element.
# Um das letzte Element zu löschen:
# tail = tail.prev
# tail.next = None
# Kein durchlauf nötig
# ohne prev müsste man alles durchlaufen um auf den wert vor tail zu kommen O(n)
# Szenario 2: tail-Zeiger nicht vorhanden
# Dann musst du trotzdem vom Head aus gehen und den letzten Node finden → O(n)

# Wenn man in der Mitte löscht braucht man nur Zugriff auf den Wert der zu löschen ist und dann kann man mit double Linked List einfach löschen
# meistens geht das nicht da man nur zugriff auf Head und Tail hat und nicht Werte in der Mitte also O(n)



class Node_D():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
    
class Node_S():
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
    
class linked_List():
    def __init__(self, head):
        self.head = head
        
    def display(self):
        curr = self.head
        while curr:
            print(f"<- ({curr.value}) -> ", end="")
            curr = curr.next

    def delete(self, val):
        _, curr, prev = self.search(val)
        curr_prev = prev
        curr_prev.next = curr.next
        del curr_prev
    
    # if x in list
    def search(self, val):
        curr = self.head
        prev = None
        while curr:
            if curr.value == val:
                return True, curr, prev
            prev = curr
            curr = curr.next
        return False, curr
    
    def new_head(self, Node): # O(1)
        Node.next = self.head

    def append(self, Node):
        _, curr = self.search(None)
        curr.next = Node

Node1 = Node_D(20)
Node2 = Node_D(30)
Node3 = Node_D(40)
Node4 = Node_D(50)
Node1.next = Node2
Node2.next = Node3
Node2.prev = Node1
Node3.prev = Node2

Node4.next = Node1 # O(1)
Node4.prev = None
Node1.prev = Node4

Node15 = Node_D(25)

head = Node4

Node1.next = Node15
Node15.next = Node2
Node15.prev = Node1

tail = Node3
# Node 15 ist O(1) da position zum einfügen bekannt ist
# nach bestimmten wert zb wie 20 einfügen wäre O(n) da im worst case alles durchgelaufen werden müsste um wert zu finden
current = head
while current.value != 20:
    current = current.next
# dann Node einfügen

# Traverse List O(n)
current = head
while current:
    print(f"<- ({current.value}) -> ", end="")
    current = current.next


# Node mit double Linked List in der Mitte einfügen, suchen des values ist O(n), rest ist O(1)
current = head
while current.value != 25:
    current = current.next
# Zeiger so anpassen das nichts mehr auf das zu löschende Element Zeigt, und prev prev Zeiger auf current zeigen lassen
current_prev = current.prev
current_prev_prev = current_prev.prev
current_prev_prev.next = current
current.prev = current_prev_prev

# Variablen löschen
del current_prev, current_prev_prev

# Traverse List O(n). 
current = head
print("")
while current:
    print(f"<- ({current.value}) -> ", end="")
    current = current.next

# Join -> l = [a, b, c, d] " - ".join(l) --> "a - b - c - d"
