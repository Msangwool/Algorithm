import java.math.BigInteger;
import java.util.Scanner;

public class Main {

    public static BigInteger factorial(int n) {
        if (n <= 1) {
            return BigInteger.ONE;
        }
        return BigInteger.valueOf(n).multiply(factorial(n - 1));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        BigInteger tg = factorial(N);

        String str = tg.toString();
        int cnt = 0;
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) != '0') {
                break;
            }
            cnt++;
        }

        System.out.println(cnt);
    }
}
