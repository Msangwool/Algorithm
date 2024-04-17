import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        // 4개가 모두 같으면 1111 * x
        // 3개가 같고 다른 q 라고 하면 (10 * p + q) * (10 * p + q)
        // 2개씩 같으면 (p + q) * ((p - q) > 0 ? (p - q) : (p - q) * -1)
        // 2개는 같고 나머지 두개는 틀리면 q * r
        // 모두 다르면 가장 작은 숫자가 정답
        int p = 1;
        int q = 1;
        int r = 1;
        
        Map<Integer, Integer> map = new HashMap<>();
        
        map.put(a, map.getOrDefault(a, 0) + 1);
        map.put(b, map.getOrDefault(b, 0) + 1);
        map.put(c, map.getOrDefault(c, 0) + 1);
        map.put(d, map.getOrDefault(d, 0) + 1);
        
        if (map.containsValue(4)) {
            return 1111 * a;
        }
        
        if (map.containsValue(3)) {
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (entry.getValue() == 3) {
                    p = entry.getKey();
                }
                if (entry.getValue() == 1) {
                    q = entry.getKey();
                }
            }
            return (10 * p + q) * (10 * p + q);
        }
        
        if (map.containsValue(2)) {
            if (map.size() == 2) {
                boolean i = true;
                for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                    if (i) {
                        p = entry.getKey();
                        i = false;
                    } else {
                        q = entry.getKey();
                    }
                }
                return (p + q) * ((p - q) > 0 ? (p - q) : (p - q) * -1);
            }
            
            boolean i = true;
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (i && entry.getValue() == 1) {
                    q = entry.getKey();
                    i = false;
                } else if (entry.getValue() == 1) {
                    r = entry.getKey();
                }
            }
            return q * r;
        }
        
        int answer = 6;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            answer = entry.getKey() < answer ? entry.getKey() : answer;
        }
    
        return answer;
    }
}