import java.util.*;

public class Main {

    static int[][] board = new int[9][9];
    static List<int[]> emptyCells = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                board[i][j] = sc.nextInt();
                if (board[i][j] == 0) {
                    emptyCells.add(new int[]{i, j});
                }
            }
        }

        solve(0);
    }

    static void solve(int cnt) {
        if (cnt == emptyCells.size()) {
            printBoard();
            System.exit(0);
        }

        int[] cell = emptyCells.get(cnt);
        int x = cell[0];
        int y = cell[1];

        for (int i = 1; i <= 9; i++) {
            if (isValid(x, y, i)) {
                board[x][y] = i;
                solve(cnt + 1);
                board[x][y] = 0;
            }
        }
    }

    static boolean isValid(int x, int y, int num) {
        for (int i = 0; i < 9; i++) {
            if (board[x][i] == num) return false;
        }

        for (int i = 0; i < 9; i++) {
            if (board[i][y] == num) return false;
        }

        int startX = (x / 3) * 3;
        int startY = (y / 3) * 3;
        for (int i = startX; i < startX + 3; i++) {
            for (int j = startY; j < startY + 3; j++) {
                if (board[i][j] == num) return false;
            }
        }

        return true;
    }

    static void printBoard() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }
}