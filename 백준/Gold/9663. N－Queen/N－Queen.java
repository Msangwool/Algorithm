import java.util.*;

public class Main {
    static boolean[] visited1;
    static boolean[] visited2;
    static boolean[] visited3;

    static int cnt = 0;
    static int N;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        visited1 = new boolean[N];
        visited2 = new boolean[N + N];
        visited3 = new boolean[2*(N-1) + 1];

        backtrack(0);

        System.out.println(cnt);
    }

    static void backtrack(int k) {
        if (k == N) {
            cnt += 1;
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!visited1[i] && !visited2[k + i] && !visited3[N - 1 + k - i]) {
                visited1[i] = true;
                visited2[k + i] = true;
                visited3[N - 1 + k - i] = true;
                backtrack(k + 1);
                visited1[i] = false;
                visited2[k + i] = false;
                visited3[N - 1 + k - i] = false;
            }
        }
    }
}