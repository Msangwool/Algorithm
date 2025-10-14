import java.util.*;

public class Main {
    
    static int N;

    static int[][] apartment;

    static boolean[][] visited;

    static int[][] move = new int[][]{{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

    static int count;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        sc.nextLine();

        apartment = new int[N][N];
        visited = new boolean[N][N];

        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < N; j++) {
                apartment[i][j] = line.charAt(j) - '0';
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (apartment[i][j] == 1 && !visited[i][j]) {
                    count = 0;
                    dfs(i, j);
                    answer.add(count);
                }
            }
        }

        Collections.sort(answer);
        StringBuilder sb = new StringBuilder();
        sb.append(answer.size()).append("\n");
        for (Integer integer : answer) {
            sb.append(integer).append("\n");
        }
        System.out.print(sb);
    }

    static void dfs(int x, int y) {
        count++;
        visited[x][y] = true;

        for (int[] xy : move) {
            int newX = x + xy[0];
            int newY = y + xy[1];

            if (newX < 0 || newX >= N) {
                continue;
            }

            if (newY < 0 || newY >= N) {
                continue;
            }

            if (apartment[newX][newY] == 1 && !visited[newX][newY]) {
                dfs(newX, newY);
            }
        }
    }
}