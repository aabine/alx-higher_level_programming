#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: singly linked list to check
 *
 * Return: 1 if list has a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
