#include <iostream>
using namespace std;

int main()
{
	int num;
	
	cout << "Input a number: ";
	cin >> num;
	
	for(int i = 1; i < 11; i++){
		cout << num << "x" << i << "=" << num*i << "\n" << endl;
	}

	
	return 0;
}
