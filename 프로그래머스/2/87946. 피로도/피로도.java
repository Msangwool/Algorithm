class Solution {
    private boolean[] visited;
    private int answer;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        backtrack(k, dungeons, 0);
        return answer;
    }
    
    private void backtrack(int k, int[][] dungeons, int count) {
        answer = Math.max(answer, count);
        
        for (int i = 0; i < dungeons.length; i++) {
            int need = dungeons[i][0];
            int cost = dungeons[i][1];
            
            if (!visited[i] && k >= need) {
                visited[i] = true;
                backtrack(k - cost, dungeons, count + 1);
                visited[i] = false;            
            }
        }
    }
}