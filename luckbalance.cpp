int luckBalance(int k, vector<vector<int>> c) {
    vector<int> v;
    int count = 0;
    int sum = 0;
    int n = c.size();
    for(int i=0;i<n;i++) {
        if(c[i][1] == 1) {
            v.push_back(c[i][0]);
            count++;
        }
        else {
            sum += c[i][0];
        }
    }
    int sub = 0;
    sort(v.begin(), v.end());
    for(int i=0;i<v.size();i++) {
        sum += v[i];
    }
    int m = count- k;
    for(int i=0;i<m;i++) {
        sub += v[i];
    }
    sum = sum-sub-sub;
    return sum;

}