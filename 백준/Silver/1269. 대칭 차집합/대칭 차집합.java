import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int l_a = Integer.parseInt(st.nextToken());
        int l_b = Integer.parseInt(st.nextToken());
        
        Set<Integer> a = new HashSet<>();
        Set<Integer> b = new HashSet<>();
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < l_a; i++) {
            a.add(Integer.parseInt(st.nextToken()));
        }
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < l_b; i++) {
            b.add(Integer.parseInt(st.nextToken()));
        }
        
        Set<Integer> diffA = new HashSet<>(a);
        diffA.removeAll(b);
        
        Set<Integer> diffB = new HashSet<>(b);
        diffB.removeAll(a);
        
        System.out.println(diffA.size() + diffB.size());
    }
}
