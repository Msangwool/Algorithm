import java.util.*;

class Solution {
    
    static boolean[] visited;
    
    static int[][] top;
    
    static int answer;
    
    static int count;
    
    static int N;
    
    public static int solution(int n, int[][] wires) {
        
        answer = Integer.MAX_VALUE;
        N = n;
        
        top = new int[n + 1][n + 1];
        
        for (int[] wire : wires) {
            int x = wire[0];
            int y = wire[1];
            
            top[x][y] = 1;
            top[y][x] = 1;
        }
                
        for (int[] wire : wires) {
            visited = new boolean[n + 1];
            
            int x = wire[0];
            int y = wire[1];
            
            int[] temp = new int[2];
            int index = 0;
            
            top[x][y] = 0;
            top[y][x] = 0;

            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    count = 0;
                    dfs(i);
                    temp[index] = count;
                    index++;
                }
            }
            
            top[x][y] = 1;
            top[y][x] = 1;
                        
            answer = Math.min(answer, Math.abs(temp[0] - temp[1]));
        }
        
        return answer;
    }
    
    public static void dfs(int i) {
        count++;
        visited[i] = true;
        
        for (int j = 1; j <= N; j++) {
            if (top[i][j] == 1 && !visited[j]) {
                dfs(j);
            }
        }
    }
}