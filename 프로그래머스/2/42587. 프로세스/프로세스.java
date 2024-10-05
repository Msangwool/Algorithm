import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
                
        Queue<Integer> q = new LinkedList<>();
        
        Map<Integer, Integer> remainMinNum = new HashMap<>();
        Set<Integer> minNum = new HashSet<>();
        
        for (int i : priorities) {
            q.add(i);
            minNum.add(i);
            remainMinNum.put(i, remainMinNum.getOrDefault(i, 0) + 1);
        }
        
        List<Integer> sortedMinNum = new ArrayList<>(minNum);
        Collections.sort(sortedMinNum, Collections.reverseOrder());
        
        int i = 0;
        
        while (true) {
            
            if (remainMinNum.get(sortedMinNum.get(i)) == 0) {
                i++;
            }
            
            if (sortedMinNum.get(i) == q.peek()) {
                int pollQ = q.poll();
                answer++;
                remainMinNum.put(pollQ, remainMinNum.get(pollQ) - 1);
                
                if (location == 0) {
                    break;
                }
                
                location--;
                continue;
            }
            
            q.add(q.poll());
            
            location--;
            if (location < 0) {
                location = q.size() - 1;
            }
        }
    
        return answer;
    }
}