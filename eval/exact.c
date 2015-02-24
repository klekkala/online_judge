#include<stdio.h>

int main(int argc,char *argv[])
{
	int retStatus = 0;
	FILE *f1 = fopen(argv[1],"r");
	FILE *f2 = fopen(argv[2],"r");
	char ch1,ch2;
	fscanf(f1,"%c",&ch1); fscanf(f2,"%c",&ch2);
	printf("%c %c\n", ch1, ch2);
	while(ch1==ch2)
	{
		if(feof(f1) && !feof(f2) || !feof(f1) && feof(f2))
		{
			fclose(f1);
			fclose(f2);
			return 1;
		}
		if(feof(f1) && feof(f2))
			return 0;
		fscanf(f1,"%c",&ch1); fscanf(f2,"%c",&ch2);
	}
	if(!feof(f1) || !feof(f2))
	{
		fclose(f1);
		fclose(f2);
		return 1;
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
