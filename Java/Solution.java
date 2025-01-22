import java.util.ArrayList;

class Solution {

    public static void main(String[] args) {
        System.out.println(fib(10));
    }

    public static int fib(int n) {

        ArrayList<Integer> ans = new ArrayList<>(); 

        ans.add(0);
        ans.add(1);
     

        for(int i =2; i< n+1; i++){
        
            ans.add((ans.get(i-1)+ans.get(i-2)));
        }

        return ans.get(n-1);
    }

  
}