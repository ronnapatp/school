#include <iostream>
using namespace std;

int main(){
	char op;
	int first_number, second_number, sum;
	
	cout << "Enter an operator (+, -, *, /): ";
	cin >> op;
	
	cout << "Enter two numbers: ";
	cin >> first_number >> second_number;
	
	switch(op){
		case '+':
			printf("%i + %i = %i", first_number, second_number, first_number + second_number);
			break;
		case '-':
			printf("%i - %i = %i", first_number, second_number, first_number - second_number);
			break;
		case '*':
			printf("%i * %i = %i", first_number, second_number, first_number * second_number);
			break;
		case '/':
			printf("%i / %i = %i", first_number, second_number, first_number / second_number);
			break;
	}
	
	
	 return 0;
}
