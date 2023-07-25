#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Structure for a doubly linked list node
struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

// Function to create a new node for the doubly linked list
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

// Function to insert a node at the end of the doubly linked list
void insertEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* current = *head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
}

// Function to print the doubly linked list
void printList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

// Function to merge two sorted linked lists
struct Node* merge(struct Node* left, struct Node* right) {
    // Create a dummy node to hold the merged list
    struct Node* dummy = createNode(0);
    struct Node* tail = dummy;

    // Merge the two sorted lists
    while (left != NULL && right != NULL) {
        if (left->data <= right->data) {
            tail->next = left;
            left->prev = tail;
            left = left->next;
        } else {
            tail->next = right;
            right->prev = tail;
            right = right->next;
        }
        tail = tail->next;
    }

    // Append any remaining nodes from the left or right list
    if (left != NULL) {
        tail->next = left;
        left->prev = tail;
    } else {
        tail->next = right;
        right->prev = tail;
    }

    // Update the prev pointer for the merged list
    struct Node* head = dummy->next;
    if (head != NULL) {
        head->prev = NULL;
    }

    // Free the dummy node
    free(dummy);

    return head;
}

// Function to perform merge sort on a linked list
struct Node* mergeSort(struct Node* head) {
    // Base case: if the list is empty or has only one node, it is already sorted
    if (head == NULL || head->next == NULL) {
        return head;
    }

    // Split the list into two halves
    struct Node* slow = head;
    struct Node* fast = head->next;
    while (fast != NULL) {
        fast = fast->next;
        if (fast != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
    }
    struct Node* left = head;
    struct Node* right = slow->next;
    slow->next = NULL;
    if (right != NULL) {
        right->prev = NULL;
    }

    // Recursively sort the left and right halves
    left = mergeSort(left);
    right = mergeSort(right);

    // Merge the sorted left and right halves
    return merge(left, right);
}

// Function to free the memory allocated for the doubly linked list
void freeList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        struct Node* temp = current;
        current = current->next;
        free(temp);
    }
}

int main() {
    struct Node* head = NULL;
    int numbers[200000];
    int i, j;
    int temp;

    // Seed the random number generator
    srand(time(0));

    // Generate an array of 2000 unique random numbers between 1 and 2000
    for (i = 0; i < 200000; i++) {
        numbers[i] = i + 1;
    }
    for (i = 0; i < 200000; i++) {
        j = rand() % 200000;
        temp = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = temp;
    }

    // Insert each number in the array into the doubly linked list
    int n = sizeof(numbers) / sizeof(numbers[0]);
    for (i = 0; i < n; i++) {
        insertEnd(&head, numbers[i]);
    }

    printf("Original list: ");
    printList(head);

    // Sort the list using merge sort
    head = mergeSort(head);

    // Print the sorted list
    printf("Sorted List: ");
    printList(head);

    // Free the memory allocated for the doubly linked list
    freeList(head);
    return 0;
}



// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// // Structure for a doubly linked list node
// struct Node {
//     int data;
//     struct Node* next;
//     struct Node* prev;
// };

// // Function to create a new node for the doubly linked list
// struct Node* createNode(int data) {
//     struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
//     newNode->data = data;
//     newNode->next = NULL;
//     newNode->prev = NULL;
//     return newNode;
// }

// // Function to insert a node at the end of the doubly linked list
// void insertEnd(struct Node** head, int data) {
//     struct Node* newNode = createNode(data);
//     if (*head == NULL) {
//         *head = newNode;
//     } else {
//         struct Node* current = *head;
//         while (current->next != NULL) {
//             current = current->next;
//         }
//         current->next = newNode;
//         newNode->prev = current;
//     }
// }

// // Function to print the doubly linked list
// void printList(struct Node* head) {
//     struct Node* current = head;
//     while (current != NULL) {
//         printf("%d ", current->data);
//         current = current->next;
//     }
//     printf("\n");
// }

// // Function to free the doubly linked list
// void freeList(struct Node* head) {
//     struct Node* current = head;
//     while (current != NULL) {
//         struct Node* temp = current;
//         current = current->next;
//         free(temp);
//     }
// }

// // Function to perform bubble sort on a linked list
// void bubbleSort(struct Node* head) {
//     int swappedped;
//     struct Node* ptr1;
//     struct Node* lptr = NULL;

//     // If list is empty, return
//     if (head == NULL) {
//         return;
//     }

//     do {
//         swappedped = 0;
//         ptr1 = head;

//         while (ptr1->next != lptr) {
//             if (ptr1->data > ptr1->next->data) {
//                 // swapped the nodes
//                 int temp = ptr1->data;
//                 ptr1->data = ptr1->next->data;
//                 ptr1->next->data = temp;
//                 swappedped = 1;
//             }
//             ptr1 = ptr1->next;
//         }
//         lptr = ptr1;
//     } while (swappedped);
// }

// int main() {
//     struct Node* head = NULL;
//     int numbers[2000000];
//     int i, j;
//     int temp;

//     // Seed the random number generator
//     srand(time(0));

//     // Generate an array of 2000 unique random numbers between 1 and 2000
//     for (i = 0; i < 2000000; i++) {
//         numbers[i] = i + 1;
//     }
//     for (i = 0; i < 2000000; i++) {
//         j = rand() % 2000000;
//         temp = numbers[i];
//         numbers[i] = numbers[j];
//         numbers[j] = temp;
//     }

//     // Insert each number in the array into the doubly linked list
//     int n = sizeof(numbers) / sizeof(numbers[0]);
//     for (i = 0; i < n; i++) {
//         insertEnd(&head, numbers[i]);
//     }

//     // Sort the list using bubble sort
//     bubbleSort(head);

//     // Print the sorted list
//     printf("Sorted List: ");
//     printList(head);

//     // Free the memory allocated for the doubly linked list
//     freeList(head);
//     return 0;
// }