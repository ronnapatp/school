#include <iostream>
using namespace std;

int main()
{

	char ch1, ch2, ch3;
	int x = 65;
	
	cout << "Enter character 1: ";
	cin >> ch1;
	
	cout << "Enter character 2: ";
	cin >> ch2;
	
	cout << "Enter character 3: ";
	cin >> ch3;
	
	cout << "Character 1 ascii code is " << int(ch1) << ".\n";
	printf("Xor for character 1 is %i.\n",  x ^ int(ch1));

	cout << "Character 2 ascii code is " << int(ch2) << ".\n";
	printf("Xor for character 2 is %i.\n",  x ^ int(ch2));

	cout << "Character 3 ascii code is " << int(ch3) << ".\n";
	printf("Xor for character 3 is %i.\n",  x ^ int(ch3));

	
	return 0;
}
