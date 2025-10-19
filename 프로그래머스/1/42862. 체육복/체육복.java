import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        List<Integer> lostList = new ArrayList<>();
        List<Integer> reserveList = new ArrayList<>();
        
        for (int l : lost) {
            boolean duplicate = false;
            for (int r : reserve) {
                if (l == r) {
                    duplicate = true;
                    break;
                }
            }
            if (!duplicate) lostList.add(l);
        }
        
        for (int r : reserve) {
            boolean duplicate = false;
            for (int l : lost) {
                if (l == r) {
                    duplicate = true;
                    break;
                }
            }
            if (!duplicate) reserveList.add(r);
        }

        for (int r : reserveList) {
            for (int j = 0; j < lostList.size(); j++) {
                int l = lostList.get(j);
                if (l == r - 1 || l == r + 1) {
                    lostList.remove(j);
                    break;
                }
            }
        }
        
        return n - lostList.size();
    }
}