
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define LEN 1023
//#define DEBUG 

void help_menu(void);
char *strip_newline(char *string);
char *parce_range(char c, int off_start, int off_end, char *string);

int main(int argc, char *argv[])
{
	char list[LEN][LEN]; 	// list of strings to store input lines
	char input[LEN] = ""; 	// string to coppy input into
	char *token; 		// used with strtok to get indevidual lines of the input
	int line = 0; 		// input line counter
	char delim = 32; 	// delimeter for parcing. 32 is SPACE, default setting
	int start = 0;
	int end = 0;
	
	char cmd;
	while (cmd != -1){
		// NOTE to self, ':' need to falow each flag representing the arg
		cmd = getopt(argc, argv, "s:e:i:d:h");
		switch (cmd){
		case 's':
			start = atoi(optarg);
			break;
		case 'e':
			end = atoi(optarg);
			break;
		case 'i':
			strncpy(input, optarg, LEN);
			break;
		case 'd':
			delim = optarg[0];
			break;
		case 'h':
			help_menu();
			return 0;
		}
	}
	
	token = strtok(input, "\n"); // setup first token
	while (token){
		strncpy(list[line], token, LEN);
		line++;
		token = strtok(NULL, "\n");
	}

	int i;
	for (i = 0; i < line; i++){
		printf("%s\n", parce_range(delim, start, end, list[i]));
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
			if (!(index == 0 && string[i] == c)){ // fixes adding first character that is = c
				new_str[index] = string[i]; // adding characters to new string
				index++;
			}
		}
	}

	return strip_newline(new_str); // strip neline if one
}

/**
 * Function takis in a string and tests for newline characters, if found they
 * are taken out be excluding them from the string being retuned
 * @param string the string to test
 * @return the striped string
 */
char *strip_newline(char *string)
{
	char *strip_str = malloc(LEN * sizeof(char)); // set size large for large strings
	int i;

	for (i = 0; i < strnlen(string, LEN); i++){
		if (string[i] != '\n') // if = to newline character is not added to string
			strip_str[i] = string[i];
	}
		
	return strip_str;
}

/**
 * Prints help menu for user to see accepted commands
 */
void help_menu(void){
	puts("");
	puts("BASIC USAGE");
	puts("-i <string> the string to parce");
	puts("");
	puts("OPTIONAL COMMANDS");
	puts("-s <int> iteration of delimiter to start parce");
	puts("-e <int> iteration of delimiter to end parce");
	puts("-d <char> parcing delimiter");
	puts("-h help menu");
	puts("");
	puts("Default values, for optional settings");
	puts("-s = 0");
	puts("-e = 0");
	puts("-d = ' '");
	puts("");
}
