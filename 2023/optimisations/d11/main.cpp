//
// I wanted to see how much speed I could get from one core to solve day 11
// Fastest was v3 & v5
// Tried to allow for as much implicit SIMD as possible

//


#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <utility>
#include <algorithm>
#include <chrono>
#include <bitset>

#define EXPANSION 1000000
// case specific
#define ANSWER 447073334102
#define N 140

using namespace std;
using namespace std::chrono;


vector<string> globData;

void loadStringData() {
    ifstream file("data.txt");
    assert(file.is_open());
    string s;
    while (file >> s)
        globData.push_back(s);

    file.close();
}

vector<string> getStringData() {
    return globData;
}


// a direct port of my python code
long long v1() {
    vector<string> data = getStringData();

    int n = data.size();  // n = #rows = #cols

    vector<long long> rowWeights(n, 1), colWeights(n, 1);
    for (int i=0; i<n; i++) {
        // search row
        string& row = data[i];
        if (find(row.begin(), row.end(), '#') == row.end())
            rowWeights[i] = EXPANSION;

        // search col
        bool found = false;
        for (int r=0; r<n; r++) {

            if (data[r][i] == '#') {
                found = true;
                break;
            }
        }
        if (!found) colWeights[i] = EXPANSION;
    }

    vector<pair<int, int>> gals;
    for (int r=0; r<n; r++) {
        for (int c=0; c<n; c++) {
            if (data[r][c] == '#') {
                gals.emplace_back(r, c);
            }
        }
    }

    long long total = 0;
    int galCount = gals.size();
    for (int i=0; i<galCount; i++) {
        pair<int, int> a = gals[i];
        for (int j=i+1; j<galCount; j++) {
            pair<int, int> b = gals[j];

            long long dist = 0;
            int rstart = min(a.first, b.first);
            int rend   = max(a.first, b.first);

            for (int r = rstart+1; r <= rend; r++) {
                dist += rowWeights[r];
            }

            int cstart = min(a.second, b.second);
            int cend   = max(a.second, b.second);

            for (int col = cstart+1; col <= cend; col++) {
                dist += colWeights[col];
            }

            total += dist;
        }
    }
    assert(total == ANSWER);
    return total;
}

// prefix sum improvement
// roughly 13x improvement
long long v2() {
    vector<string> data = getStringData();

    int n = data.size();

    vector<long long> pfxRowWeights(n, 1), pfxColWeights(n, 1);

    for (int i=1; i<n; i++) { // assume r[1] and c[1] both have galaxies
        string& row = data[i];

        // row
        pfxRowWeights[i] = pfxRowWeights[i-1];
        if (find(row.begin(), row.end(), '#') == row.end()) {
            pfxRowWeights[i] += EXPANSION;
        }else {
            pfxRowWeights[i] += 1;
        }

        // col
        pfxColWeights[i] = pfxColWeights[i-1];
        bool found = false;
        for (int r=0; r<n; r++) {
            if (data[r][i] == '#') {
                found = true;
                break;
            }
        }
        if (!found) {
            pfxColWeights[i] += EXPANSION;
        }else {
            pfxColWeights[i] += 1;
        }
    }

    vector<pair<int, int>> gals;
    for (int r=0; r<n; r++) {
        for (int c=0; c<n; c++) {
            if (data[r][c] == '#') {
                gals.emplace_back(r, c);
            }
        }
    }

    long long total = 0;
    int galCount = gals.size();
    for (int i=0; i<galCount; i++) {
        pair<int, int> a = gals[i];
        for (int j=i+1; j<galCount; j++) {
            pair<int, int> b = gals[j];

            // removed loops across intermediate rows and cols

            long long dist = 0;

            int rstart = min(a.first, b.first);
            int rend   = max(a.first, b.first);

            dist += pfxRowWeights[rend] - pfxRowWeights[rstart];

            int cstart = min(a.second, b.second);
            int cend   = max(a.second, b.second);

            dist += pfxColWeights[cend] - pfxColWeights[cstart];

            total += dist;
        }
    }
    assert(total == ANSWER);
    return total;
}

