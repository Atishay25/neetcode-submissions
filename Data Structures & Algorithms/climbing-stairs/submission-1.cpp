class Solution {
    vector<int> v;
public:
    Solution() {
        v.push_back(1);
        v.push_back(2);
        for(int i = 3; i <= 45; i++){
            v.push_back(v[i-3] + v[i-2]);
        }
    }
    int climbStairs(int n) {
        return v[n-1];
    }
};
