#include <iostream>
using namespace std;

int main()
{
	string search;
	string name[5] = {"a","b","c","d","e"};
	int scoreone[5] = {1,2,3,4,5};
	int scoretwo[5] = {45,45,23,56,45};
	int scorethree[5] = {8,6,9,10,9};
	
	cout << "Input name search : ";
	cin >> search;
	
	for(int i = 0; i < 5; i++){
		if(search == name[i]){
			cout << "Name: " << name[i] << "\n";
			cout << "Score1 : " << scoreone[i] << "\n";
			cout << "Score2 : " << scoretwo[i] << "\n";
			cout << "Score3 : " << scorethree[i] << "\n"; 
		} 
	}
	

	
	return 0;
}
