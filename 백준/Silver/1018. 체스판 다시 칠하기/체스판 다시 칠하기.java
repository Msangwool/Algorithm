import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int M = sc.nextInt();
        int N = sc.nextInt();
        sc.nextLine(); 

        char[][] board = new char[M][N];

        for (int i = 0; i < M; i++) {
            board[i] = sc.nextLine().toCharArray();
        }

        int result = Integer.MAX_VALUE;

        for (int i = 0; i <= M - 8; i++) {
            for (int j = 0; j <= N - 8; j++) {
                result = Math.min(result, getRepaintCount(board, i, j));
            }
        }

        System.out.println(result);
    }

    public static int getRepaintCount(char[][] board, int row, int col) {
        int countW = 0; 
        int countB = 0;

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                char expectedW = ((i + j) % 2 == 0) ? 'W' : 'B';
                char expectedB = ((i + j) % 2 == 0) ? 'B' : 'W';

                char actual = board[row + i][col + j];

                if (actual != expectedW) countW++;
                if (actual != expectedB) countB++;
            }
        }

        return Math.min(countW, countB);
    }
}