

'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
from typing import List
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        import collections

        res = collections.defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res[sorted_str].append(string)
        return res.values() 

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            x = ''.join(sorted(i))
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]

        return d.values()

class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        retDict = defaultdict(list)  # key is string's representation, value is list of strings with this representation
        for s in strs:
            retDict["".join(sorted(s))].append(s)

        return list(retDict.values())



test = Solution2()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))