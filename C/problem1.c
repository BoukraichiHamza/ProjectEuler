#include <stdio.h>
#include <stdlib.h>

int main()
{
	int sum=0;
	int i;
	for (i=0;i<1000;i++)
	{
		if (i%3==0 || i%5==0)
		{
			sum=sum+i;
		}
	}
	printf("the sum of all the multiples of 3 or 5 below 1000 is : %d\n",sum);
}
