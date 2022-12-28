
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  // Seed the random number generator with the current time
  srand(time(0));

  // Generate a random number between 1 and 10
  int randomNumber = rand() % 1000 + 1;

  printf("Random number: %d\n", randomNumber);

  return 0;
}