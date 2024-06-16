class Solution {
    public void rotate(int[][] matrix) {

        int left = 0; 
        int right = matrix.length-1; 


        while(left < right){
           int temp[] = matrix[left]; 
            matrix[left] = matrix[right]; 
            matrix[right] = temp; 

            left ++; 
            right --; 
        
        }

        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < i; j ++){
                int temp = matrix[j][i]; 
                matrix[j][i] = matrix[i][j]; 
                matrix[i][j] = temp; 
            }
        }
        
    }
}