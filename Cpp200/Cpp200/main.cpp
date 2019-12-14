#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int max_number;
		cin >> max_number;
		int answer = 0;
		for (int i = 1; i <= max_number; max_number++)
		{
			int number = pow(10, (i / 10 + 1));
			if (number % i == 0)
			{
				answer += 1;
			}
		}
		cout << "#" << "test_case" << " " << answer << endl;
	}

	return 0;
}