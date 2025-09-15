import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean isExist = false;

        for (int i = 1; i < n; i++) {
            int sum = i;
            int temp = i;

            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }

            if (sum == n) {
                System.out.println(i);
                isExist = true;
                break;
            }
        }

        if (!isExist) {
            System.out.println(0);
        }
    }
}
