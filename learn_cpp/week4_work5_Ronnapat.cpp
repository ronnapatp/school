#include <iostream>
using namespace std;

int main()
{
	int num, sum, a;
	
	cout << "Input a number: ";
	cin >> num;
	
	for(int i = 1; i < num+1; i++){
		a = i*i;
		sum = sum + a;
	}
	
	cout << "Sum of series: " << sum << endl;

	
	return 0;
}
