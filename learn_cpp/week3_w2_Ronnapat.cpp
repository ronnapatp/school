#include <iostream>
using namespace std;

int main()
{
  int score;
  
  cout << "Enter your score";
  cin >> score;
    
  if(score <= 0 || score > 100){
  	cout << "Enter your score between 1-100" << endl;
  }
  
  switch(score/10){
  	case 9:
  		cout << "Grade A";
  		break;
  	case 8:
  		cout << "Grade B";
  		break;
  	case 7:
  		cout << "Grade C";
  		break;
  	case 6:
  		cout << "Grade D";
  		break;
  	case 5:
  		cout << "Grade E";
  		break;
  	default:
  		cout << "Grade F";
  		break;
  }
  
  return 0;
}
