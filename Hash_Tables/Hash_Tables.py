# Hash Tables, Hash functions, Sets & Maps

# Speichert Schlüssel Wert Paare unabhängig voneinander im Speicher
# Jeder Key weiß nichts von anderen Keys, Jeder Wert hat Key bei dem er gespeichert wird
# Damit for x in dict die Keys in Einfüge-Reihenfolge ausgibt, merkt sich Python zusätzlich eine logische Reihenfolge der Keys.
# Jeder Eintrag Bucket oder Slot genannt
# Hash Table besitzt einen eigenen Speicherblock wo dann die pointers zu den elementen im speicher sind

#       "str123" -> |Hash Funktion| -> 15231 -> 15231 % Anzahl der Positionen in der Tabelle -> 15231 % 5 = 1
#       "lmnop" -> 1234567 % 5 = 2
#       "xyz" -> 123456 % 5 = 1             Hash Funktionen können koalisionen verursachen
# 0 |
# 1 | "str123"
# 2 | "lmnop" ! "xyz"
# 3 | 
# 4 |
#
# Bei Koalision: Separate Chaining -> Linked List die werte sind die Nodes
# Andere werte eigentlich auch Linked List nur mit nur einer Node

# Hash Set
# Speichert nur einzigartige Werte ohne die Values
# Slot leer? → Wert einfügen
# Slot mit gleichem Wert? → ignoriere (kein Duplikat)
# Slot belegt, aber anderer Wert? → Kollision → Suche nächsten freien Slot

# Werte im Hash set finden ist *O(1) da es immer gleich lange dauert Wert zu berechnen und ihn dann mit dem index im Speicher aufzurufen
# Bei einer collition ist es aber so das man zuerst über jeden Wert der Linked List iritieren muss was O(n) ist
# Wert hinzufügen ist O(1), da der Index immer gleich Lange zu berechnen braucht, wenn bereits wert da ist dann wird header verschoben, dauert auch nur O(1)
# Wert löschen *O(1), da es sein kann das es in einer Linked LIst gespeichert wird


# Modulo Operator gibt immer Rest von einer division zurück - 10 % 2 = Null, 7 % 3 = 1, 6.5 % 2 = 0.5, Wie oft geht hinein, was bleibt Rest
# Bei Modulo kommt immer Wert der um maximal eins kleiner ist raus da sonst man ja die zahl nochmal durch dividieren könnte

# Hash Map

# Hash map nutzt gleiche prinzip wie hash sets nur kann man daten darin speichern
# Speichert Key value paare, keine Duplikate in den Keys
# Nur Key wird gehasht nicht value
# person = {"xy": 34} -> Anna wird gehasht Key wird als Index gespeichert
# Hash sagt wo gespeichert
# Slot:
    # Hash: hash("xy")
    # key: "xy"
    # value: 34
# Für anwendungen wo schneller zugriff wichtiger ist als Speicher
# Index ist immer Intern in der Hash Tabelle
# Das ist nur ein Slot im internen Array der Hash Table
# Er sagt „geh zu diesem Slot“, nicht „geh direkt zum Objekt im RAM“

# Lookup = *O(1) hash wird berechnet
# add O(1) da immer berechnet, wenn wert schon vergeben dann versetzt es header nicht ganze linked list
# Remove *O(1), del H["xy"]
# if in... *O(1) da es einfach hash berechnen muss und index im speicher prüft, bei value O(n), da es alle werte durchgehen muss

# Linear Probing
# Hash("xy") = Index 1
# Hash("ls") = Index 1
# Koallition, bei Linear Probing durchsucht es nächsten Slot, wenn frei, dann speichert es dort
# bei Lookup gleiches Prinzip, prüft immer ob slot den Wert hat oder ob es Leer ist, weil wenn Leer ist ist der Wert garantiert nicht in der liste
# linear Probing ist immer einen nach anderen Wert überprüfen
# Linear Probing ist *O(1). da es sein kann das es im worst case ganze tabelle durchgeht
# Wenn bei Linear Probing wert gelöscht wird dann könnte es sein das ein anderer Wert bei Lookup, der den gleichen Index hat auf Empty Slot stoßt und False returnt,
# weil bei Leeren Slot es normalerweise heist das es Wert nicht gibt
# Darum wird beim Löschen wert mit speziellen zeichen wie -1 gekennzeichnet das man weis das etwas da war aber nicht mehr da ist

# Wenn man Array mit N werte hätte, dann würde es O(n) dauern den Wert zu finden im worst case
# Bei Hash Table dauert es fast immer O(1) außer bei Linked List oder Linear Probing

# Hashable Objekte / Immutable
# strings
# integers
# Tuples (1, 2, 3)

# Nicht Hashable / mutable 
# Arrays
# Dictionarys

# Da hashable Objekte immutable sind, weil sonst schwierigkeiten wenn sich im Hash table gespeicherte Werte danach verändern und weil gleicheer Wert immer gleichen Index geben soll,
# bei mutable Objekten nicht so
# Hash Tables haben bei erstellung immer 8 Slots
print(hash("ls") % 2)

# Hashset - sets
s = set()
print(s)

# Adding *O(1)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
# Lookup *O(1)
if 3 in s:
    print(True)
if 9 in s:
    print(True)
# Remove Key *O(1)
s.remove(3)
print(s)
# Set construction O(n) - n Länge vom Str
strng = "AJGJDGJKDSKJGKSLDS"
setstrng = set(strng)
print(setstrng)
for x in setstrng: # O(n)
    pass

# Hashmap - Dictionary
d = dict()
d = {"xy":123,"ls":4321,"wk":34}
print(d)

# Adding Key:vak *O(1)
d["sk"] = [1,2,3,4]
print(d)
# Looking up *O(1)
if d["ls"] in d:
    print(True)
# Value von einem Key *O(1)
print(d["wk"])
# Iterating through key:val of dict O(n)
for key, val in d.items():
    print(key, val)

# Default Dict
from collections import defaultdict
default = defaultdict(int)

print(default[2])
# Counter
from collections import Counter

counter = Counter(strng)
print(counter)