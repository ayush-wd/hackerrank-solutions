vector<int> gradingStudents(vector<int> a) {
    vector<int> v;
    for(int i=0;i<a.size();i++) {
        if(a[i]>=38) {
            if(a[i]%5>=3) {
                a[i]=a[i]+(5-a[i]%5);
            }
            
        }
        v.push_back(a[i]);
    }
    return v;
}