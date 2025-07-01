from collections import defaultdict
def groupAnagrams(my_list):
    new = defaultdict(list)
    for words in my_list:
        count = [0] * 26
        for char in words:
            count[ord(char) - ord('a')] += 1
        new[tuple(count)].append(words)
    return list(new.values())
my_list = ['eat', 'tea', 'met', 'team', 'meat']
print(groupAnagrams(my_list))