def find_group_anagrams(strs):
    visited = [False] * len(strs)
    ans = []

    for i in range(len(strs)):
        if visited[i]:
            continue
        subAns = [strs[i]]
        visited[i] = True
        for j in range(i + 1, len(strs)):
            if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                subAns.append(strs[j])
                visited[j] = True
        ans.append(subAns)

    return ans

print(find_group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

from collections import defaultdict
def another_sove(strs):
    anagrams = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())