// prefix sum improvement
// roughly 1.5x improvement
long long v3() {
    vector<string> data = getStringData();

    int n = data.size();

    vector<long long> pfxRowWeights(n, 1), pfxColWeights(n, 1);

    for (int i=1; i<n; i++) { // assume r[1] and c[1] both have galaxies
        string& row = data[i];

        // row
        pfxRowWeights[i] = pfxRowWeights[i-1];
        if (find(row.begin(), row.end(), '#') == row.end()) {
            pfxRowWeights[i] += EXPANSION;
        }else {
            pfxRowWeights[i] += 1;
        }

        // col
        pfxColWeights[i] = pfxColWeights[i-1];
        bool found = false;
        for (int r=0; r<n; r++) {
            if (data[r][i] == '#') {
                found = true;
                break;
            }
        }
        if (!found) {
            pfxColWeights[i] += EXPANSION;
        }else {
            pfxColWeights[i] += 1;
        }
    }


    vector<pair<int, int>> gals;
    for (int r=0; r<n; r++) {
        for (int c=0; c<n; c++) {
            if (data[r][c] == '#') {
                gals.emplace_back(r, c);
            }
        }
    }


    long long total = 0;
    int galCount = gals.size();
    for (int i=0; i<galCount; i++) {
        pair<int, int> a = gals[i];
        for (int j=i+1; j<galCount; j++) {
            pair<int, int> b = gals[j];

            // removed loops across intermediate rows and cols

            long long dist = 0;

            dist += pfxRowWeights[b.first] - pfxRowWeights[a.first];

            dist += abs(pfxColWeights[b.second] - pfxColWeights[a.second]);

            total += dist;
        }
    }
    assert(total == ANSWER);
    return total;
}

// using a bitset and static arrays
// no improvements
long long v4() {
    vector<string> strData = getStringData();

    bitset<N*N> data;
    int shift = N*N;

    for (int row=0; row<N; row++) {
        string s = strData[row];
        for (int col=0; col<N; col++) {
            shift --;
            data[shift] = (bool)(s[col] ^ '.');
        }
    }




    long long pfxRowWeights[N], pfxColWeights[N];

    pfxRowWeights[0] = 1;
    pfxColWeights[0] = 1;

    bitset<N*N> firstRow = 0ULL, firstCol = 0ULL;

    for (int i=0; i<N; i++) {
        firstRow.set(N*(N-1) + i);
        firstCol.set(N*(i+1)-1);
    }

    for (int i=1; i<N; i++) {
        firstRow >>= N;
        firstCol >>= 1;
        // row
        pfxRowWeights[i] = pfxRowWeights[i-1];
        if ((data & firstRow).any()) {
            pfxRowWeights[i] += 1;
        }else {
            pfxRowWeights[i] += EXPANSION;
        }

        // col
        pfxColWeights[i] = pfxColWeights[i-1];
        if ((data & firstCol).any()) {
            pfxColWeights[i] += 1;
        }else {
            pfxColWeights[i] += EXPANSION;
        }
    }



    vector<pair<int, int>> gals;
    for (int r=0; r<N; r++) {
        for (int c=0; c<N; c++) {
            if (data[r*N + c]) {
                gals.emplace_back(N-r-1, N-c-1);
            }
        }
    }


    long long total = 0;
    int galCount = gals.size();
    for (int i=0; i<galCount; i++) {
        pair<int, int> a = gals[i];
        for (int j=i+1; j<galCount; j++) {
            pair<int, int> b = gals[j];

            // removed loops across intermediate rows and cols

            long long dist = 0;

            dist += abs(pfxRowWeights[b.first] - pfxRowWeights[a.first]);

            dist += abs(pfxColWeights[b.second] - pfxColWeights[a.second]);

            total += dist;
        }
    }
    assert(total == ANSWER);
    return total;

}

