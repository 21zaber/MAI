




int main() {
    int n;
    cin >> n;
    map<int, vector<pair<int, int> > > m;
    for (int i = 0; i < n; ++i) {      
        int s, v;
        cin >> s >> v;
        if (!m.find(s)) {
            m[s] = vector<pair<int, int> >(); 
        } 
        m[s].push_back(make_pair(v, i + 1));
    }
    for (map<int, vector<pair<int, int> > >::iterator i = m.begin(); i != m.end(); ++i) {
        if (i
    }   

    m.
}
