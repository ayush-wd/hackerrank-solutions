long long gcd(long long int a, long long int b)
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

long long lcm(int a, int b)
{
    return (a / gcd(a, b)) * b;
}

int getTotalX(vector<int> a, vector<int> b) {
    int n =a.size();
    int m = b.size();
    // int least = lcm(a[0],a[n-1]);
    // while(least<=b[0] && least>=a[n-1]) {
    //     for(int i=0;i<m;i++) {
    //         if(b[i]%i != 0) {
    //             break;
    //         }
    //     }
    //     least += least;
    // }
    int ans=0;
    for(int x=1;x<=100;x++){
        bool ok=true;
        for(int i=0;i<n;i++) if(x%a[i]!=0) ok=false;
        for(int i=0;i<m;i++) if(b[i]%x!=0) ok=false; 
        if(ok) ans++;
    }
    return ans;
}
