class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        
        // v 는 적어도 하나가 true 면 true
        // ^ 는 둘 다 true일 때만 true
        return (x1 | x2) & (x3 | x4);
    }
}