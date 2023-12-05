#include<iostream>
#include<fstream>
#include<vector>
#include<utility>
#include<array>


using namespace std;

int dist(int sx, int sy, int ex, int ey){
    return abs(sx-ex) + abs(sy-ey);
}


int main(){
    int maxDist = 20;
    maxDist = 4000000;
    int minDist = 0;
    vector<array<int, 4>> coords;
    array<int, 4> a;
    array<int, 4> cop;
    fstream file;
    file.open("15.txt");
    string word;
    while (file){
        for (int i=0; i<4; ++i){
            file >> a[i];
        }
        copy(a.begin(), a.end(), cop.begin());
        coords.push_back(cop);
    }
    file.close();


    vector<pair<int, int>> possibles;
    vector<pair<pair<int, int>, int>> distances;
    pair<int, int> newCoord;
    pair<pair<int, int>, int> coordDistance;
    



    int newDist;
    int yChange;
    int x, y;
    for (auto a : coords){
        x = a[0];
        y = a[1];
        newDist = 1 + dist(a[0], a[1], a[2], a[3]);

        cout << newDist << '\n';

        newCoord.first = x;
        newCoord.second = y;
        coordDistance.first = newCoord;
        coordDistance.second = newDist-1;
        distances.push_back(coordDistance);



        for (int xChange=-newDist; xChange<=newDist;++xChange){
            yChange = newDist-abs(xChange);
            newCoord.first = x+xChange;
            newCoord.second = y+yChange;
            if (newCoord.first>=0 && newCoord.first<=maxDist && newCoord.second>=0 && newCoord.second<=maxDist)
            possibles.push_back(newCoord);
            newCoord.second = y-yChange;
            if (newCoord.first>=0 && newCoord.first<=maxDist && newCoord.second>=0 && newCoord.second<=maxDist)
            possibles.push_back(newCoord);
        }
        
    }
    
    int sourceX, sourceY, sourceDist;
    bool found = false;

    for (pair<int, int> coord : possibles){
        x = coord.first;
        y = coord.second;
        found = true;


        // check if it is within range of any source
        for (auto distCoordPair : distances){
            sourceX = distCoordPair.first.first;
            sourceY = distCoordPair.first.second;
            sourceDist = distCoordPair.second;
            newDist = dist(x, y, sourceX, sourceY);
            if (newDist <= sourceDist){
                found = false;
                break;
            }
        }
        if (found){
            cout << x << ' ' << y << '\n';
            break;
        }
    }
    cout << x << ' ' << y << '\n';
    cout <<(long long) x * 4000000 + y << '\n';
    
}
