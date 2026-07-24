#include <stdio.h>
#include <stdlib.h>

struct Arr {
    int cap;
    int i;
    int data[];
};

// void * append(void *item, size_t s, struct Arr *arr) {
//     arr->i++;
//     if (arr->cap <= arr->i+1) {
//         void *ptr = realloc(&(arr->data[0]), sizeof(*arr->data) * (arr->cap*=2));
//         if (item != ptr) {
//             return ptr;
//         }
//     }
//     return NULL;
// }

void *append(int *item, struct Arr *arr) {
    if (arr->cap <= arr->i+1) {
        arr = realloc(arr, sizeof(arr) + sizeof(*item) * (arr->cap*=2));
    }
    arr->i++;
    *(arr->data + arr->i) = *item;
    return arr;
}


int main() {
    struct Arr *arr;
    int cap;
    arr = malloc(sizeof(*arr) + sizeof(arr->data[0]) * cap);
    arr->cap=cap;
    arr->i=0;

    arr = append(1, arr);
    arr = append(2, arr);
    arr = append(3, arr);
    arr = append(4, arr);
    arr = append(5, arr);
    arr = append(6, arr);

    for (int *ptr = arr-arr->i; arr < (arr+arr->i); ptr++) {
        printf("Item: %d", *ptr);
    }

    free(arr);
}
