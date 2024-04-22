import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        Map<Character, Integer> map = new HashMap<>();
        
        for (String key : keymap) {
            for (int i = 1; i <= key.length(); i++) {
                char alphabet = key.charAt(i - 1);
                if (i < map.getOrDefault(alphabet, 101)) {
                    map.put(alphabet, i);
                }
            }
        }
        
        int[] answer = new int[targets.length];
        
        for (int i = 0; i < targets.length; i++) {
            for (int j = 0; j < targets[i].length(); j++) {
                int key = map.getOrDefault(targets[i].charAt(j), -1);
                if (key == -1) {
                    answer[i] = -1;
                    break;
                }
                answer[i] += key;
            }
        }
    
        return answer;
    }
}