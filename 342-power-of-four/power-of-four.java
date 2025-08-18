class Solution {
    public boolean isPowerOfFour(int n) {
        if(n <= 0 ){
            return false;
        }
        if(n == 1 || n== 4){
            return true;
        }
        int i = 0;
        while(n > 0){
            if(n % 4 != 0){
                return false;
            }
            n = n / 4;
            System.out.println("n = "+ n);
            i++;
            if(n == 1){
                return true;
            }
            if(n % 4 != 0){
                return false;
            }
            n = n / 4;
            System.out.println("n = "+ n);
            i++;
            if(n == 1){
                return true;
            }
        }
        return false;
    }
}