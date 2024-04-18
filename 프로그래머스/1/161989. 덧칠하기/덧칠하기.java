class Solution {
    public int solution(int n, int m, int[] section) {
        
        int answer = 0;
        int t = section[0];
        
        for (int i : section) {

            if (t <= i) {
                t = i;
                t += m;
                answer++;
            }
        }
        
        return answer;
    }
}