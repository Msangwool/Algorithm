import java.util.*;

public class Solution {
    public int[] solution(int []arr) {        
        List<Integer> answer = new ArrayList<>();
        
        Stack<Integer> stack = new Stack<>();
        
        
        answer.add(arr[0]);
        stack.push(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if (stack.peek() == arr[i]) {
                continue;
}
            answer.add(arr[i]);
            stack.push(arr[i]);
}

        return answer.stream().mapToInt(i->i).toArray();
    }
}