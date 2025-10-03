import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        // PriorityQueue
        for (int v : scoville) {
            pq.offer(v);
        }
        
        // pg의 숫자가 2일때까지 또는 가장 작은 수가 k보다 큰 경우
        while (pq.peek() < K) {
            if (pq.size() < 2) {
                return -1;
            }
            answer++;
            pq.offer(pq.poll() + (pq.poll() * 2));
        }
        
        return answer;
    }
}