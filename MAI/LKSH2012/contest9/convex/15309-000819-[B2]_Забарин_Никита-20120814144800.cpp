#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

const long long inf = 1000000000000000000;

class Vect {
public:
	long long x, y;
	Vect (){};
	Vect (long long a, long long b){
		x = a;
		y = b;
	};	
	long double l (){
		return sqrt((long double)(x * x + y * y));
	};
	long double operator * (Vect b){
		return x * b.y - y * b.x;
	};
};
Vect p0;

Vect makevect (Vect a, Vect b){
	Vect v;
	v.x = b.x - a.x;
	v.y = b.y - a.y;
	return v;
};

bool cmpr (pair<Vect, int> p1, pair<Vect, int> p2) {
    
	Vect v1 = makevect(p0, p1.first);
	
    Vect v2 = makevect(p0, p2.first);
    
    if ((v1 * v2) > 0) {
        return true;
	} else { 
		if ((v1 * v2) == 0) {
			return v1.l() < v2.l();
		};
	};
    return false;
};

long long square(vector< pair<Vect, int> > &pts) {
	long double ans = 0;	
	for (int i = 1; i < pts.size(); i++) {
		ans += (pts[i].first * pts[i - 1].first);
	};
	ans += pts[0].first * pts[pts.size() - 1].first;
	return abs(ans);
};

long double per(vector< pair<Vect, int> > &pts) {
	long double ans = 0;
	
	for (int i = 0; i < pts.size() - 1; i++) {
		ans += (long double) makevect(pts[i].first, pts[i + 1].first).l();
	};
	ans += (long double) makevect(pts[pts.size() - 1].first, pts[0].first).l();
	return ans;
};

Vect readvect (){
	Vect v;
	long long x, y;
	cin >> x >> y;
	v.x = x;
	v.y = y;
	return v;
};

stack<pair <Vect, int> > st;

pair<Vect, Vect> lst (){
	Vect last = st.top().first;
	int tmp = st.top().second;
	st.pop();
	Vect plast = st.top().first;
	st.push(make_pair(last, tmp));
	return make_pair(last, plast);
};


vector<pair <Vect, int> > pts;
vector<pair <Vect, int> > ans;

int main (){
	freopen("convex.in", "r", stdin);
    freopen("convex.out", "w", stdout);
	int n;
	cin >> n;
	Vect v;
	p0.x = inf;
	p0.y = inf;
	for (int i = 0; i < n; i ++){
		v = readvect();
		if (p0.y > v.y || ((p0.y == v.y) && (p0.x > v.x))){
			p0 =v;
		};
		pts.push_back(make_pair(v, i));
	};
	sort(pts.begin(), pts.end(), cmpr);

	for (int i = 0; i < n; i ++){
		v = pts[i].first;
		if (st.size() > 1){
			while ((st.size() > 1) && (makevect(lst().second, lst().first) * makevect(lst().first, v) <= 0)){
				st.pop();
			};
		};
		st.push(pts[i]);
	};
	while (st.size() > 0) {
		ans.push_back(st.top());
		st.pop();
	};
	sort(ans.begin(), ans.end(), cmpr);
	cout << ans.size() << "\n";
	for (int i = 0; i < ans.size(); i ++){
		cout << ans[i].second + 1 << " ";
	};
	cout.precision(25);
	cout << "\n";
	cout << per(ans) << "\n";
	long long s = square(ans);
	if (s % 2 == 1){
		cout << s / 2 << ".5";
	} else {
		cout << s / 2 << ".0";
	};
	return 0;
};