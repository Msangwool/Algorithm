import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
                
        Queue<Integer> q = new LinkedList<>();
        
        for (int i : priorities) {
            q.add(i);
        }
        
        Arrays.sort(priorities);
            
        int i = priorities.length - 1;
        
        while (true) {
                        
            if (priorities[i] == q.peek()) {
                q.poll();
                
                i--;
                answer++;
                location--;
                
                if (location < 0) break;
            
                continue;
            }
            
            q.add(q.poll());
            
            location--;
            if (location < 0) location = q.size() - 1;
        }
    
        return answer;
    }
}