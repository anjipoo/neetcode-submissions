class Solution {
    public int getSum(int a, int b) {
        int ans=0;
        int carry=0;
        for(int i=0; i<32; i++) {
            int x=(a>>i)&1;
            int y=(b>>i)&1;
            int bit=x^y^carry;
            carry=(x&y)|(x&carry)|(y&carry);
            ans|=bit<<i;
        }
        if((ans>>31)!=0) {
            ans=~(ans^0xFFFFFFFF);
        }
        return ans;
    }
}
