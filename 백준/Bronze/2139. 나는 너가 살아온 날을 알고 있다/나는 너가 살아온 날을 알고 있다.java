import java.util.Scanner;

public class Main {
    
    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] monthDays = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

        while (true) {
            int d = sc.nextInt(); // day
            int m = sc.nextInt(); // month
            int y = sc.nextInt(); // year

            if (d == 0 && m == 0 && y == 0) {
                break;
            }

            int days = 0;

            for (int i = 0; i < m - 1; i++) {
                days += monthDays[i];
            }

            if (isLeapYear(y) && m > 2) {
                days += 1;
            }

            days += d;

            System.out.println(days);
        }

        sc.close();
    }
}