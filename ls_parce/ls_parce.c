
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define LEN 1023
#define DEBUG 

char *strip_newline(char *string);
char *parce_range(char c, int off_start, int off_end, char *string);

int main(void)
{
	char list[LEN][LEN]; // list of strings
	char buf[LEN];
	int line = 0; // input line counter
	
	printf("\n\t>>> INPUT <<<\n");
	while (fgets(buf, LEN, stdin)){
		strncpy(list[line], buf, LEN);
		printf("%s", list[line]);
		line++;
	}

	puts("");

	int i;
	for (i = 0; i < line; i++){
		printf("%s\n", parce_range(' ', 0, 3, list[i]));
	}

	return 0;
}

/**
 * Function gets the characters between a range of iterations of a character, 
 * for example if the user wanted all the character between the 1st and 3rd iteration of 't
 * NOTE: 0, 0 will get the string bwtween the first letter and the first iteration of c'
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

char *strip_newline(char *string)
{
	char *strip_str;	
	return strip_str;
}
