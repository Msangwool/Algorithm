class Solution {
    public long solution(int balls, int share) {
        
        long answer = 1;
        
        if (share > balls - share) {
            share = balls - share;
        }
        
        int t = 1;
        for (int i = share; i > 0; i--) {
            answer = answer * (balls - i + 1);
            answer = answer / t;
            t++;
        }
        
        return answer;
    }
    
}