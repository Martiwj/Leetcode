import java.util.HashMap;

class twoSum {
    
public static void twoSum(int target, int[] arr){

    HashMap<Integer,Integer> map = new HashMap<>(); 
    
    for(int i = 0; i < arr.length; i ++){

        if (map.containsKey((target - arr[i]))){
            System.out.println(target-arr[i] +" "+ i); 
        }

        map.put(target-arr[i], 0); 
    }
}

public static void main(String[] args) {
    
    int test [] = new int[10];
    
    for (int i = 0; i < test.length; i++){
        test[i] = i; 
    }

    System.out.println(twoSum(10, test));
}


}
