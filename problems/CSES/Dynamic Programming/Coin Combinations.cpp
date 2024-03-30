#include <bits/stdc++.h>
 
// n acho que eu seja bom, mas eu ja fui pior
 
using namespace std;
 
const int MOD = 1e9+7;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, x; cin >> n >> x;
    vector<int> coin(n), dp(x+1, 0);
    
    for (int i = 0; i < n; i++) {
        cin >> coin[i];
    }
    
    dp[0] = 1;
 
    for (int i = 1; i <= x; i++) {
        for (int j = 0; j < coin.size(); j++) {
            if (i - coin[j] >= 0) {
                dp[i] = (dp[i] + dp[i - coin[j]]) % MOD;
            }
        }
    }
 
    cout << dp[x] << '\n';
 
    return 0;
}