int dfs(int x, int p) {
    for (auto e : adj[x]) {
        if (e != p) {
            dfs(e, x);
        }
    }
}