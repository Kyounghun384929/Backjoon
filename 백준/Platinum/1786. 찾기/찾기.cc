#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> computePrefixFunction(const string& P) {
    int m = P.length();
    vector<int> pi(m, 0);
    int k = 0;

    for (int q = 1; q < m; ++q) {
        while (k > 0 && P[k] != P[q]) {
            k = pi[k - 1];
        }
        if (P[k] == P[q]) {
            k++;
        }
        pi[q] = k;
    }
    return pi;
}

vector<int> KMPMatcher(const string& T, const string& P) {
    int n = T.length();
    int m = P.length();
    vector<int> pi = computePrefixFunction(P);
    vector<int> result;

    int q = 0;
    for (int i = 0; i < n; ++i) {
        while (q > 0 && P[q] != T[i]) {
            q = pi[q - 1];
        }
        if (P[q] == T[i]) {
            q++;
        }
        if (q == m) {
            result.push_back(i - m + 1);
            q = pi[q - 1];
        }
    }
    return result;
}

int main() {
    string T, P;
    getline(cin, T);
    getline(cin, P);

    vector<int> result = KMPMatcher(T, P);

    cout << result.size() << endl;
    for (int pos : result) {
        cout << pos + 1 << " ";
    }
    cout << endl;

    return 0;
}
