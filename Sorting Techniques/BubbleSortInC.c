#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(int array[], int n) {
  int i, j, temp;

  for (i = 0; i < n - 1; i++) {
    for (j = 0; j < n - i - 1; j++) {
      if (array[j] > array[j + 1]) {
        temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
}

#define array_size 4000

int main() {
  int array[array_size];

  srand(time(0));

  // Generate random numbers and store them in the array
  for (int i = 0; i < array_size; i++) {
    array[i] = rand() % 1000 +1;
  }
  int n = sizeof(array) / sizeof(array[0]);
  
//   for (int i = 0; i < n; i++) {
//     printf("%d ", array[i]);
//   }
  
  clock_t start = clock();
  bubbleSort(array, n);
  clock_t end = clock();

//   printf("Sorted array: \n");
//   for (int i = 0; i < n; i++) {
//     printf("%d ", array[i]);
//   }
  printf("\n");
  
  double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

  // Calculate the CPU utilization percentage
  double utilization = (time_taken / CLOCKS_PER_SEC) * 100.0;
  printf("CPU utilization: %f%%\n", utilization);
  printf("time: %f\n", time_taken);

  return 0;
}
