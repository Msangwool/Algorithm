class Solution {
    public int solution(String my_string, String is_prefix) {
        if (is_prefix.length() > my_string.length()) {
            return 0;
        }
        for (int i = 0; i < my_string.length(); i++) {
            if (i == is_prefix.length() && my_string.length() != is_prefix.length()) {
                break;
            }
            if (is_prefix.charAt(i) != my_string.charAt(i)) {
                return 0;
            }
        }
        return 1;
    }
}