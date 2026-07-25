#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Arr {
    size_t cap;
    size_t i;
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


bool append(int item, struct Arr **arr) {
    if ((*arr)->cap <= ((*arr)->i+1) * sizeof((*arr)->data[0])) {
        void *temp = realloc(*arr, sizeof(**arr) * ((*arr)->cap*=2));
        if (temp == NULL) {
            return false;
        }
        *arr = temp;
    }
    *((*arr)->data + (*arr)->i) = item;
    (*arr)->i++;
    return true;
}

void append_arr(struct Arr **arr, size_t n) {
    for (int i = 0; i <= n; i++) {
        printf("*arr: %p\n", arr);
        printf("Cap: %zu\n", (*arr)->cap);
        if (append(i, arr) == false) {
            return;
        }
    }
    for (int *ptr = (*arr)->data; ptr < (*arr)->data+(*arr)->i; ptr++) {
        printf("Item: %d\n", *ptr);
    }
}

int main() {
    struct Arr *arr;
    int item_count = 4;
    size_t     cap = sizeof(arr->data[0]) * item_count;

    arr = malloc(sizeof(*arr) + cap);
    if (arr == NULL) {
        return 1;
    }
    *arr = (struct Arr) {
        .cap = cap,
        .i = 0
    };
    append_arr(&arr, 12);
    free(arr);
}
