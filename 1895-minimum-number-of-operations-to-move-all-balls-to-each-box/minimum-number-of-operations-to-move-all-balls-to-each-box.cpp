class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> res;
        vector<int> ind;
        for (int i=0;i<boxes.size();i++){
            if (boxes[i] == '1'){
                ind.push_back(i);
                //cout << i << endl;
            }
        }
        for(int i=0;i<boxes.size();i++){
            int sum = 0;
            for (int j=0;j<ind.size();j++){
                int diff = i - ind[j];
                if (diff < 0){
                    diff = diff * -1;
                }
                sum += diff;
            }
            res.push_back(sum);
        }
        return res;
    }
};