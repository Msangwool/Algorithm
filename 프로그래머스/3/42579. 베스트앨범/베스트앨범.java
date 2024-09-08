import java.util.*;

class Solution {
    public List<Integer> solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        Map<String, Integer> genresMap = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            genresMap.put(genres[i], genresMap.getOrDefault(genres[i], 0) + plays[i]);
        }
        
        List<Map.Entry<String, Integer>> entryList = new ArrayList<>(genresMap.entrySet());
        
        entryList.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));
        
        List<String> genresKey = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : entryList) {
            genresKey.add(entry.getKey());
        }
        
        for (int i = 0; i < genresKey.size(); i++) {
            String genresName = genresKey.get(i);
            
            int maxFirst = 0;
            int maxSecond = 0;
            int[] best = {-1, -1};
            
            for (int j = 0; j < genres.length; j++) {
                if (genres[j].equals(genresName)) {
                    if (maxFirst < plays[j]) {
                        maxSecond = maxFirst;
                        maxFirst = plays[j];
                        
                        best[1] = best[0];
                        best[0] = j;
                    } else if (plays[j] == maxFirst || maxSecond < plays[j]) {
                        maxSecond = plays[j];
                        
                        best[1] = j;
                    } 
                }
            }
            
            answer.add(best[0]);
            
            if (best[1] != -1) {
                answer.add(best[1]);   
            }
        }
        
        return answer;
    }
}