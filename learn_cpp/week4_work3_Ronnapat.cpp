#include <iostream>
using namespace std;

int main()
{
	int score{};
	
	cout << "Enter your score: ";
	cin >> score;
	
	if(score < 0 || score > 100){
		cout << "Please enter point between 1-100 marks";
	} else {
		if(score <= 100 && score >= 90){
			cout << "Grade A+";
		} else if(score <= 89 && score >= 80){
			cout << "Grade A";
		} else if(score <= 79 && score >= 70){
			cout << "Grade B";
		} else if(score <= 69 && score >= 60){
			cout << "Grade C";
		} else if(score <= 59 && score >= 50){
			cout << "Grade D";
		} else if(score <= 50){
			cout << "Grade F";
		}
	}

	
	return 0;
}
