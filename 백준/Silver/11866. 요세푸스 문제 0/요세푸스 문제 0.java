import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            deque.offer(i); 
        }

        List<Integer> result = new ArrayList<>();

        while (!deque.isEmpty()) {
            for (int i = 0; i < K - 1; i++) {
                deque.offer(deque.poll()); 
            }
            result.add(deque.poll()); 
        }

        System.out.print("<");
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i != result.size() - 1) {
                System.out.print(", ");
            }
        }
        System.out.println(">");
    }
}