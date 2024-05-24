class Solution {
    public int solution(String my_string, String is_suffix) {
        int str_length = my_string.length();
        int suf_length = is_suffix.length();
        
        int answer;
        if (str_length < suf_length) {
            answer = 0;
        } else if (str_length == suf_length) {
            if (my_string.equals(is_suffix)) {
                answer = 1;
            } else {
                answer = 0;
            }
        } else {
            answer = 1;
            for (int i = 0; i < suf_length; i++) {
                if (my_string.charAt(i + str_length - suf_length) != is_suffix.charAt(i)) {
                    answer = 0;
                    break;
                }
            }
        }
        return answer;
    }
}