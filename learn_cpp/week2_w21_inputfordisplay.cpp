#include <iostream>
using namespace std;

int main()
{
	int number;
	cout << "Enter number";
	cin >> number;
	
	for (int i = 0; i < number+1; i++){
		cout << i << "\n";
	}

	cout << "\n\n";
	for (int i = number; i > 0; i--){
		cout << i << "\n";
	}
	return 0;
	 	
}
