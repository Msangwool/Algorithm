import java.util.*;

public class Main {
    static StringBuilder stringBuilder = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int sum = (int) Math.pow(2, n) - 1;
        stringBuilder.append(sum).append("\n");

        top(n, 1, 2, 3);

        System.out.println(stringBuilder);
    }

    static void top(int n, int start, int middle, int goal) {
        if (n == 1) {
            stringBuilder.append(start).append(" ").append(goal).append("\n");
        } else {
            top(n - 1, start, goal, middle);
            stringBuilder.append(start).append(" ").append(goal).append("\n");
            top(n - 1, middle, start, goal);
        }
    }
}