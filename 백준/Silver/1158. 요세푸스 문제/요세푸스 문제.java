import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            q.offer(i);
        }

        List<Integer> result = new ArrayList<>();

        while (!q.isEmpty()) {
            for (int i = 0; i < K - 1; i++) {
                q.offer(q.poll()); 
            }
            result.add(q.poll()); 
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i));
            if (i != result.size() - 1) {
                sb.append(", ");
            }
        }
        sb.append(">");

        System.out.println(sb);
    }
}
