#include <iostream>
using namespace std;

int main()
{
	string name[2];
	float scoreone[2], scoretwo[2], scorethree[2];

	cout << "Enter Data of students:\n";	
	for(int i = 0; i < 2; i++){
		cout << "Input student number " << i+1 << "\n\n";
		cout << "Input name: ";
		cin >> name[i];
		cout << "Input score1: ";
		cin >> scoreone[i];
		cout << "Input score2: ";
		cin >> scoretwo[i];
		cout << "Input score3: ";
		cin >> scorethree[i];
	}
	
	cout << "\nDisplaying information: \n";
	for(int y = 0; y < 2; y++ ){
		cout << "All number: " << y+1 << "\n";
		cout << "name: " << name[y] << "\n";
		cout << "score1: " << scoreone[y] << "\n";
		cout << "score2: " << scoretwo[y] << "\n";
		cout << "score3: " << scorethree[y] << "\n";
	}
	

	
	return 0;
}
