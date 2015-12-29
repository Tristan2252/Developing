
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define LEN 1023
#define DEBUG 

char *parce(char c, int off_start, char *string);
char *parce_range(char c, int off_start, int off_end, char *string);

int main(void)
{
	char list[LEN][LEN];
	char buf[LEN];
	
	printf("\n\t>>> INPUT <<<\n");
	int line = 0;
	while (fgets(buf, LEN, stdin)){
		if((buf[0] == 'd') | (buf[0] == '-')){
			strncpy(list[line], buf, LEN);
			printf("%s", list[line]);
			line++;
		}
	}
	puts("");

#ifdef DEBUG
	int i;
	printf("Permissions: Links: Owner:\n");
	for (i = 0; i < line; i++){
		printf("%s\n", parce_range(' ', 0, 2, list[i]));
	}
#endif

	return 0;
}

/**
 * Function gets the characters between a range of iterations of a character, 
 * for example if the user wanted all the character between the 1st and 3rd iteration of 't'
 * @param c the character to search for
 * @param off_start the offset starting point or the iteration at with to start the range
 * @param off_end the end of the range or the iteration of c at witch to stop
 * @param string the string to search
 * @return new_str the string within the range
 */
char *parce_range(char c, int off_start, int off_end, char *string){
	char *new_str = malloc(LEN * sizeof(char));
	int cnt = 0;  // keeps track of c iterations
	int index = 0; // keeps track of indexes of new string
	int i;
	for (i = 0; i < strnlen(string, LEN); i++){
		if (string[i] == c)
			cnt++;
		if (cnt >= off_start && cnt <= off_end){
			if (index == 0 && string[i] == c) // fixes adding first character that is = c
				;
			else{
				new_str[index] = string[i]; // adding characters to new string
				index++;

			}
		}
	}

	return new_str;
}

