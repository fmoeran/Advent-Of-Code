#include<bits/stdc++.h>
#include<array>

using namespace std;

typedef array<int, 3> bp;
typedef array<bp, 4> bpArr; 


bool canMake(const bp &robotPrices, const bp &materials){
    for (int i=0; i<3; ++i){
        if (robotPrices[i] > materials[i]){
            return false;
        }
    }
    return true;
}

bp sub(const bp &als, const bp &bls){
    bp newls;
    for (int i=0; i<3; i++){
        newls[i] = als[i]-bls[i];
    }
    return newls;
}


int maxGeodeCount(bpArr blueprint, int time, bp robCounts, bp matCounts, bp maxRobots){
    if (!time){
        return 0;
    }
    



    bp newMats;
    for (int i=0; i<3; i++){
        newMats[i] = robCounts[i]+matCounts[i];
    }

    int ans;
    bp newRobots;

    ans = maxGeodeCount(blueprint, time-1, robCounts, newMats, maxRobots);
    
    
    if (canMake(blueprint[blueprint.size()-1], matCounts)){
        ans = max(ans, time - 1 + maxGeodeCount(blueprint, time-1, robCounts, newMats, maxRobots));
        
    }

    for (int i=0; i<3; i++){
        if (maxRobots[i]-1 == robCounts[i]){
            continue;
        }
        if (canMake(blueprint[i], matCounts)){
            newRobots = robCounts;
            newRobots[i]++;
            ans = max(ans, maxGeodeCount(blueprint, time-1, newRobots, sub(newMats, blueprint[i]), maxRobots));

        }
    }

    

    return ans;

}

int main(){
    fstream file;

    file.open("19_test.txt");
    
    vector<bpArr> blueprints;
    bpArr newArr;
    bp newBp;
    while (file){
        // ore
        newBp = {0, 0, 0};
        file >> newBp[0];
        newArr[0] = newBp;
        // clay
        newBp = {0, 0, 0};
        file >> newBp[0];
        newArr[1] = newBp;
        // obsidian
        newBp = {0, 0, 0};
        file >> newBp[0];
        file >> newBp[1];
        newArr[2] = newBp;
        // geode
        newBp = {0, 0, 0};
        file >> newBp[0];
        file >> newBp[2];
        newArr[3] = newBp;
        blueprints.push_back(newArr);
    }

    cout << "making..." << '\n';

    bpArr blueprint = blueprints[0] ;

    bp maxRobots = {0,0,0};
    for (int i=0; i<3; i++){
        for (int j=0; j<4; j++){
            maxRobots[i] = max(maxRobots[i], blueprint[j][i]);
        }
    }


    cout << maxGeodeCount(blueprint, 22, {1, 0, 0}, {0, 0, 0}, maxRobots) << endl;



}