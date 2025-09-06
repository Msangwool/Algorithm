import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            String input = sc.nextLine();
            
            if (input.equals("# 0 0")) {
                break;
            }

            String[] parts = input.split(" ");
            String name = parts[0];
            int age = Integer.parseInt(parts[1]);
            int weight = Integer.parseInt(parts[2]);

            if (age > 17 || weight >= 80) {
                System.out.println(name + " Senior");
            } else {
                System.out.println(name + " Junior");
            }
        }

        sc.close();
    }
}
