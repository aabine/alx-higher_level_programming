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
        if (current->n == number)
        {
            free(new);
            return (NULL);
        }
        prev = current;
        current = current->next;
    }

    new->next = current;
    prev->next = new;

    return (new);
}