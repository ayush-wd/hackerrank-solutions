
void countApplesAndOranges(int s, int t, int a, int b, vector<int> ap, vector<int> o) {
    int apples=0,oranges=0;
    for(int i=0;i<ap.size();i++) {
        if(a+ap[i] >= s && a+ap[i] <= t) {
            apples++;
        }
    }
    for(int i=0;i<o.size();i++) {
        if(b+o[i] >= s && b+o[i] <= t) {
            oranges++;
        }
    }
    cout<<apples<<endl<<oranges;
}