import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Integer[] convertedCitations = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(convertedCitations, Collections.reverseOrder());
        
        int h = 0;
        for (int i = 0; i < convertedCitations.length; i++) {
            if (h + 1 > convertedCitations[i]) {
                break;
            }
            h++;
        }
        return h;
    }
}