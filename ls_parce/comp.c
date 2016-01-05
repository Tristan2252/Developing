#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int comp_date(int n1, int n2);

int main (int argc, char *argv[])
{
	char cmd;
	char input[1023] = "";
	int num1;
	int num2;

	while (cmd != -1){
		cmd = getopt(argc, argv, "d:t:a:");
		switch(cmd){
		case 'd':
			strncpy(input, optarg, 1023);
			num1 = atoi(strtok(input, ","));
			num2 = atoi(strtok(NULL, "\0"));
			printf("%d", comp_date(num1, num2));
			break;
		case 't':
			break;
		case 'a':
			break;
		}
	}
	return 0;
}

int comp_date(int n1, int n2)
{
	if (n1 < n2){
		int tmp = n1;
		n1 = n2;
		n2 = tmp;
	}
	return n1 - n2;
}
