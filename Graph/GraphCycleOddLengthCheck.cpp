

#include <iostream> 
#include <queue> 
#define V 4 
using namespace std; 
   

bool containsOdd(int G[][V], int src) 
{ 
   
    int colorArr[V]; 
    for (int i = 0; i < V; ++i) 
        colorArr[i] = -1; 
   
    
    colorArr[src] = 1; 
   
   
    queue <int> q; 
    q.push(src); 
   
  
    while (!q.empty()) 
    { 
        
        int u = q.front(); 
        q.pop(); 
   
       
        if (G[u][u] == 1) 
           return true;   
   
        
        for (int v = 0; v < V; ++v) 
        { 
           
            if (G[u][v] && colorArr[v] == -1) 
            { 
                
                colorArr[v] = 1 - colorArr[u]; 
                q.push(v); 
            } 
   
           
            else if (G[u][v] && colorArr[v] == colorArr[u]) 
                return true; 
        } 
    } 
   
    
    return false; 
} 
   

int main() 
{ 
    int G[][V] = {{0, 1, 0, 1}, 
        {1, 0, 1, 0}, 
        {0, 1, 0, 1}, 
        {1, 0, 1, 0} 
    }; 
   
    containsOdd(G, 0) ? cout << "Yes" : cout << "No"; 
    return 0; 
} 
