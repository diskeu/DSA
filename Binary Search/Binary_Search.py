# Binary Search

# Traditionell und Bedinungsbasiert

# Traditionell
# Binary Search ist algorithmus um eine bestimmte zahl in einem sortierten array zu finden
# Man schaut immer zuerst auf Mitte -> wenn Mitte gesuchte elemet ist dann fertig
# Wenn gesuchte Element kleiner ist sucht man nur in der Linken hälfte weiter
# Wenn größer dann nur in der Rechten hälfte
# Dann widerholt bis das element gefunden wird

# wenn man sortiertes array hat dann kann man immer binary search anwenden z.B. arr = [-5, 3, 2, 1, 3, 6, 9]
# binary search oft verwendet bei lookup ob irgendetwas in einem array ist
# normale Suche wäre O(n) aber bei binary search wird jedesmal der zeitaufwand halbiert
# umkehrung zu O(2**n) -> wächst extrem langsam, bei exponentielle zeit wächst bei jeder weiteren eingabe um doppelte

# 2 Point algorithmus
# wenn man arr = [-5, 3, 2, 1, 3, 6, 7, 9] hat,
#           L ->   0  1  2  3  4  5  6  7<- R
# Left und Right sind die 2 Pointer (Indexe)
# L = 0, R = n-1
# Man sucht immer die Mitte bis das die Mitte die gesuchte Zahl ist,
# wenn man zwei mitten hat weil die n | länge gerade ist, rundet man runter mit floor division
# Mitte = (Links + Rechts) // 2 -> nicht immer neue liste machen und dort die mitte finden weil dann würde es nicht effizient sein
# Mitte = (Links + Rechts) // 2 funktioniert da es zb die mitte von 3 bis 7 hergibt, das 5 ist und da indexe nach der reihe sind ergibt ews dann die mitte
# Mitte ist immer ein Idex
# wenn man dann mitte hat schaut man ob arr[mitte] der gesuchte wert ist, wenn nicht dann schaut man ob mitte größer als wert ist oder kleiner als wert
# wenn mitte kleiner als wert ist dann verschiebt man links zur mitte, also links ist dann die mitte index, sonst ist rechts die mitte
# wenn z.B. nummer größer ist als die Mitte wird die komplette Liste kleiner gemacht und L = m + 1, da L nicht die Mitte sein kann aber auch nicht kleiner als die Mitte
# eine komplette hälfte ist weniger zu suchen
# wenn L gleicher Index wie R ist dann ist (L + R) // 2 immer index von L oder R

# wenn man nach Zahl sucht die es nicht gibt dan wird irgendwann zb L = i0 und R = i1 und M = i2, dann macht man (0 + 1) // 2 und das würde 0 ergeben,
# also macht man R zu 0 - 1 und dann ist Rechts kleiner als Links und darum schreibt man while R >= L
# man benutzt auch L + [(R-L) // 2] um Integer owerflow zu vermeiden da dann keine so große zahl wie sonst entsteht, z.B. wenn L und R nebeneinander liegen und sehr große zahlen sind

# wenn man bereich von index L bis index R hat dann ist die länge des berreiches R - L + 1
# um die mitte eines berreiches zu bekommen muss man den berreich durch 2 dividieren in demm fall // um abzurunden
# man kann auch sagen Mitte liegt halb so weit vom Linken ende entfernt -> Mitte = L + Breite des berreiches // 2
# Die Breite des Bereichs = R - L
# 	•	Beispiel: L=3, R=7 → Breite = 7-3 = 4
# 	•	Hälfte davon: (R-L)//2 = 4//2 = 2
# 	•	Addiere das zum linken Index: L + 2 = 5 → genau die Mitte
# oder man nimmt rechter Index plus linker Index durch 2
	# •	(R-L)//2 = Abstand von L zur Mitte
	# •	Addiere L → Index der Mitte im Originalarray

def search(ol, num) -> int: # -> returnt immer Links zuerst
    L = 0
    R = len(ol) - 1
    while R >= L:
        mid = (L + R) // 2
        if ol[mid] == num: return mid
        elif ol[mid] < num: L = mid + 1
        else: R = mid - 1
    return False

print(search([-5, 3, 2, 1, 3, 6, 7, 9], 9))

# Ower under methode / condition based

# wird bei bugs verwendet wie in git bei git biscet
# z.B. du hast eine commit histiorie und ab einem punkt merkt man das ein bug da ist
# um zu prüfen seit wann er existiert nimmt man immer die mitte und prüft ob er da schon existierte

# [T, T, T, T, F, F, F]
#  0  1  2  3  4  5  6
# geht solange ab einem punkt True oder False ist

# man startet bei Mitte und prüft ob True oder False, wenn True dann setzt man L zu mid + 1
# wenn dann False ist setzt man R zu mid da man nicht sicher ist ob es das erste False ist darum auch nicht mid - 1
# L ist nie hinter einem False -> Bereich wird eingegränzt
# wenn R == L dann muss algorithmus returnen

def condition_Search(l) -> int:
    Left = 0
    Right = len(l) - 1
    while Right > Left:
        mid = (Left + Right) // 2
        if l[mid]: Left = mid + 1
        else: Right = mid
    return Left # | Right

l = [True, True, True, False]

print(condition_Search(l))

# Time Space Complexity

# Bei jeder Binary Search gleich
# Schneller als wie O(n), da man nicht alle werte durchsucht
# bei recursion macht jedes element zwei neue bis zu base case
# bei binary search macht jede liste auch zwei neue bis zu base case, aber die neuen listen sind um die hälfte kleiner
# bei binary search macht jede verdoppelung von n nur eine neuen case den es überprüfen muss
# bei recursion macht jedes neue element eine 2**n ebenen also zb bei 3 ebenen sind auf den leaves 4 elemente
# binary search wächst am anfang schnell dann immer langsamer weil bis zu einer neuen ebene n immer verdoppelt werden muss
# bei recursion wächst am anfang langsam dann schnell da man immer 2**n machen muss

# bei binary search wird jedes mal der search space bei jedem neuen case halbiert
# Time complexity ist O(log2n)
# Space complexity ist O(1) da man immer nur 3 werte speichert

