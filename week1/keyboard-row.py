class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiop"
        b="asdfghjkl"
        c="zxcvbnm"
        ans=[]
        for i in words:
            s=0
            u=i[0]
            t=0
            if u.lower() in a:
                t="a"
            elif u.lower() in b:
                t="b"
            else:
                t="c"
            for j in i:
                x=0

                if j.lower() in a:
                    x="a"
                elif j.lower() in b:
                    x="b"
                else:
                    x="c"
                if x!=t:
                    s=1
                    break
            if s==0:
                ans.append(i)
              
        return ans