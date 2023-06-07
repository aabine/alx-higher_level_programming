#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *prev;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL || number < (*head)->n)
    {
        new->next = *head;
        *head = new;
        return (new);
    }

    current = *head;
    prev = NULL;

    while (current != NULL && current->n <= number)
    {
        prev = current;
        current = current->next;
    }

    new->next = current;
    if (prev != NULL && prev->n == number) {
        free(new);
        return (NULL);
    }
    else if (prev == NULL)
        *head = new;
    else
        prev->next = new;

    return (new);
}