
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define LEN 1023
//#define DEBUG 

char *parce(char c, int off_start, char *string);
char *parce_range(char c, int off_start, int off_end, char *string);

int main(void)
{
	char list[LEN][LEN];
	char buf[LEN];
	
	int line = 0;
	while (fgets(buf, LEN, stdin)){
		if((buf[0] == 'd') | (buf[0] == '-')){
			strncpy(list[line], buf, LEN);
			//printf("%s", list[line]);
			line++;
		}
	}
/*	
#ifdef DEBUG
	int i;
	char *perm_flags;
	char *link_num;
	char *owner;
	printf("Permissions: Links: Owner:\n");
	for (i = 0; i < line; i++){
		perm_flags = strtok(list[i], " ");
		link_num = strtok(NULL, " ");
		owner = strtok(NULL, " ");
		printf("  %s  %s  %s\n", perm_flags, link_num, owner);
	}
#endif

	puts("");

//	parce(' ', 4, list[1]);
//
*/
//	printf("%s\n", parce_range(' ', 5, 7, list[4]));
	printf("%s\n", parce_range('t', 1, 3, list[4]));

	return 0;
}

char *parce_range(char c, int off_start, int off_end, char *string){
	char *new_str = malloc(LEN * sizeof(char));
	int cnt = 0; 
	int cnt1 = 0;
	int i;
	for (i = 0; i < strnlen(string, LEN); i++){
		if (string[i] == c)
			cnt++;
		if (cnt >= off_start && cnt <= off_end){
			new_str[cnt1] = string[i];
			cnt1++;
		}
	}

	return new_str;
}

/*
char *parce(char c, int off_start, char *string){
	int cnt = 0;
	int i;
	for (i = 0; i < strnlen(string, LEN); i++){
		if (string[i] == c && cnt == off_start)
			;
		else if (string[i] == c){
			printf("%s", &string[i]);
			cnt++;
		}
	}

	return string;
}
*/
