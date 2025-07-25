from collections import Counter
def topKFrequent(nums, k):
    count = Counter(nums)
    most_common = count.most_common(k)
    result = [num for num, freq in most_common]
    return result

print(topKFrequent([1, 2,3 , 4, 3, 3, 5, 5, 2], 3))
