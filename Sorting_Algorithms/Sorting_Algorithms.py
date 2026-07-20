# Sorting Algorithmen

# Verschiedene Soritieralgorithmen

# Bubble Sort -> (name da sich die elemente min/max beim sortieren wie bubbles nach oben schieben

# Bubble sort funktioniert indem man einen pointer i setzt und dann wenn bei index i die zahl grösser ist als bei index i - 1 vertauscht man die werte
# und das macht man so lange bis i so groß ist wie die länge vom array, dann ist automatisch das größte element ganz am schluss am array
# dann startet man wieder bei 1 und macht das gleiche wieder den ganzen stack minus 1
# die elemente bubblen nach rechts
# Bubble sort hat eine Time complexity von O(n^2) da man für jeden wert zirka das ganze array durchgehen muss, die space complexity ist O(1) da man das gleiche array benutzt (Inplace)
def bubbleSort(arr: list) -> list: # T: O(n^2), S: O(1)
    n = len(arr)
    while n != 1: # letzter wert muss nicht verschoben werden
        swapped = False # wenn kein wert bei einem durchgang getauscht wurde ist bereits sortiert
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                swapped = True
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        if not swapped:
            break
        n -= 1
    return arr

print(bubbleSort([4, 2, 3, 21, 213, 32, 12, -32, 2, 1, 32, 33, 12, 21])) # -> [2, 4, 12, 21]

# normalerweise bei 13 elementen egal ob die liste schon sortiert ist oder nicht muss man 13+12+11+10+9+8+7+6+5+4+3+2+1 -> 91 operationen machen
# mit swapped flag die überprüft ob in dem durchgang überhaupt etwas getauscht wurde dauert es nur solange bis das alles sortiert wurden in dem fall 81
# wenn man n nicht kleiner macht dauert es immer n^2 im worst case mit n kleiner machen weniger

# nach einem ganzen durchgang steht das größte element ganz hinten

# Insertion sort

# die idee dahinter ist das man immer ein sortiertes array hat auf der linken seite und ein unsortiertes auf der rechten seite
# mit der zeit tut man dann unsortierte ins sortierte array und sortiert sie

# bei array [-5, 2, 3, 1 -3 -3, 7, 2, 2] hat man zwei pointer j und i die am anfang beide auf index 1 zeigen da ein array das 1 element hat automatisch sortiert ist
# dann überprüft man ob arr bei index i kleiner ist als bei index i - 1 wenn nicht dann setzt man i und j aufs nächste element wenn schon dann setzt man j auf i - 1 und tauscht die werte,
# dann geht man wiederhohlt von j bis zum anfang durch und überprüft ob j - 1 arr kleiner ist als j, das wiederhohlt man so lange bis man am anfang ist oder es sich nichts verändert hat
# die sortierte region wird jedesmal sobald i sich bewegt größer man muss zirka n mal alle n elemente von vorne bis hinten durchgehen also O(n^2)

# Insertion sort und bubble sort machen im worst case nur (n^2)/2 schritte

# Time complexity insertion sort: O(n^2), Space complexity O(1) -> inplace

# Bubble Sort (mit swapped)
# 	•	Runde 1: n-1 Vergleiche
# 	•	Abbruch
# O(n)

# Insertion Sort
# 	•	Für jedes Element 1 Vergleich
# 	•	Kein Verschieben
# O(n)
# Bei fast sortierten array -> [1, 3, 2, 5, 4, 7, 6] muss bubble sort viele runden machen und bei insertion sort gibt es keine extra runde wenn schon alles sortiert ist
# bei fehler weit vorne im array -> [1, 2, 3, 4, 5, 6, 7, -1] muss bubble sort das array n mal ganz durchgehen und überprüfen, bei insertion muss man nur einmal das array dann durchgehen
# insertion sort -> jeder fehler wird lokal behandelt
# es gibt viele inputs wo beide gleich schnell sind aber keinen input wo bubble sort schneller ist

