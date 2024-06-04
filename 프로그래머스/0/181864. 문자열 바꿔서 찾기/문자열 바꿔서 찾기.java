class Solution {
    public int solution(String myString, String pat) {
        StringBuilder st = new StringBuilder();
        for (int i = 0; i < myString.length(); i++) {
            st.append(myString.charAt(i) == 'A' ? 'B' : 'A');
        }
        return st.toString().contains(pat) ? 1 : 0;
    }
}