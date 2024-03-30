#include <bits/stdc++.h>

// n acho que eu seja bom, mas eu ja fui pior

using namespace std;

const int MAX_VAL = 1e5+17;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n; cin >> n;
    vector<int> coins(n);
    
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    vector<int> dp(MAX_VAL, 0); // is_possible
    dp[0] = 1;
    
    for (auto coin : coins) {
        for (int i = MAX_VAL-1; i >= 0; i--) {
            if (i+coin < MAX_VAL) {
                dp[i+coin] |= dp[i];
            }
        }
    }
    
    vector<int> ans;
    
    for (int i = 1; i < MAX_VAL; i++) {
        if (dp[i]) {
            ans.push_back(i);
        }
    }
    
    cout << ans.size() << '\n';
    for (auto e : ans) {
        cout << e << ' ';
    }
    
    return 0;
}