#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev = NULL, *tmp;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    slow = *head;
    fast = *head;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        tmp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = tmp;
    }

    if (fast != NULL)
        slow = slow->next;

    while (prev != NULL)
    {
        if (prev->n != slow->n)
            return (0);

        prev = prev->next;
        slow = slow->next;
    }

    return (1);
}