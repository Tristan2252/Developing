#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

struct stats_t {
	int date1;
	int date2;
	char time1[1023];
	char time2[1023];
	int hour1;
	int hour2;
	int min1;
	int min2;
};

void swap(int *num1, int *num2);
int comp_num(int n1, int n2);

int main (int argc, char *argv[])
{
	char cmd;
	char input[1023] = "";
	struct stats_t stats;

	while (cmd != -1){
		cmd = getopt(argc, argv, "d:t:a:");
		switch(cmd){
		case 'd':
			strncpy(input, optarg, 1023);
			stats.date1 = atoi(strtok(input, ","));
			stats.date2 = atoi(strtok(NULL, "\0"));
			printf("%d days", comp_num(stats.date1, stats.date2));
			break;
		case 't':
			strncpy(input, optarg, 1023);
			strncpy(stats.time1, strtok(input, ","), 1023);
			strncpy(stats.time2, strtok(NULL, ","), 1023);
			
			stats.hour1 = atoi(strtok(stats.time1, ":"));
			stats.min1 = atoi(strtok(NULL, "\0"));
			stats.hour2 = atoi(strtok(stats.time2, ":"));
			stats.min2 = atoi(strtok(NULL, "\0"));

			printf("%d hours and %d minutes", comp_num(stats.hour1, stats.hour2), comp_num(stats.min1, stats.min2));
			break;
		}
	}
	return 0;
}

int comp_num(int n1, int n2)
{
	if (n1 < n2)
		swap(&n1, &n2);

	return n1 - n2;
}

void swap(int *num1, int *num2)
{	
	int tmp = *num1;
	*num1 = *num2;
	*num2 = tmp;

}
