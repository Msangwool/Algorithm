import java.util.*;
import java.io.*;

public class Main {
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    public static int gcdList(List<Integer> nums) {
        int result = nums.get(0);
        for (int i = 1; i < nums.size(); i++) {
            result = gcd(result, nums.get(i));
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        List<Integer> diffs = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int ai = Integer.parseInt(st.nextToken());
            diffs.add(Math.abs(ai - s));
        }

        System.out.println(gcdList(diffs));
    }
}