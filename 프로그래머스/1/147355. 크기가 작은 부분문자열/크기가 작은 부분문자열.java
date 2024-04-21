class Solution {
    public int solution(String t, String p) {
        
        boolean isSuccess;
        int answer = 0;
        
        for (int i = 0; i < t.length() - p.length() + 1; i++) {
            isSuccess = true;
            for (int j = 0; j < p.length(); j++) {
                if (t.charAt(i + j) > p.charAt(j)) {
                    isSuccess = false;
                    break;
                } else if (t.charAt(i + j) < p.charAt(j)) {
                    break;
                }
            }
            if (isSuccess) {
                answer++;
            }
        }
        return answer;
    }
}