string kangaroo(int x1, int v1, int x2, int v2) {
    string yes="YES";
    string no="NO";
    int i=0;
    while(i<10000) {
        if(x1==x2) {
            return yes;
        }
        x1 += v1;
        x2 += v2;
        i++;
    }
    return no;
}