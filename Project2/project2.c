#Hootan Hosseinzadeganbushehri



#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int PM[524288];
int D[1024][512];
int freeFrame[1024];
int is_dp;

void read_block(int b, int m)
{
	for (int i = 0; i < 512; i++)
	{
		PM[m + i] = D[b][i];
	}
}

void write_block(int b, int m)
{
	for (int i = 0; i < 512; i++)
	{
		D[b][i] = PM[m + i];
	}
}

void read_init_file(char *filename)
{
	int s, z, f, p;
	FILE *fptr;
	is_dp = 0;
	for (int i = 0; i < 524288; i++)
		PM[i] = 0;
	for (int k = 0; k < 1024; k++)
	{
		for (int i = 0; i < 512; i++)
		{
			D[k][i] = 0;
		}
		freeFrame[k] = 0;
	}
	
	if ((fptr = fopen(filename, "r")) == NULL)
	{
		printf("Error! opening %s file", filename);
		exit(1);
	}
	freeFrame[0] = freeFrame[1] = 1;

	while (fscanf(fptr, "%d %d %d", &s, &z, &f) != EOF)
	{
		PM[s * 2] = z;
		PM[s * 2 + 1] = f;
		if (f > 0)
		{
			freeFrame[f] = 1;
		}
		if (getc(fptr) == '\n')
			break;
	}
	while (fscanf(fptr, "%d %d %d", &s, &p, &f) != EOF)
	{

		
		PM[PM[2 * s + 1] * 512 + p] = f;
		if (PM[2 * s + 1] < 0) 
		{
			is_dp = 1;
			D[(PM[2 * s + 1]) * -1][p] = f;
		}
		else 
		{
			if (f > 0)
			{
				freeFrame[f] = 1;
			}
			else
			{
				D[PM[2 * s + 1]][p] = s;
			}
		}


		if (f > 0)
		{
			freeFrame[f] = 1;
		}
	
		if (getc(fptr) == '\n')
			break;
	}

	fclose(fptr);

}

int get_PA(int VA)
{
	int s, p, w, pw;

	s = VA >> 18;

	w = VA & 511;

	p = (VA & 261632) >> 9;

	pw = VA & 262143;

	if (pw >= PM[2 * s])
		return -1;
	if (PM[2 * s + 1] < 0)
	{
		for (int k = 0; k < 1024; k++)
		{
			if (freeFrame[k] == 0)
			{
				freeFrame[k] = 1;
				if (PM[2 * s + 1] < 0)
					read_block(-(PM[2 * s + 1]), k * 512);
				else
					read_block((PM[2 * s + 1]), k * 512);
				PM[2 * s + 1] = k;
				break;
			}
		}

		if (PM[PM[2 * s + 1] * 512 + p] < 0)
		{
			for (int k = 0; k < 1024; k++)
			{
				if (freeFrame[k] == 0)
				{
					freeFrame[k] = 1;
					if (PM[PM[2 * s + 1] * 512 + p] < 0)
						read_block(-(PM[PM[2 * s + 1] * 512 + p]), k * 512);
					else
						read_block((PM[PM[2 * s + 1] * 512 + p]), k * 512);
					PM[PM[2 * s + 1] * 512 + p] = k;
					break;
				}
			}


		}

		
	}
	else if (PM[PM[2*s + 1] * 512 + p] < 0)
	{
		for (int k = 0; k < 1024; k++)
		{
			if (freeFrame[k] == 0)
			{
				freeFrame[k] = 1;
				if (PM[2 * s + 1] < 0)
					read_block(-(PM[2 * s + 1]), k * 512);
				else
					read_block((PM[2 * s + 1]), k * 512);
				PM[PM[2*s + 1] * 512 + p] = k;
				break;
			}
		}

	}
	return PM[PM[2 * s + 1] * 512 + p] * 512 + w;
}

void read_input_file(char *filename)
{
	int VA;
	FILE *fptr, *optr;
	if(is_dp == 0)
		optr = fopen("output-no-dp.txt", "w");
	else
		optr = fopen("output-dp.txt", "w");

	if ((fptr = fopen(filename, "r")) == NULL)
	{
		printf("Error! opening %s file", filename);
		exit(1);
	}

	while (fscanf(fptr, "%d", &VA) != EOF)
	{
		int PA = get_PA(VA);
		fprintf(optr, "%d ", PA);
	}
	fclose(optr);
	fclose(fptr);
}

int main(int argc, char **args)
{
	if (argc != 3)
	{
		printf("There is not init and input file name please enter again!");
		return -1;
	}
	read_init_file(args[1]);
	read_input_file(args[2]);
	return 0;
}