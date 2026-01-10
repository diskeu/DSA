# Static arrays, dynamic arrays, strings

# Static Arrays = Arrays mit fester größe
# Python hat keine statischen Arrays da sehr limitierend sind, sind in der größe immutable
# Wenn arr = [1, 2, 4, 5] und arr[2] insert 7, dann arr = [1, 2, 7, 4] - 
# - jedes element muss um eins verschoben werden bei worst case also O(n)
# bei arr = [1, 2, 3, 4, 5] del 3 arr = [1, 2, 4, 5, x] alles muss bei worst case verschoben werden O(n)

# Dynamic Array
# bei append array hat oft noch freien speicher am ende wie zb arr = [1, 2, 4, 5, x, x] dann bei append einfach neuen wert einzufügen O(1)
# wenn kein speicher mehr frei ist hinten dann O(n) da neuer array mit mehr speicher und eingefügten wert gemacht werden muss
# bei del am ende O(1) da einfach memory hinten wieder frei gemacht wird, wenn aber del in der mitte oder anfang dann O(n) da im worst case
# alle werte vorgerückt werden müssen
# bei append O(n) oder O(1) bei del am anfang oder mitte O(n) da alle werte vorgerückt werden müssen, bei del am ende O(1)
# bei insert O(n) da imn worst case alles vorgerückt werden muss
# python macht bei arrays immer doppelt so viel platz wenn voll ist wei zuvor, bei arr = [0, 0] dann wenn voll arr = [0, 0, 0, 0], dann wenn voll arr = [0, 0, 0, 0, 0, 0, 0, 0] usw
# List - Dynamic Array
# appenden zum Ende speziell, meistens *O(1) aber öfters wenn memory voll ist dann O(n)

# elemente eines Arrays liegen nebeneinander im Ram
# Adresse:   100   104   108   112   116   120
# Wert:       5     7     9    12    14    20
# Index:      0     1     2     3     4     5

# wenn acces auf einen wert wird nicht durchgegangen bis zum Wert sondern adresse vom Wert mit Adresse = Startadresse + (Index * Größe eines Elements) berechnet
# darum ist modifizieren und inspecten O(1) nicht O(n) da nicht bis zum wert durchgegangen wird
# bei insert muss alles im worst case verschoben werden darum O(n)

# Strings
# sind immutable mann kann sie nicht verändern, wenn man zb bei str = "abc" "d" hinzufügen will dann müsste man neuen str mit O(n) machen
# man kann strngs inspecten mit str[1] mit O(1) aber nicht mit zb str[1] = "d" modifizieren
# in python wird ein Array Liste genannt, das es mehrere verschiedene Objekte enthalten kann

# Strings sind immutable (unveränderlich) in Python, um:
# 	•	Sicherheit und Vorhersehbarkeit zu gewährleisten
# 	•	Als Dictionary-/Set-Keys zuverlässig zu sein (hashbar)
# 	•	Speicher zu sparen (Interning möglich)
# 	•	Konsistentes Verhalten wie in anderen Sprachen zu haben

# Deshalb muss jede Veränderung einen neuen String erzeugen → fast alle Operationen, die ändern oder suchen, sind O(n).

# Arrays
a = [1, 2, 3,]

a.pop() # O(1)
print(a) # [1, 2]

a.insert(2, 3) # O(n)
print(a) # [1, 2, 3]

a[2] = 4 # O(1)
print(a) # [1, 2, 4]

a.insert(2, 3) # O(n)
print(a) # [1, 2, 3, 4]

print(a[3]) # O(1)
# 4

a.pop(3) # O(n)
print(a) # [1, 2, 3]

if 2 in a:
    print(True) # True

# Modifizieren (arr[i] = ...) → O(1): Direkter Zugriff über Index im Speicher.
# Prüfen (x in arr) → O(n): Liste muss jedes Element nacheinander durchsuchen.

print(len(a)) # O(1) da python die länge speichert also dauert es immer O(1)

# Strings

# Append to End - O(n) muss immer neuer str gemacht werden
s = "Hello"
b = s + " !"

if "e" in s: # O(n)
    print(True)

# Position O(1) da strings eigentlich wie arrrays gespeichert werden
print(s[1])

print(len(s)) # auch O(1) wie bei strngs