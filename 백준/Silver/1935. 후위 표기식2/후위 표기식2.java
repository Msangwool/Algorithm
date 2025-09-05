import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static double calculate(double num1, double num2, char operator) {
        switch (operator) {
            case '+': return num2 + num1;
            case '-': return num2 - num1;
            case '*': return num2 * num1;
            case '/': return num2 / num1;
            default: throw new IllegalArgumentException("Invalid operator: " + operator);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); 
        sc.nextLine();       

        String expression = sc.nextLine();
        int[] values = new int[N];      

        for (int i = 0; i < N; i++) {
            values[i] = sc.nextInt();    
        }

        Stack<Double> stack = new Stack<>();

        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);

            if (Character.isUpperCase(c)) {
                stack.push((double) values[c - 'A']);
            } else {
                double num1 = stack.pop();
                double num2 = stack.pop();
                double result = calculate(num1, num2, c);
                stack.push(result);
            }
        }

        System.out.printf("%.2f\n", stack.pop());
    }
}
