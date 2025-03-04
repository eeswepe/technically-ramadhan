#include <stdio.h>
#include <string.h>

int word_score(const char *word) {
  int sum = 0;
  for (int i = 0; i < strlen(word); i++) {
    sum += word[i] - 'a' + 1;
  }
  return sum;
}

int main() {
  int test = word_score("friendship");
  printf("%d", test);
}
