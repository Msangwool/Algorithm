class Solution {
    public int solution(int[] num_list) {
        // 10개면,
        // 10번 + 10번
        int odd = 0;
        int even = 0;
        for (int i = 0; i < num_list.length; i += 2) {
            odd += num_list[i];
        }
        for (int i = 1; i < num_list.length; i += 2) {
            even += num_list[i];
        }
        return odd > even ? odd : even;
    }
}