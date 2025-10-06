import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        TreeMap<Integer, Integer> tree = new TreeMap<>();
        
        for (int i = 0; i < operations.length; i++) {
            String[] parts = operations[i].split(" ");
            String operation = parts[0];
            int num = Integer.parseInt(parts[1]);
                        
            if (operation.equals("I")) {
                tree.put(num, tree.getOrDefault(num, 0) + 1);
            } else {
                // 연산 무시
                if (tree.isEmpty()) continue;
                
                int key = (num == -1) ? tree.firstKey() : tree.lastKey();
                int value = tree.get(key);
                
                if (value == 1) {
                    tree.remove(key);
                } else {
                    value -= 1;
                    tree.put(key, value);
                }
            }
        }
        
        if (tree.isEmpty()) return new int[] {0, 0};
        return new int[] {tree.lastKey(), tree.firstKey()};
    }
}