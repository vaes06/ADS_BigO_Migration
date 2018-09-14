
def BinarySearch(numberlist, needle, min, max):
    midpoint = int((max + min) / 2)
    if (len(numberlist) > 0 and numberlist[midpoint] == needle):
        return midpoint
    if min >= max:
        return
    if numberlist[midpoint] > needle:
        return BinarySearch(numberlist, needle, min, midpoint-1)
    return BinarySearch(numberlist, needle, midpoint+1, max)

numberlist = [1, 3, 3, 7, 10, 11, 16, 17, 20, 21, 25, 26, 30, 32, 34 , 35]
needle = 32
min = 0

position = BinarySearch(numberlist, needle, min,len(numberlist))
print("Position:", position+1)