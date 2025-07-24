import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int N = Integer.parseInt(parts[0]);
        int M = Integer.parseInt(parts[1]);

        Map<Integer, String> numToName = new HashMap<>();
        Map<String, Integer> nameToNum = new HashMap<>();

        for (int i = 1; i <= N; i++) {
            String name = br.readLine().trim();
            numToName.put(i, name);
            nameToNum.put(name, i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            String target = br.readLine().trim();
            if (isNumeric(target)) {
                int num = Integer.parseInt(target);
                sb.append(numToName.get(num)).append("\n");
            } else {
                sb.append(nameToNum.get(target)).append("\n");
            }
        }

        System.out.print(sb);
    }

    private static boolean isNumeric(String s) {
        return s.matches("\\d+");
    }
}