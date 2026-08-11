class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans=0
        carry=0
        for i in range(32):
            x=(a>>i)&1
            y=(b>>i)&1
            bit=x^y^carry
            carry=(x&y)|(x&carry)|(y&carry)
            ans|=bit<<i
        if ans>>31:
            ans=~(ans^0xFFFFFFFF)
        return ans