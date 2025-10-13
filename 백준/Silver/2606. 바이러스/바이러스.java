import java.util.*;

public class Main {
    
    static int N;

    static int M;

    static int[][] graph;

    static boolean[] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        N = scanner.nextInt();
        M = scanner.nextInt();

        graph = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < M; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        dfs(1);

        int count = 0;
        for (int i =1; i <= N; i++) {
            if (visited[i]) {
                count++;
            }
        }

        System.out.println(count - 1);
    }

    static void dfs(int node) {
        visited[node] = true;

        for (int next = 1; next <= N; next++) {
            if (graph[node][next] == 1 && !visited[next]) {
                dfs(next);
            }
        }
    }
}