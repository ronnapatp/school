#include <iostream>
using namespace std;

int main()
{
	int grade;
	
	cout << "Enter your grade: ";
	cin >> grade;
	
	if(grade <= 100 && grade >= 90){
		cout << "Grade A+";
	} else if (grade <= 89 && grade >= 80){
		cout << "Grade A";
	} else if (grade <= 79 && grade >= 70){
		cout << "Grade B";
	} else if (grade <= 69 && grade >= 60){
		cout << "Grade C";
	} else if (grade <= 59 && grade >= 50){
		cout << "Grade C";
	} else if (grade < 50 && grade >= 0){
		cout << "Grade F";
	} else {
		cout << "Please enter your grade again (0-100): ";
	};
	
	return 0;
}
