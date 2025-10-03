import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int pricesLen = prices.length;
        int[] answer = new int[pricesLen];
        
        Stack<Integer> stack = new Stack<>();
        
        // 1. 각 인덱스에 맞게 걸린 시간을 계산해야 함
        // 2. stack을 써서 while로 비어질 때까지 계산하면서 기존에 들어있던 애가 더 크면 걔는 점수가 떨어진 것
        // 3. stack에 저장하는 값은 해당 값이 아니라 인덱스를 저장해야 함
        //    - 인덱스로 저장해야 해당 인덱스에 지난 초과 시간을 저장할 수 있음
        
        // 반복
        for (int i = 0; i < pricesLen; i++) {
            // while 돌면서 stack이 없을 떄까지 돌아야 함. 즉, 비어있으면 계속 돌아야 함
            // 추가로 스택이 현재보다 큰지를 검사해야 함, 크면 걔는 빼고 그 인덱스로 숫자 넣어줘야 함
            // 즉, 반대로 작을때
            while (!stack.empty() && prices[stack.peek()] > prices[i]) {
                int j = stack.pop(); // 가격이 떨어진 인덱스
                // 떨어진 시간은 j부터 i까지 센기간
                answer[j] = i - j;
            }
            stack.push(i);
        }
        
        // 마지막까지 초가 떨어지지 않은 애들은 추가를 해줘야 함
        while (!stack.empty()) {
            int j = stack.pop();
            answer[j] = pricesLen - j - 1; // 길이는 인덱스보다 1이 크니까 -1을 해줘야 함
        }
        return answer;
    }
}