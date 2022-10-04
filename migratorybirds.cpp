int migratoryBirds(vector<int> a) {
    int count=1;
    vector<int> v;
    int n =a.size();
    for(int i=1;i<=5;i++) {
        count=1;
        for(int j=0;j<n;j++) {
            if(a[j] == i) {
                count++;
            }
        }
        v.push_back(count);
    }
    int max = *max_element(v.begin(), v.end()); 
    int m =v.size();
    for(long long int i=0;i<m;i++) {
        if(v[i] == max) {
            return i+1;
        }
    }
    return 0;
}