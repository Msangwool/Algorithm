import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] l = {25, 10, 5, 1};
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();  
        for (int j = 0; j < t; j++) {
            int C = sc.nextInt();
            for (int i : l) {
                System.out.print(C / i + " ");
                C = C % i;
            }
            System.out.println();
        }
        sc.close();
    }
}
