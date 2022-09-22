#include <iostream>
using namespace std;

int main()
{
	string name[2];
	int scoreone[2], scoretwo[2], scorethree[2], sum[2];

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
		
		sum[i] = scoreone[i] + scoretwo[i] + scorethree[i];
	}
	
	cout << "\nDisplaying information: \n";
	for(int y = 0; y < 2; y++ ){
		cout << "All number: " << y+1 << "\n";
		cout << "name: " << name[y] << "\n";
		cout << "score1: " << scoreone[y] << "\n";
		cout << "score2: " << scoretwo[y] << "\n";
		cout << "score3: " << scorethree[y] << "\n";
		cout << "sum :" << sum[y] << "\n";
	}
	
	cout << "\n _______________ \n\n";
	
	cout << "All sum : " << sum[0] + sum[1] << "\n";
	cout << "Average : " << (sum[0] + sum[1])/2;
	

	
	return 0;
}
