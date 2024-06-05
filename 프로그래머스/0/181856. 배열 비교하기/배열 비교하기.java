class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int arr1Length = arr1.length;
        int arr2Length = arr2.length;
        if (arr1Length > arr2Length) {
            return 1;
        } else if (arr1Length < arr2Length) {
            return -1;
        }
        
        int sum = 0;
        for (int i : arr1) {
            sum += i;
        }
        for (int i : arr2) {
            sum -= i;
        }
        return sum > 0 ? 1 : sum < 0 ? -1 : sum;
    }
}