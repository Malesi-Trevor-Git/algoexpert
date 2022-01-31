def twoNumberSum(array, target):
    for i in range(len(array) - 1):
        first = array[i]
        for j in range(i + 1, len(array)):
            second = array[j]
            if first + second == target:
                return [first, second]
    return []


array = [1, 2, 3, 4, 5, 6, 7]
target = 3
print(twoNumberSum(array, target))


def twoNumberHash(array, target):
    nums = {}
    for i in array:
        if target - i in nums:
            return [target - i, i]
        else:
            nums[i] = True
    return []


print(twoNumberHash(array, target))
