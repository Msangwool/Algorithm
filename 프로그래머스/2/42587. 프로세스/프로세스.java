import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
                
        Queue<Integer> q = new LinkedList<>();
        
        Map<Integer, Integer> countMap = new HashMap<>();
        Set<Integer> sortedMin = new HashSet<>();
        
        for (int i : priorities) {
            q.add(i);
            sortedMin.add(i);
            countMap.put(i, countMap.getOrDefault(i, 0) + 1);
        }
        
        List<Integer> sortedList = new ArrayList<>(sortedMin);
        Collections.sort(sortedList, Collections.reverseOrder());
        
        int i = 0;
        
        while (true) {
            
            if (countMap.get(sortedList.get(i)) == 0) {
                i++;
            }
            
            if (sortedList.get(i) == q.peek()) {
                int pollQ = q.poll();
                answer++;
                countMap.put(pollQ, countMap.get(pollQ) - 1);
                
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