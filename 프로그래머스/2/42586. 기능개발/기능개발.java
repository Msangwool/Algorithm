import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        
        int[] deployDays = new int[progresses.length];
        
        for (int i = 0; i < progresses.length; i++) {
            int remainProgress = 100 - progresses[i];
            
            deployDays[i] = 
                remainProgress % speeds[i] == 0 
                ? remainProgress / speeds[i] 
                : remainProgress / speeds[i] + 1;
        }
        
        int count = 0;
        
        for (int i = 0; i < deployDays.length; i++) {
            if (stack.size() == 0) {
                stack.push(deployDays[i]);
                count = 1;
                continue;
            }
                
            if (deployDays[i] <= stack.peek()) {
                count++;
            } else {
                answer.add(count);
                count = 1;
                stack.push(deployDays[i]);
            }
        }
        answer.add(count);
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}