// change to have arrays of bitsets for every row and col
// improves from v4 but basically as fast as v3
long long v5() {
    vector<string> strData = getStringData();

    bitset<N> rows[N], cols[N];
    int shift = N*N;

    for (int row=0; row<N; row++) {
        string s = strData[row];
        for (int col=0; col<N; col++) {
            bool val = (bool)(s[col] ^ '.');
            rows[row][col] = val;
            cols[col][row] = val;
        }
    }




    long long pfxRowWeights[N], pfxColWeights[N];

    pfxRowWeights[0] = 1;
    pfxColWeights[0] = 1;

    for (int i=1; i<N; i++) {
        // row
        pfxRowWeights[i] = pfxRowWeights[i-1];
        if (rows[i].any()) {
            pfxRowWeights[i] += 1;
        }else {
            pfxRowWeights[i] += EXPANSION;
        }

        pfxColWeights[i] = pfxColWeights[i-1];
        // col
        if (cols[i].any()) {
            pfxColWeights[i] += 1;
        }else {
            pfxColWeights[i] += EXPANSION;
        }
    }

    vector<pair<int, int>> gals;
    for (int r=0; r<N; r++) {
        for (int c=0; c<N; c++) {
            if (rows[r][c]) {
                gals.emplace_back(r, c);
            }
        }
    }


    long long total = 0;
    int galCount = gals.size();
    for (int i=0; i<galCount; i++) {
        pair<int, int> a = gals[i];
        for (int j=i+1; j<galCount; j++) {
            pair<int, int> b = gals[j];

            // removed loops across intermediate rows and cols

            long long dist = 0;

            dist += pfxRowWeights[b.first] - pfxRowWeights[a.first];

            dist += abs(pfxColWeights[b.second] - pfxColWeights[a.second]);

            total += dist;
        }
    }
    assert(total == ANSWER);
    return total;

}

// use smaller type sizes
long long v6() {
    vector<string> strData = getStringData();
    vector<vector<bool>> data(N, vector<bool>(N, false));

    for (int row=0; row<N; row++) {
        for (int col=0; col<N; col++) {
            data[row][col] = strData[row][col] == '#';
        }
    }

    long long pfxRowWeights[N], pfxColWeights[N];
    pfxRowWeights[0] = 1;
    pfxColWeights[0] = 1;

    for (int i=1; i<N; i++) {
        vector<bool> row = data[i];

        // row
        pfxRowWeights[i] = pfxRowWeights[i-1];
        bool found = false;
        for (int c=0; c<N; c++) {
            if (row[c]) {
                found = true;
                break;
            }
        }
        if (!found) {
            pfxRowWeights[i] += EXPANSION;
        }else {
            pfxRowWeights[i] += 1;
        }

        // col
        pfxColWeights[i] = pfxColWeights[i-1];
        found = false;
        for (int r=0; r<N; r++) {
            if (data[r][i]) {
                found = true;
                break;
            }
        }
        if (!found) {
            pfxColWeights[i] += EXPANSION;
        }else {
            pfxColWeights[i] += 1;
        }
    }

    vector<pair<unsigned short, unsigned short>> gals;
    for (unsigned short r=0; r<N; r++) {
        for (unsigned short c=0; c<N; c++) {
            if (data[r][c]) {
                gals.emplace_back(r, c);
            }
        }
    }


    long long total = 0;
    for (int i=0; i<gals.size(); i++) {
        auto a = gals[i];
        for (int j=i+1; j<gals.size(); j++) {

            auto b = gals[j];

            total += pfxRowWeights[b.first] - pfxRowWeights[a.first];

            total += abs(pfxColWeights[b.second] - pfxColWeights[a.second]);
        }
    }
    assert(total == ANSWER);
    return total;
}

void bench(string name, long long (*const fn)(), int count=500) {
    if (fn() != ANSWER) {
        cerr << name << " did not return the correct value." << endl;
    }
    long long res;
    auto t0 = high_resolution_clock::now();
    for (int i=0; i<count; i++) {
        res = fn();
    }
    auto t1 = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(t1-t0).count();

    cout << name << ": ";
    cout << ((float)duration/(float)count) << " µs" << endl;
    //cout << endl;
    //cout << "-Total:   " << duration << " µs" << endl;
    //cout << "-Average: " << ((float)duration/(float)count) << " µs" << endl;
}


int main() {
    loadStringData();

    bench("Basic", v1, 100);
    bench("Prefix Sum", v2);
    bench("No MaxMin", v3);
    bench("Bitset", v4);
    bench("RC Bitsets", v5);
    bench("Small types", v6);


}