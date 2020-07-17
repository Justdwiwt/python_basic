class Solution:
    @staticmethod
    def countAndSay(n: int) -> str:
        res = ["", "1"]
        if n == 1:
            return res[1]
        for i in range(2, n + 1):
            p = []
            s = ""
            for x in res[i - 1]:
                if p == [] or x == p[0]:
                    p.append(x)
                else:
                    s += str(len(p))
                    s += p[0]
                    p = [x]
            s += str(len(p))
            s += p[0]
            res.append(s)
        return res[n]
