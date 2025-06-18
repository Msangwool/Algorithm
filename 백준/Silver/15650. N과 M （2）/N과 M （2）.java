import java.util.*;

public class Main {
    static int N, M;
    static boolean[] visited;
    static List<Integer> result = new ArrayList<>();
    static Set<String> seen = new HashSet<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        visited = new boolean[N + 1];

        backtrack();
    }

    static void backtrack() {
        if (result.size() == M) {
            List<Integer> sorted = new ArrayList<>(result);
            Collections.sort(sorted);
            String key = sorted.toString(); // e.g. [1, 2, 3]

            if (seen.contains(key)) return;

            seen.add(key);
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i));
                if (i != result.size() - 1) System.out.print(" ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result.add(i);
                backtrack();
                result.remove(result.size() - 1);
                visited[i] = false;
            }
        }
    }
}