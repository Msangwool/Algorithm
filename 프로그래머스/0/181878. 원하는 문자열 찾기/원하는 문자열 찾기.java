class Solution {
    public int solution(String myString, String pat) {
        for (int i = 0; i < myString.length(); i++) {

            if (myString.length() - i < pat.length()) {
                break;
            }
            int j = 0;
            for (; j < pat.length(); j++) {
                if (Character.toUpperCase(myString.charAt(i + j))!= Character.toUpperCase(pat.charAt(j))) {
                    break;
                }
            }
            if (j == pat.length()) {
                return 1;
            }
        }
        return 0;
    }
}