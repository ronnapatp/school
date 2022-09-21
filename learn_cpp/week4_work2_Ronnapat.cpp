#include <iostream>
using namespace std;

int main()
{
	
	char key = 's';
	string message;
	string output;
	
	cout << "Enter string: ";
	cin >> message;
	
	for(int i = 0; i < sizeof(message); i++){
		if(message[i]!=0)
		{
			printf("%c",message[i] ^ key);
		}
		output[i] = message[i] ^ key;
	}
	cout << "\n" << "Encrypt + Decrypt: ";
	
	for(int i = 0; i < sizeof(output); i++){
		printf("%c",output[i] ^ key);
	}
	
	
	return 0;
}
