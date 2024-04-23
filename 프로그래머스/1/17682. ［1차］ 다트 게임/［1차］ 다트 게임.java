class Solution {
    public int solution(String dartResult) {
        
        // 다트 3번 (합계로 승부)
        
        // 0 ~ 10 (한번당)
        // S -> * 1  /  D -> * 2  /  T -> * 3
        
        // * -> 지금꺼 * 2, 방금전꺼 * 2
        // # -> 해당 점수는 -=
        
        // * 가 처음이면 지금꺼만 * 2
        
        // * 는 중첩이 가능함 (4배가 됨)
        
        // 점수 오고( 0 ~ 10 ) / 보너스 오고 ( S, D, T ) / 옵션 ( * or # or 없음)
        
        
        // 앞에서부터 반복했을 때, 두번째 연산이 일어난다는 것을 어떻게 인지 할 수 있는지 ?
        // 뒤에서부터 반복했을 때, index bound? 가 일어나는 것을 어떻게 막을 수 있는지 ?
        
        int[] sum = new int[4];
        
        int level = 1;
        
        for (int i = 0; i < dartResult.length(); i++) {
            if (Character.isDigit(dartResult.charAt(i))) {
                if (Character.isDigit(dartResult.charAt(i + 1))) {
	                sum[level] = getPoint(dartResult.charAt(i + 2), 10);
                    if (i + 3 >= dartResult.length()) {
                        break;
                    }
                    if (dartResult.charAt(i + 3) == '*') {
                        sum[level] *= 2;
                        if (level >= 1) {
                            sum[level - 1] *= 2;
                        }
                        i += 3;
                    } else if (dartResult.charAt(i + 3) == '#') {
                        sum[level] *= -1;
                        i += 3;
                    } else {
                        i += 2;
                    }
                } else {
                    sum[level] = getPoint(dartResult.charAt(i + 1), dartResult.charAt(i) - '0');
                    if (i + 2 >= dartResult.length()) {
                        break;
                    }
                    if (dartResult.charAt(i + 2) == '*') {
                        sum[level] *= 2;
                        if (level > 1) {
                            sum[level - 1] *= 2;
                        }
                        i += 2;
                    } else if (dartResult.charAt(i + 2) == '#') {
                        sum[level] *= -1;
                        i += 2;
                    } else {
                        i += 1;
                    }
                }
            }
            level++;
        }
        
        int answer = 0;
        for (int i = 1; i < sum.length; i++) {
            answer += sum[i];
        }
        return answer;
    }
    
    public static int getPoint(char bonus, int point) {
        if (bonus == 'S') {
            return point;
        } else if (bonus == 'D') {
            return point * point;
        } else {
            return point * point * point;
        }
    }
}