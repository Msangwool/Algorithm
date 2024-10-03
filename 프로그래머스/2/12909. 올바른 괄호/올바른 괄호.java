import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();  
        
        // Case 1
        // Stack에 닫히지 않은 괄호가 없는 경우
        // -> ')' 기호인 경우에 Stack size가 0인 경우

        // Case 2
        // Stack에 닫히지 않은 괄호가 남는 경우
        // -> s를 모두 반복했음에도 Stack size가 0 이상인 경우
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            } else {
                // Case 1
                if (stack.size() == 0) {
                    return false;
                }
                
                stack.pop();
            }
        }
        
        // Case 2
        if (stack.size() > 0) {
            return false;
        }

        return true;
    }
}