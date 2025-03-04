#include <stdio.h>

void count_positives_sum_negatives(int *values, size_t count,
                                   int *positivesCount, int *negativesSum) {
  // Please store the positives count in the memory, pointed to
  // by the positivesCount parameter.

  // Please store the negatives sum in the memory, pointed to
  // by the negativesSum parameter.
  for (int i = 0; i < count; i++) {
    if (values[i] > 0) {
      *positivesCount += 1;
    } else {
      *negativesSum += values[i];
    }
  }
}

int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15};

int main() {
  int positivesCount = 0;
  int negativesSum = 0;
  count_positives_sum_negatives(data, sizeof(data) / sizeof(data[0]),
                                &positivesCount, &negativesSum);
  printf("%d %d\n", positivesCount, negativesSum);
  return 0;
}
