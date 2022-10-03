void miniMaxSum(vector<int> arr) {
    long long int sum=0;
    long long int min = *min_element(arr.begin(), arr.end());
    long long int max = *max_element(arr.begin(), arr.end());
    for(int i=0;i<arr.size();i++) {
        sum += arr[i];
    }
    long long int ans1=0,ans2=0;
    ans1 = sum-max;
    ans2 = sum-min; 
    cout<<ans1<<" "<<ans2;
}