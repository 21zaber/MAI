#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<bool> used;
vector<int> s;
vector<long long> powers, left_hash, rigth_hash;
int n, m;

void hhash (long long p, long long q){
	powers.resize(n * 5 + 5, 0);
	left_hash.resize(n * 5 + 5);
	rigth_hash.resize(n * 5 + 5);
	powers[0] = 1;
	for (int i = 1; i < n; i ++){
		powers[i] = ((powers[i - 1] * p) % q + q) % q;
	};
	left_hash[0] = s[0];
	for(int i = 1; i < n; i ++){
		left_hash[i] = ((left_hash[i - 1] * p + s[i]) % q + q) % q;
	};
	rigth_hash[n - 1] = s[n - 1];
	for(int i = n - 2; i > -1; i --){
		rigth_hash[i] = ((rigth_hash[i + 1] * p + s[i]) % q + q) % q;
	};
	for (int i = 0; i < n; i ++){
		long long h2 = ((rigth_hash[i + 1] - rigth_hash[2 * i + 2] * powers[i + 1]) % q + q) % q;
		/*h2 = rigth_hash[i + 1];
		h2 = rigth_hash[2 * i + 2];
		h2 = powers[i + 1];*/
		long long h1 = left_hash[i];
		if (h1 != h2){
			used[n - i - 1] = false;
		};
	};
};

int main() {
	freopen("cubes.in", "r", stdin);
	freopen("cubes.out", "w", stdout);
	
	cin >> n >> m;
	
	used.resize(n * 5 + 5, true);
	s.resize(n * 5 + 5);

	for (int i = 0; i < n; i++){
		cin >> s[i];
	};

	hhash(797,  1000000007);
	hhash(1543, 1000000037);
	hhash(1547, 1000000087);
	/*hhash(2376582235, 476514765147564);
	hhash(2141242412, 257245724572267);
	hhash(4576586233, 125725724574577);
	hhash(178481,     926378261);
	hhash(148579,     973231291);*/

	for (int i = 0; i < n; i++){
		if (used[i]){
			cout << i << " ";
		};
	};
	cout << n;
}
