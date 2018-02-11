#include <stdio.h>
#include <stdlib.h>

int main()
{
	int size=32;
	int tab[size];
	tab[0]=1 ; tab[1]=2;
	int i=2, somme=2;
	for (i=2;i<32;i++)
	{
		tab[i]=tab[i-1]+tab[i-2];
		printf("%d\n",tab[i]);
		if (tab[i]%2==0)
		{
			somme=somme+tab[i];
		}	
	}
	printf("la somme des éléments de la suite est : %d\n",somme);  
	return 0;
}
