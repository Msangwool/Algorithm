import java.util.*;

public class Main {
    static int N, M;
    static List<Integer> result = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        backtrack();
    }

    static void backtrack() {
        if (result.size() == M) {
            for (int num : result) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (result.isEmpty() || result.get(result.size() - 1) <= i) {
                result.add(i);
                backtrack();
                result.remove(result.size() - 1);
            }
        }
    }
}