# Swapping vs Shifting
# swapping -> zwei variablen vertauschen kostet immer O(1)
# shifting -> werte verschieben kann O(n) kosten
# implementation mit shifting: j zeigt immer eins weiter nach links als key, key ist immer der wert zu dem wir den richtigen platz zuweisen möchten
# dann iritiert man rückweärts über die sortierte liste solang j <= 0 ist das man nicht über den listenrand geht und j größer als der key ist -> da wenn j größer als der key ist das heist das der wert links vom key größer ist
# J ist immer bei dem wert den man vergleichen möchte
# -> arr[j + 1] = arr[j] -> der wert oberhalb von j nimmt j an -> !!!Man verschiebt das element j um eins nach rechts (indem man den wert über j j gleichsetzt)!!!
# j           arr             Aktion
# 2           [2,4,6,3]       arr[3] = arr[2] → [2,4,6,6]
# 1           [2,4,6,6]       arr[2] = arr[1] → [2,4,4,6]
# 0           [2,4,4,6]       arr[1] = arr[0] → [2,2,4,6]
# dann geht man einen schritt nach links im sortierten bereich
# irgendwann wird der loop brechen da entweder j kleiner ist als der key oder man das ende erreicht hat
# dann setzt man key zu j + 1 da wenn man das ende erreicht hat der key ganz hinten hinmuss und j dann -1 ist oder
# j ist größer als der key, die 3 im obigen beispiel geht nicht verloren da sie als key zwischengespeichert wurde
# wenn arr = [-2, -1, 4, 8, 3] key = arr[i] -> 3, j = i - 1 (3) -> while arr[j] > key
# dann ist arr -> [-2, -1, 4, 8, 8] -> j = 2 -> arr[j] -> 4 -> 4 > 3 -> [-2, -1, 4, 4, 8] -> j = 1
# dann ist arr bei index j + 1 (2) -> key und array sieht so aus -> [-2, -1, 3, 4, 8]
# der shift geht ohne zu poppen da man die werte einfach umstellt und da man immer gleich viele werte hat
# Beispiel [2,4,6,3]

# Shifting:
# 	•	Elemente größer als key=3: 4,6
# 	•	Schreiboperationen:
# 	•	arr[3] = 6
# 	•	arr[2] = 4
# 	•	arr[1] = key = 3
# 	•	Gesamt: 3 Schreiboperationen

# Swapping:
# 	•	Tausche 3 mit 6 → [2,4,3,6]
# 	•	Tausche 3 mit 4 → [2,3,4,6]
# 	•	Gesamt: 4 Schreiboperationen
# Bei swapping muss man auserdem bei jedem swap einen wert zwischenspeichern

# shifting ist minimal schneller aber bei größeren listen viel effizienter
# bei bubble sort wäre shifting unnötig da man sowieso nur eine operation hat und nie weiter zurück muss
# -> Bubble sort arbeitet paarweise nicht mit einem unterteilten array
# shifting ist nur sinnvoll wenn man länger werte vertauschen muss
# swapping dann wenn man einfach zwei werte vertauschen muss
def insertion_sort_swapping(arr):
    for i in range(1, len(arr)): # erster wert bis zu letztem wert
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
            else: break
    return arr

print(insertion_sort_swapping([1, 2, 3, 5, 6, 7, -1]))

def insertion_sort_shifting(arr):
    for i in range(1, len(arr)): # erster wert bis zu letztem wert
        key = arr[i] # gleicher lookup wöre bei swapping
        j = i - 1
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

print(insertion_sort_shifting([2, 32, 12, 23, 2, 23, -2, 23, -4, -21]))

# Selection sort

# Stabilität ist wenn ursprüngliche reihenfolge gleich bleibt
# wenn man z.B. zwei werte mit gleichem wert hat und die werte nach dem sortieren auch wenn sie den gleichen wert haben trotzdem hinter / nebeneinander bleiben ist es stabil
# wenn z.B. bei selection sort z.B. Liste: [ (A, 2), (B, 2), (C, 1) ] ist, dann wird [ (C,1), (B,2), (A,2) ] gemacht und A ist hinter B auch wenn sie denselben wert haben ist ihre reihenfolge vertauscht
# Bei insertion sort ist das nicht so bei z.B. Liste: [ (A, 2), (B, 2), (C, 1) ] wird nur C hinter A und B geschoben -> reihenfolge bleibt gleicht
# Bei bubble sort passiert tausch nur wenn links > index nicht wenn sie gleich bleiben -> reihenfolge bleibt gleich

# wie es funktioniert
# man geht die liste von links nach rechts durch und sucht das kleinste element, dann fügt man kleinste element hinten ein, dann wiederhohlend findet man dss zweitkleinste element im unsortierten bereich und ffügt es an zweiter stelle
# man hat wie bei insertion sort einen sortierten und einen unsortierten bereich

def selection_sort(arr): # T: O(n^2), S: O(1)
    for i in range(len(arr)):
        cur = i
        for j in range(i+1, len(arr)): # man muss nur von i + 1 weg kontrollieren, da wenn keine zahl kleiner ist als i es sich nichts verändert
            if arr[j] < arr[cur]: cur = j
        if cur != i: arr[i], arr[cur] = arr[cur], arr[i]

    return arr

print(selection_sort([2, 32, 12, 23, 2, 23, -2, 23, -4, -21]))