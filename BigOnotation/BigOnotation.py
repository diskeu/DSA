# gibt an wie Laufzeit eines Algorythmus sic vergrösert, wenn die eingabegröße (N) grrößer wird
# O(n) - bleibt Konstant
# O(n^2) - Laufzeit quadriert sich
# O(log n) - jede verdopplung eingabe, braucht extra schritt

# BigO = wächst die funktion mit n?
# O(26) = O(1), 

a: list = [1, 2, 3, 4,]
b: list = []
def square(arr) -> list: # Time complexity of O(n)
    for x in a:
        b.append(x**2)
    return b
# print(square(a))

a: list = [1, 2, 3, 4,]
def compare(arr): # Time complexity of O(n^2)
    for x in arr:
        for y in arr:
            print(x, y)
# compare(a)

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Middle index
        if arr[mid] == target:
            return mid  # Element found, return index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Element not found

l = [1, 2, 3, 4, 5, 6, 7, 8, 12, 32, 39, 41]
print(binarySearch(l, 32))