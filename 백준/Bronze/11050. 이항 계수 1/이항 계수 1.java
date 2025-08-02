import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int K = scanner.nextInt();

        long result = factorial(N) / (factorial(K) * factorial(N - K));
        System.out.println(result);
    }

    public static long factorial(int num) {
        if (num <= 1) return 1;
        return num * factorial(num - 1);
    }
}