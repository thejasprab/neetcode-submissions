class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }

        Map<Character,Integer> sHashmap = new HashMap<>();
        Map<Character,Integer> tHashmap = new HashMap<>();

        for(int i =0;i<s.length();i++){
            sHashmap.put(s.charAt(i), sHashmap.getOrDefault(s.charAt(i), 0) + 1);
            tHashmap.put(t.charAt(i), tHashmap.getOrDefault(t.charAt(i), 0) + 1);
        }

        if (sHashmap.equals(tHashmap)){
            return true;
        }
        else{
            return false;
        }
    }
}
