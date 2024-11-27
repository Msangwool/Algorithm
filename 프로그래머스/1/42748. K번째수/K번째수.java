import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        
        int[] arr;
        for (int t = 0; t < commands.length; t++) {
            int i = commands[t][0];
            int j = commands[t][1];
            int k = commands[t][2];
            arr = new int[j - i + 1];
            
            int q = 0;
            for (int p = i; p < j + 1; p++) {
                arr[q] = array[p - 1];
                q++;
            }
            
            Arrays.sort(arr);

            answer.add(arr[k - 1]); 
        }   
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}