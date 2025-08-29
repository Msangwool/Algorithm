import java.util.Scanner;

public class Main {

    public static int GCD(int a, int b) {
        if (b == 0) return a;
        return GCD(b, a % b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A1 = sc.nextInt();
        int B1 = sc.nextInt();
        int A2 = sc.nextInt();
        int B2 = sc.nextInt();

        int lcm;
        if (B1 > B2) {
            lcm = B1 * B2 / GCD(B1, B2);
        } else {
            lcm = B1 * B2 / GCD(B2, B1);
        }

        int A = (lcm / B1) * A1 + (lcm / B2) * A2;

        int gcd;
        if (A > lcm) {
            gcd = GCD(A, lcm);
        } else {
            gcd = GCD(lcm, A);
        }

        System.out.println((A / gcd) + " " + (lcm / gcd));

        sc.close();
    }
}
