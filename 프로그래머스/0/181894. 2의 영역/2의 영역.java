import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> index = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                index.add(i);
            }
        }
        
        if (index.size() == 0) {
            return new int[] {-1};
        }
        
        if (index.size() == 1) {
            return new int[] {2};
        }
        
        for (int i = index.get(0); i < index.get(index.size() - 1) + 1; i++) {
            answer.add(arr[i]);
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}