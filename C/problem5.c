#include <stdio.h>
#include <stdlib.h>


int ppcm(int a, int b);

int main()
{
	int i = 2;
	int init = 1;
	while (i!=20)
	{
		init = ppcm(init,i);
		i += 1;
	}
	printf("%d\n",init);
	return 0;
}

int ppcm(int a, int b)
{
	int c=a;
	int d=b;
	while (a!=b)
	{
		if (a>b)
			b+=d;
		else if (a<b)
			a+=c;
	}
	return a;
}


