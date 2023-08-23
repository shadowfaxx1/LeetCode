#include <bits/stdc++.h>
using namespace std;

void dfsperform(int vertex, vector<bool> &vis, vector<int> g[]) {
    vis[vertex] = true;
    cout << vertex << " ";
    for (int i : g[vertex]) {
        if (!vis[i])
            dfsperform(i, vis, g);
    }
}

void dfs(vector<int> graph[], int n) {
    vector<bool> visited(n, false);
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfsperform(i, visited, graph);
        }
    }
}

int main() {
    int n = 4;  // Number of vertices
    vector<int> graph[n];  // Adjacency list representation

    // Adding edges
    graph[0].push_back(1);
    graph[1].push_back(2);
    graph[2].push_back(3);
    graph[3].push_back(1);

    dfs(graph, n);

    return 0;
}
