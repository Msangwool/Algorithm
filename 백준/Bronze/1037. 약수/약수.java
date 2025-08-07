import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int cnt = sc.nextInt();  
        int[] arr = new int[cnt];

        for (int i = 0; i < cnt; i++) {
            arr[i] = sc.nextInt();
        }

        int min = arr[0];
        int max = arr[0];

        for (int i = 1; i < cnt; i++) {
            if (arr[i] < min) min = arr[i];
            if (arr[i] > max) max = arr[i];
        }

        System.out.println(min * max);
    }
}