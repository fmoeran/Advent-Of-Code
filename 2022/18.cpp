#include<iostream>
#include<fstream>
#include<set>
#include<array>
#include<string>
#include<vector>




using namespace std;

array<array<int, 3>, 6> n = {{-1, 0, 0}, {1, 0, 0}, {0, -1, 0}, {0, 1, 0}, {0, 0, -1}, {0, 0, 1}};

vector<array<int, 3>> getNeighbours(array<int, 3> &pos){
    vector<array<int, 3>> result;



}

int main(){
    set<array<int, 3>> blocks;
    array<int, 3> a;
    fstream file;
    file.open("18.txt");
    string s;
    string num;
    while (file){
        file >> s;
        int i = 0;
        string num;
        // cout << s << endl;
        for (char c : s){
            //cout << c << endl;
            if (c == ','){
                a[i] = stoi(num);
                num = "";
                ++i;
            }else{
                num += c;
            }
        }
        a[i] = stoi(num);
        blocks.insert(a);
        cout << a[0] << endl;
    }


}