#include<bits/stdc++.h>
using namespace std; 

void df
void dfs(vector<int> graph[])
{
    int n=graph.size();

    vector<bool> visited;
    for(int i = 0 ;i<n;i++)
    {
        if(!visited[i])
        dfsperform(i);


    }
}


int main ()
{
    vector<int> graph[3];
    dfs(graph);

}