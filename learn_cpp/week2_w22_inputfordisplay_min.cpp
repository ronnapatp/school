#include <iostream>
using namespace std;

int main()
{
	int number;
	cout << "Enter number";
	cin >> number;

	for (int i = 1; i <= number; i++){
		for (int s = 1; s <= i; s++){
			printf("*");	
		}
		printf("\n");
	}
	
	return 0;
}
