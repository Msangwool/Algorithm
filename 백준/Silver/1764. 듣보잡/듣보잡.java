import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Set<String> notSee = new HashSet<>();
        Set<String> notListen = new HashSet<>();

        for (int i = 0; i < N; i++) {
            notSee.add(br.readLine().trim());
        }
        for (int i = 0; i < M; i++) {
            notListen.add(br.readLine().trim());
        }

        List<String> list = new ArrayList<>();
        for (String name : notSee) {
            if (notListen.contains(name)) {
                list.add(name);
            }
        }

        Collections.sort(list);

        StringBuilder sb = new StringBuilder();
        sb.append(list.size()).append("\n");
        for (String name : list) {
            sb.append(name).append("\n");
        }
        System.out.print(sb);
    }
}
