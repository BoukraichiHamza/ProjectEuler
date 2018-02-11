#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// We have to set a function that returns directly the biggest plindrome
// for now my program gives all the multiplications that have a palindrome as a result

void toString(char [], int);
int isPalindrome(char []);

int main()
{
	char str[20];
	int produit;
	int i, j;
	for (i=100;i<=999;i++)
	{
		for (j=i;j<=999;j++)
		{
			produit = i*j;
			
			toString(str, produit);
			
			if ( (isPalindrome(str)==1) )
				printf("this is a palindrome\n : %d * %d = %d \n",i,j,produit); 
		}
	}
	
}

int isPalindrome(char str[])
{
	int len=strlen(str), i;
	for (i=0;i<len/2;i++)
	{
		if (str[i]!=str[len-1-i])
		{
			return 0;
		}
	}
	return 1;
}

void toString(char str[], int num)
{
    int i, rem, len = 0, n;
 
    n = num;						// we create a variable n equal to num in order to do successive divisions by 10
    while (n != 0)
    {
        len++;
        n /= 10;
    }
    for (i = 0; i < len; i++)
    {
        rem = num % 10;
        num = num / 10;
        str[len - (i + 1)] = rem + '0';
    }
    str[len] = '\0';
}






