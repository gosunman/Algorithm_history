//
//  028.cpp
//  Cpp200
//
//  Created by Netple_Mac on 2019/12/14.
//  Copyright © 2019 Netple_Mac. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int main()
{
    bitset<8> bit1;
    bit1.reset();
    bit1 = 127;

    bitset<8> bit2;
    bit2.reset();
    bit2 = 0x20;

    bitset<8> bit3 = bit1 & bit2;
    bitset<8> bit4 = bit1 | bit2;
    bitset<8> bit5 = bit1 ^ bit2;
    bitset<8> bit6 = ~bit2;
    bitset<8> bit7 = bit2 << 1;
    bitset<8> bit8 = bit2 >> 1;

    cout << bit3 << bit4 << bit5 << bit6 << bit7 << bit8 << endl;

    return 0;
}
