#include <iostream>
using namespace std;

int main(){
	int x = 23, y = 34;
	cout << "Before swapping x = " << x << " and y = " << y << ".\n";
	
	x = x^y;
	y = x^y;
	x = x^y;
	
	cout << "After swapping x = " << x << " and y = " << y << ".\n";
	
	return 0;
}
