import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        
        int[] arr;
        for (int t = 0; t < commands.length; t++) {
            int i = commands[t][0];
            int j = commands[t][1];
            int k = commands[t][2];
            
            arr = Arrays.copyOfRange(array, i - 1, j);
            Arrays.sort(arr);
            answer.add(arr[k - 1]); 
        }   
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}