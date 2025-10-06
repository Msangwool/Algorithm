import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        TreeMap<Integer, Integer> map = new TreeMap<>();
        
        for (int i = 0; i < operations.length; i++) {
            String[] parts = operations[i].split(" ");
            String operation = parts[0];
            int num = Integer.parseInt(parts[1]);
            
            if (operation.equals("I")) {
                // insert 되는 값을 key로 삽입, 들어오는 갯수를 value로 삽입
                map.put(num, map.getOrDefault(num, 0) + 1);
            } else if (operation.equals("D")) {
                if (map.isEmpty()) continue;
                
                int key = (num == 1) ? map.lastKey() : map.firstKey();
                // -1 하기 전의 value가 1이면 제거
                if (map.put(key, map.get(key) - 1) == 1) {
                    map.remove(key);
                }
            }
        }
        
        if (map.isEmpty()) return new int[]{0, 0};
        return new int[]{map.lastKey(), map.firstKey()};
    }
}