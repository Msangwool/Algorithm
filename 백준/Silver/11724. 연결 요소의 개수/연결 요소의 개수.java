import java.util.*;

public class Main {
    static int N;
    static int count;
    static int[][] graph;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] nm = scanner.nextLine().split(" ");
        N = Integer.parseInt(nm[0]);

        graph = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < Integer.parseInt(nm[1]); i++) {
            String[] uv = scanner.nextLine().split(" ");
            int u = Integer.parseInt(uv[0]);
            int v = Integer.parseInt(uv[1]);

            graph[u][v] = 1;
            graph[v][u] = 1;
        }

        for (int i = 1; i < N + 1; i++) {
            if (!visited[i]) {
                dfs(i);
                count++;
            }
        }

        System.out.print(count);
    }

    static void dfs(int node) {
        visited[node] = true;

        for (int j = 1; j < N + 1; j++) {
            if (graph[node][j] == 1 && !visited[j]) {
                dfs(j);
            }
        }
    }
}