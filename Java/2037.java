import java.util.Arrays;

class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {


        int a[] = Arrays.sort(seats);
        int b[] = Arrays.sort(students);
        int moves = 0; 

        for(int i = 0; i < students.length; i ++){
            moves = moves + Math.abs(a[i] - b[i]); 
        }

        return moves; 

    }
}