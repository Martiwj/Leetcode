class Solution {
    public String mergeAlternately(String word1, String word2) {

        StringBuilder newString = new StringBuilder(); 

        int minLength = Math.min(word1.length(), word2.length());

        for(int i = 0; i < minLength; i++){
            newString.append(word1.charAt(i)); 
            newString.append(word2.charAt(i)); 
        }

        if (word1.length() > word2.length()){
            newString.append(word1.substring(minLength)); 

        }else{
            newString.append(word2.substring(minLength)); 
        }

        return newString

    }
}