



typedef struct node_s {
    int parent;
    int value;
    vector<int> children;
} node_t;


int main() {
    int n, a, b;
    cin >> n; 
    node_t nodes[n];
    for (int i = 0; i < n; ++i) {
        
    }
    for (int i = 0; i < n-1; ++i) {
        cin >> a >> b;
        nodes[a].children.push_back(b);
        nodes[b].parent = a;    
    }
    
    for (int i = 0; i < n; ++i) {
        if (nodes[i].children.size() == 0) {
            
        }    
    }

}


    for (int i = 0; i < n; ++i) {
        
    }
