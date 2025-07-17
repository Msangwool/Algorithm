import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int idx = 1;
        int N = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] l = new int[N];
        for (int i = 0; i < N; i++) {
            l[i] = Integer.parseInt(st.nextToken());
        }
        
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < N; i++) {
            int person = l[i];
            
            if (person != idx) {
                stack.push(person);
                continue;
            }
            
            idx++;
            
            while (!stack.isEmpty() && stack.peek() == idx) {
                stack.pop();
                idx++;
            }
        }
        
        if (stack.isEmpty()) {
            System.out.println("Nice");
        } else {
            System.out.println("Sad");
        }
    }
}