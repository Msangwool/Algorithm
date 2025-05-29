import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt(); 
        int M = sc.nextInt(); 
        
        boolean[] visited = new boolean[N + 1];
        
        Stack<Integer> result = new Stack<>();
        
        backtrack(result, visited, N, M);
    }
    
    static void backtrack(Stack<Integer> result, boolean[] visited, int N, int M) {
        if (result.size() == M) {
            stackPrinter(result);
            return;
        }
        
        for (int i = 1; i < N + 1; i++) {
            if (!visited[i]) {
                result.add(i);
                visited[i] = true;
                backtrack(result, visited, N, M);
                result.pop();
                visited[i] = false;
            }
        }
    }
    
    static void stackPrinter(Stack<Integer> result) {
        System.out.println(
            result.stream()
                 .map(String::valueOf)
                 .collect(Collectors.joining(" "))
        );
    }
}