#include <iostream> 
using namespace std;

int main(){
	
	string username, password;
	
	cout << "Enter username: ";
	cin >> username;
	
	cout << "Enter password: ";
	cin >> password;
	
	if(username != "ronnapat" && password != "hello"){
		printf("Invalid username or password");
	} else {
		printf("Login success");
	}	
	
	return 0;
}
