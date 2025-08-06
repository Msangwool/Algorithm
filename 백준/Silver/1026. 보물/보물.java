import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];
        Integer[] B = new Integer[N];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        for (int i = 0; i < N; i++) {
            B[i] = sc.nextInt();
        }

        Arrays.sort(A); 

        Integer[] BIndices = new Integer[N];
        for (int i = 0; i < N; i++) {
            BIndices[i] = i;
        }

        Arrays.sort(BIndices, (i, j) -> B[j] - B[i]); 

        int S = 0;
        for (int i = 0; i < N; i++) {
            S += A[i] * B[BIndices[i]];
        }

        System.out.println(S);
    }
}