#include <ctype.h>
#include <stdio.h>

char *to_weird_case(char *string) {
  // mutate string and return it
  int counter = 0;
  for (int i = 0; string[i] != '\0'; i++) {
    if (string[i] == ' ') {
      counter = 0;
      continue;
    }
    if (counter % 2 == 0) {
      string[i] = toupper(string[i]);
    } else {
      string[i] = tolower(string[i]);
    }
    counter++;
  }
  return string;
}

int main() {
  char myString[] = "Weird string case";
  printf("%s\n", to_weird_case(myString));
}
