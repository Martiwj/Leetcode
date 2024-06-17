class Solution {
    public boolean judgeSquareSum(int c) {
        if (c < 0) {
            return false;
        }

        for (int a = 0; a <= Math.sqrt(c); a++) {
            int bSquare = c - a * a;
            int b = (int) Math.sqrt(bSquare);

            if (b * b == bSquare) {
                return true;
            }
        }
        
        return false;
    }
}
