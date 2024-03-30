#include <bits/stdc++.h>

// n acho que eu seja bom, mas eu ja fui pior

using namespace std;

const int MAX = 1010;
const int MOD = 1e9+7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n; cin >> n;
    char grid[MAX][MAX];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    int dp[MAX][MAX];
    
    dp[0][0] = (grid[0][0] != '*');

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;
            
            dp[i][j] = 0;
            
            if (grid[i][j] != '*') {
                if (i-1 >= 0) {
                    dp[i][j] += dp[i-1][j];
                }
    
                if (j-1 >= 0) {
                    dp[i][j] += dp[i][j-1];
                }
    
                dp[i][j] %= MOD;
            }
        }
    }

    cout << dp[n-1][n-1] << '\n';

    return 0;
}
