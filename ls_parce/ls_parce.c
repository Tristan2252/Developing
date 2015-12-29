
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
			printf("%s", list[line]);
			line++;
		}
	}
	
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
	printf("%s", parce_range(' ', 4, 6, list[4]));

	return 0;
}

char *parce_range(char c, int off_start, int off_end, char *string){
	int cnt = 0;
	int i;
	for (i = 0; i < strnlen(string, LEN); i++){
		if (string[i] == c && cnt == off_start)
			parce(c, off_end-off_start, &string[i]);
		else if (string[i] == c){
			printf("%s", &string[i]);
			cnt++;
		}
	}

	return string;
}
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
