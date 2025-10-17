import java.util.*;

class Solution {
    
    static List<String> books = new ArrayList<>();
    
    static char[] alpha = new char[]{'A', 'E', 'I', 'O', 'U'};
        
    static int maxLen;
    
    public static int solution(String word) {
        
        // 길이 1 ~ 5까지 반복하면서 그 안에서 DFS 진행
        for (int strLen = 1; strLen <= 5; strLen++) {
            maxLen = strLen;
            backtrack("");
        }
        
        Collections.sort(books);
                
        return books.indexOf(word) + 1;
    }
    
    public static void backtrack(String str) {
        if (str.length() == maxLen) {
            books.add(str);
            return;
        }
        
        
        for (int i = 0; i < alpha.length; i++) {
            backtrack(str + alpha[i]);
        }
    }
}