import java.util.*;

class Solution {
    public int[] solution(int n, int k) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 1; i * k <= n; i++) {
            answer.add(i * k);
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}