class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for (int num : num_list) {
            while (true) {
                if (num == 1) {
                    break;
                }
                num = num / 2;
                answer += 1;
            }
        }
        return answer;
    }
}