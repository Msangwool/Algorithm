class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        
        // 카드 뭉치 두개 
        
        // 차드에 적힌 단어들을 사용해서 원하는 순서의 단어 배열
        
        // int 를 두개 둬서 
        // idx_1 = 0;
        // idx_2 = 0;
        
        // 으로 해서 조건에 맞을 때마다 각각 index를 하나씩 빼면 되겠네
        
        // if (첫번째 배열)
        // else if (두번째 배열)
        // else {answer = "No"; break;}
        
        String answer = "Yes";
        
        int idxCards1 = 0;
        int cards1Length = cards1.length;
        int idxCards2 = 0;
        int cards2Length = cards2.length;
        for (String str : goal) {
            if (idxCards1 < cards1Length && str.equals(cards1[idxCards1])) {
                idxCards1++;
            } else if (idxCards2 < cards2Length && str.equals(cards2[idxCards2])) {
                idxCards2++;
            } else {
                answer = "No";
                break;
            }
        } 
        
        return answer;
    }
}