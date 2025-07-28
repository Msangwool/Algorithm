import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] A;
    static int[] operators; // +, -, *, /
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        operators = new int[4]; 

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            operators[i] = Integer.parseInt(st.nextToken());
        }

        backtrack(1, A[0]);

        System.out.println(max);
        System.out.println(min);
    }

    public static void backtrack(int idx, int currentValue) {
        if (idx == N) {
            max = Math.max(max, currentValue);
            min = Math.min(min, currentValue);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (operators[i] > 0) {
                operators[i]--;
                backtrack(idx + 1, calculate(currentValue, A[idx], i));
                operators[i]++;
            }
        }
    }

    public static int calculate(int value1, int value2, int op) {
        switch (op) {
            case 0: return value1 + value2; 
            case 1: return value1 - value2; 
            case 2: return value1 * value2; 
            case 3: 
                if (value1 >= 0) return value1 / value2;
                else return -(-value1 / value2); 
        }
        throw new IllegalArgumentException("Invalid operator index");
    }
}