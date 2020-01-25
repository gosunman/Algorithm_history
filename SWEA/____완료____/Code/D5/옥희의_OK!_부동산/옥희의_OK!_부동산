import sys
import timeit
import pprint

sys.stdin = open('옥희의_OK!_부동산', 'r')

start_time = timeit.default_timer()

#include<iostream>
using namespace std;
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
    int N, M;
    int answer;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        cin >> N >> M;
        answer = 0;
        int sample[N];
        int temp[N];
        for (int i = 0; i<N; i++){
            temp[i] = 0;
        	cin >> sample[i];
        }
        for (int i = 0; i<N; i++){
            int size = 0;
        	while (true) {
            	if (i+size < N){
                	if (temp[i] + sample[i+size] < M){
                        temp[i] += sample[i+size];
                        size += 1;
                    } else if (temp[i] + sample[i+size] == M){
                        answer += 1;
                        break;
                    } else {
                    break;
                    }
                } else {
                break;
                }
            }
        }
        cout << "#" << test_case << " " << answer << endl;
	}
	return 0;
}

end_time = timeit.default_timer()

print('running time: {}'.format(end_time - start_time))

#1 3
#2 4