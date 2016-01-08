def binarySearch(listy, target):
    mini = 0
    maxi = len(listy) - 1
    for i in listy:
        mid = maxi//2
        if listy[mid] == target:
            return listy.index(target)
        elif i == target:
            return listy.index(target)
        elif listy[mid] < i:
            mini = mid + 1
        elif listy[mid] > i:
            maxi = mid - 1



print(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 12))
print(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 4))
