#include <iostream>
using namespace std;

int main()
{
	int number[4];
	int numbers;
	cout << "Enter 5 numbers: \n";

	for(int i = 0; i < 5; i++){
		cin >> numbers;
		number[i] = numbers;
	}
	cout << "The number are: \n";
	for(int y = 0; y < 5; y++ ){
		cout << number[y] << "\n";
	}
	
	return 0;
}
