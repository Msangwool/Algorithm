import java.util.Scanner;

public class Main {

    public static int GCD(int a, int b) {
        if (a % b == 0) {
            return b;
        }
        return GCD(b, a % b);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();  

        for (int i = 0; i < t; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            int gcd = (a > b) ? GCD(a, b) : GCD(b, a);  
            int lcm = (a * b) / gcd; 

            System.out.println(lcm);
        }

        scanner.close();
    }
}
