vector<int> breakingRecords(vector<int> scores) {
    long long int max=scores[0],min=scores[0];
    int count1=0,count2=0;
    vector<int> v;
    for(int i=0;i<scores.size();i++) {
        if(scores[i]>max) {
            max=scores[i];
            count1++;
        }
        if(scores[i]<min) {
            min=scores[i];
            count2++;
        }
    }
    v.push_back(count1);
    v.push_back(count2);
    return v;
}
