/* Written by Barnaan2;
email barnaantekalign@gmail.com;
i did this with the smallest possible line of code;
secure text delivery*/
#include <iostream>
#include <cstring>
using namespace std;
void lock(char a[100], int x, int y);
void unlock(char a[100], int x, int y);

int main()

{
// limiting the number of characters to make it easily compiled 
char a[100];
	int n, w, k;
	cout << "write any string you want to lock or unlock" << endl;
	cin.get(a, 100);
	cout << "insert your a format to lock (0 to 10)" << endl;
	cin >> w;
	k = w + 1;
            n = strlen(a);
	cout << endl;
//taking user input to do the required operation
	cout << "press A to lock the text" << endl
		 << "press B to unlock the locked text" << endl;
	char h;
	cin >> h;
	if (h == 'A')
	{
	lock(a, n, k);
	}
	else if (h == 'B')
	{
unlock(a, n, k);
	}
	
	else cout << " unqulifed key touched please try agin!";
	

	return 0;
}
//  function to lock the text
	void lock(char a[100], int x, int y)
	{
		for (int i = 0; i < x; i++)
		{
			a[i] = a[i] + y;
			cout << a[i];
		}
	}
// function to unlock the text
	void unlock(char a[100], int x, int y)
	{
		for (int i = 0; i < x; i++)
		{
			a[i] = a[i] - y;
			cout << a[i];
		}
	}
