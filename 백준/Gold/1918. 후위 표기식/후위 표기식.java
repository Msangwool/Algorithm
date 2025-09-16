import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        Stack<Character> stack = new Stack<>();
        Map<Character, Integer> priority = new HashMap<>();
        priority.put('+', 1);
        priority.put('-', 1);
        priority.put('*', 2);
        priority.put('/', 2);
        priority.put('(', 0);

        StringBuilder result = new StringBuilder();

        for (char c : input.toCharArray()) {
            if (Character.isLetter(c)) { 
                result.append(c);
                continue;
            }

            if (c == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    result.append(stack.pop());
                }
                stack.pop();
                continue;
            }

            if (c == '(') {
                stack.push(c);
                continue;
            }

            while (!stack.isEmpty() && priority.get(c) <= priority.get(stack.peek())) {
                result.append(stack.pop());
            }
            stack.push(c);
        }

        while (!stack.isEmpty()) {
            result.append(stack.pop());
        }

        System.out.println(result.toString());
    }
}
