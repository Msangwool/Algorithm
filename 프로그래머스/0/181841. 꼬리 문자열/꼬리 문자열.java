class Solution {
    public String solution(String[] str_list, String ex) {
        StringBuilder answer = new StringBuilder();
        for (String str : str_list) {
            if (str.indexOf(ex) == -1) {
                answer.append(str);
            }
        }
        return answer.toString();
    }
}