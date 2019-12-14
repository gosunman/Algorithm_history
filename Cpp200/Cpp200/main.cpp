#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <stack>

using namespace std;

int main()
{

    int test_case;
    int T;
    cin>>T;
    for(test_case = 1; test_case <= T; test_case++)
    {
        int check[10] = {0,};
        string inputs;
        cin >> inputs;
        for (int i=0; i<inputs.size(); i++)
        {
            int number = inputs[i];
            if (check[number])
            {
                check[number] = 0;
            }
            else
            {
                check[number] = 1;
            }
        }
        int answer = 0;
        for (int i = 0; i < 10; i++)
        {
            if(check[i])
            {
                answer += 1;
            }
        }
        cout << "#" << test_case << " " << answer << endl;
    }
    return 0;
    
}
