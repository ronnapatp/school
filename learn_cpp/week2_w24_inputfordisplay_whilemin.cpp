#include <iostream>
using namespace std;

int main()
{
	int number;
	cout << "Enter number";
	cin >> number;
	int i = 1;


	while (i <= number){
		int s = 1;	
			while (s <= i){
				s++;
				printf("*");	
			}
		printf("\n");
		i++;
	}
	
	return 0;
}
