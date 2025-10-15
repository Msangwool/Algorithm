import java.util.*;

public class Main {
    
    static int M;

    static int N;

    static int[][] kimchi;

    static boolean[][] visited;

    static int[][] move = new int[][]{{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            M = sc.nextInt(); // 가로
            N = sc.nextInt(); // 세로
            int K = sc.nextInt(); // 배추 개수

            kimchi = new int[M][N];
            visited = new boolean[M][N];

            for (int j = 0; j < K; j++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                kimchi[x][y] = 1;
            }

            int count = 0;

            for (int x = 0; x < M; x++) {
                for (int y = 0;y < N; y++) {
                    if (kimchi[x][y] == 1 && !visited[x][y]) {
                        dfs(x, y);
                        count++;
                    }
                }
            }

            sb.append(count).append("\n");
        }

        System.out.println(sb);
    }

    static void dfs(int x, int y) {
        visited[x][y] = true;

        for (int[] xy : move) {
            int newX = x + xy[0];
            int newY = y + xy[1];

            if (newX < 0 || newX >= M) {
                continue;
            }

            if (newY < 0 || newY >= N) {
                continue;
            }

            if (kimchi[newX][newY] == 1 && !visited[newX][newY]) {
                dfs(newX, newY);
            }
        }
    }
}