#include <stdio.h>

int word_score(const char *word) {
  int sum = 0;
  while (*word) {
    sum += *word - 'a' + 1;
    word++;
  }
  return sum;
}

int main() {
  int test = word_score("friendship");
  printf("%d", test);
}
