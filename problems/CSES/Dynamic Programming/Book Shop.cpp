#include <bits/stdc++.h>

// n acho que eu seja bom, mas eu ja fui pior

using namespace std;

const int INF = 1e9+17;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, x; cin >> n >> x;
    vector<int> price(n+1), pages(n+1);

    for (int i = 1; i <= n; i++) { cin >> price[i]; }

    for (int i = 1; i <= n; i++) { cin >> pages[i]; }
    
    vector<vector<int>> dp(n+1, vector<int>(x+1, 0));
    dp[0][0] = 0;

    for (int i = 1; i <= n; i++) {
        for (int peso = 1; peso <= x; peso++) {
            if (peso - price[i] >= 0) { // pegar o item
                dp[i][peso] = max(dp[i-1][peso], dp[i-1][peso - price[i]] + pages[i]);
            } else { // n pegar o item
                dp[i][peso] = dp[i-1][peso];
            }
        }
    }

    cout << dp[n][x] << '\n';

    return 0;
}