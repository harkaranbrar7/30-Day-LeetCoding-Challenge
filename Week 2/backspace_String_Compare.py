'''
Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''

class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def sim(S):
            ans = ''
            for c in S:
                if c == '#':
                    if len(ans) > 0: ans = ans[:-1]
                else:
                    ans += c
            return ans
        return sim(S) == sim(T)

class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS, stackT = [], []
        for s in S:
            if s != "#":
                stackS.append(s)
            elif stackS:
                stackS.pop()
        for t in T:
            if t != "#":
                stackT.append(t)
            elif stackT:
                stackT.pop()
        return stackS == stackT

class Solution3:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ans_S = ""
        ans_T = ""
        for s in S:
            if s == '#':
                if ans_S:
                    ans_S = ans_S[:-1]
            else:
                ans_S += s
        for t in T:
            if t == '#':
                if ans_T:
                    ans_T = ans_T[:-1]
            else:
                ans_T += t
        return ans_S == ans_T


test = Solution3()
print(test.backspaceCompare("a##c","#a#c"))