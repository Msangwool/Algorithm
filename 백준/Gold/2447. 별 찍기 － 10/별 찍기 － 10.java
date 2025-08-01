import java.util.*;

public class Main {
    static int N;
    static List<String> init = Arrays.asList(
        "***",
        "* *",
        "***"
    );

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        List<String> result = rep(3, init);
        for (String line : result) {
            System.out.println(line);
        }
    }

    public static List<String> rep(int n, List<String> arr) {
        if (n == N) {
            return arr;
        }

        List<String> tmp = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            tmp.add(arr.get(i) + arr.get(i) + arr.get(i));
        }

        for (int i = 0; i < arr.size(); i++) {
            tmp.add(arr.get(i) + " ".repeat(n) + arr.get(i));
        }

        for (int i = 0; i < arr.size(); i++) {
            tmp.add(arr.get(i) + arr.get(i) + arr.get(i));
        }

        return rep(n * 3, tmp);
    }
}