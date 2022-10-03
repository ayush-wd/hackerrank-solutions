int birthdayCakeCandles(vector<int> a) {
    long long int max = *max_element(a.begin(), a.end());
    long long int count=0;
    for(int i=0;i<a.size();i++) {
        if(a[i]==max) {
            count++;
        }
    }
    return count;
}