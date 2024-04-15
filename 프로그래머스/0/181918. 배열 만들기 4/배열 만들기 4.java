import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        // arr -> stk 로 만들어서 반환
        // i = 0, i < arr.length
        
        // stk.empty()  ->  stk.add(arr[i])  ->   i+1
        // stk.present()  ->  stk.lastIndexOf() < arr[i]  ->  stk.add(arr[i])  ->  i + 1
        // stk.present()  ->  stk.lastIndexOf() >= arr[i]  ->  stk.remove(stk.lastIndexOf())
        
        List<Integer> stk = new ArrayList<>();
        
        int i = 0;
        while (i < arr.length) {
            if (stk.size() == 0) {
                stk.add(arr[i]);
                i++;
                continue;
            }
            
            int lastIndex = stk.size() - 1;
            if (stk.get(lastIndex) < arr[i]) {
                stk.add(arr[i]);
                i++;
            } else {
                stk.remove(lastIndex);
            }
        }
        
        return stk.stream().mapToInt(Integer::intValue).toArray();
    }
}