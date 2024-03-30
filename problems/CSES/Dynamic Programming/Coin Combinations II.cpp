#include <bits/stdc++.h>

// n acho que eu seja bom, mas eu ja fui pior

using namespace std;
using ll = long long;

const int MOD = 1e9+7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, x; cin >> n >> x;
    vector<int> coin(n);

    for (int i = 0; i < n; i++) {
        cin >> coin[i];
    }
    
    vector<ll> dp(x+1, 0);
    dp[0] = 1;

    for (int j = 0; j < n; j++) {
        for (int i = 0; i <= x; i++) {
            if (i-coin[j] >= 0) {
                dp[i] += dp[i-coin[j]];
                dp[i] %= MOD;
            }
        }
    }

    cout << dp[x] << '\n';

    return 0;
}