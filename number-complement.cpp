#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findComplement(int num) {
        int n_bits = ceil(log2(num));
        int ret = 0;
        for(int i = n_bits-1; i >= 0; i--){
			int bit = (num & (1<<i)) > 0 ? 0 : 1;
			if(bit and !ret)ret = bit;			
			else ret = (ret << 1) | bit;			
		}
        return ret;
    }
};

int main(){
	Solution sol;
	cout<<sol.findComplement(1)<<endl;
}
