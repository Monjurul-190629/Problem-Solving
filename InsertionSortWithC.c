#include <stdio.h>

void insertionSort(int arr[], int n){
    int key, i, j;
    for(i = 1; i < n; i++){
        key = arr[i];
        j = i - 1;
        while ((j >= 0) && (key < arr[j])){
            arr[j + 1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = key;
    }
}

int main(){
    int arr[] = {22, 4, 1, 3, 5};
    int n;
    n = sizeof(arr) / sizeof(arr[0]);
    insertionSort(arr, n);
    printf("Sorted Array: ");
    for(int i = 0; i< n; i++){
        printf("%d ", arr[i]);
    }
    return 0;
}