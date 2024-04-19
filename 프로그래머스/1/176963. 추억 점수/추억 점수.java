import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        Map<String, Integer> map = new HashMap<>();
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < name.length; i++) {
            map.put(name[i], yearning[i]);
        }
        
        for (int i = 0; i < photo.length; i++) {
            int sum = 0;
            for (String str : photo[i]) {
                sum += map.getOrDefault(str, 0);
            }
            answer.add(sum);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}