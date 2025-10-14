import java.util.*;

public class Main {
    
    static int[][] island;

    static boolean[][] visited;

    static int w;

    static int h;

    static int[][] move = new int[][]{{1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int count;

        while (true) {
            w = sc.nextInt();
            h = sc.nextInt();

            if (w + h == 0)  {
                break;
            }

            island = new int[h][w];
            visited = new boolean[h][w];

            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    island[i][j] = sc.nextInt();
                }
            }

            count = 0;

            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (island[i][j] == 1 && !visited[i][j]) {
                        dfs(i, j);
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
            if (0 > newX || newX >= h) {
                continue;
            }

            if (0 > newY || newY >= w) {
                continue;
            }

            if (island[newX][newY] == 1 && !visited[newX][newY]) {
                dfs(newX, newY);
            }
        }
    }
}