import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int A = sc.nextInt();
        int B = sc.nextInt();
        int gcd;
        int lcm;
        if (A > B) {
            gcd = getGcd(A, B);
        } else {
            gcd = getGcd(B, A);
        }
        
        lcm = (A * B) / gcd;
            
        System.out.println(gcd);
        System.out.println(lcm);
    }
    
    static int getGcd(int a, int b) {
        if (a % b == 0) {
            return b;
        }  
        return getGcd(b, a % b);
    }
}