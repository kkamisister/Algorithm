class Solution {
    boolean solution(String s) {
        int count = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                count++; // 열린 괄호 +1
            } else {
                count--; // 닫힌 괄호 -1
                if (count < 0) return false; // 닫힌 괄호가 더 많으면 음수
            }
        }

        return count == 0; // 모두 짝이 맞을 떄만 true
    }
}
