import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String vowels = "aeiouAEIOU";

        while (true) {
            String line = sc.nextLine();
            if (line.equals("#")) {
                break;
            }

            int count = 0;
            for (char ch : line.toCharArray()) {
                if (vowels.indexOf(ch) != -1) { 
                    count++;
                }
            }

            System.out.println(count);
        }
        sc.close();
    }
}
