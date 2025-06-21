import java.util.*;

public class Main {
    static int N, M;
    static int[] result;
    static StringBuilder sb;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        N = sc.nextInt(); 
        M = sc.nextInt(); 
        
        sb = new StringBuilder();
        result = new int[M];
        
        backtrack(0);
        
        System.out.print(sb);
    }
    
    static void backtrack(int depth) {
        if (depth == M) {
            printer();
            return;
        }
        
        for (int i = 1; i < N + 1; i++) {
            result[depth] = i;
            backtrack(depth + 1);
        }
    }
    
    static void printer() {
        for (int i = 0; i < M; i++) {
            sb.append(result[i]).append(" ");
        }
        sb.append("\n");
    }
}