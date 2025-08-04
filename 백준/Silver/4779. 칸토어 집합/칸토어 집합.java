import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextInt()) {
            int N = scanner.nextInt();
            int length = (int) Math.pow(3, N);
            char[] arr = new char[length];

            for (int i = 0; i < length; i++) {
                arr[i] = '-';
            }

            cantor(arr, 0, length);
            System.out.println(new String(arr));
        }

        scanner.close();
    }

    public static void cantor(char[] arr, int start, int length) {
        if (length <= 1) return;

        int third = length / 3;
        int midStart = start + third;

        for (int i = midStart; i < midStart + third; i++) {
            arr[i] = ' ';
        }

        cantor(arr, start, third);
        cantor(arr, midStart + third, third);
    }
}