import java.util.*;
import java.lang.Math;

public class Solution {

    public int solution(String numbers) {
        Set<Integer> generated = generateCombinations(numbers.toCharArray());
        int max = Collections.max(generated);
        
        boolean[] isPrime = sieve(max);

        int count = 0;
        for (int n : generated) {
            if (isPrime[n]) count++;
        }
        return count;
    }

    // 모든 가능한 숫자 조합 생성
    private Set<Integer> generateCombinations(char[] numbers) {
        Set<Integer> result = new HashSet<>();
        boolean[] used = new boolean[numbers.length];
        backtrack(numbers, new StringBuilder(), used, result);
        return result;
    }

    private void backtrack(char[] numbers, StringBuilder path, boolean[] used, Set<Integer> result) {
        if (path.length() > 0) {
            int num = Integer.parseInt(path.toString());
            result.add(num);
        }

        for (int i = 0; i < numbers.length; i++) {
            if (!used[i]) {
                used[i] = true;
                path.append(numbers[i]);
                backtrack(numbers, path, used, result);
                path.deleteCharAt(path.length() - 1);
                used[i] = false;
            }
        }
    }

    // 에라토스테네스의 체
    private boolean[] sieve(int max) {
        boolean[] isPrime = new boolean[max + 1];
        Arrays.fill(isPrime, true);
        if (max >= 0) isPrime[0] = false;
        if (max >= 1) isPrime[1] = false;

        int sqrt = (int) Math.sqrt(max);
        for (int i = 2; i <= sqrt; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= max; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return isPrime;
    }
}
