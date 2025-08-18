
class Solution {
public:
    string largestGoodInteger(string num) {
        string key = "0123456789";
        if (num.size() == 3 && num[0] == num[1] && num[1] == num[2]){
            return num;
        }
        int n = -1;
        for (int i=0;i<num.size()-2;i++){
            if (num[i] == num[i+1] && num[i+1] == num[i+2]){
                for (int j=0;j<key.size();j++){
                    if (key[j] == num[i]){
                        if (j > n){
                            n = j;
                        }
                        break;
                    }
                }
            }
        }
        string res = "";
        if (n == -1){
            return res;
        }
        res += key[n];
        res += key[n];
        res += key[n];
        return res;
    }
};