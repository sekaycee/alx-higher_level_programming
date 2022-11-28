#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a loop in it
 * @list: pointer to the head of listint_t
 * Return: 0 if there is no loop. 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *p1 = NULL, *p2 = NULL;

	if (!list)
		return (0);

	p1 = list;
	p2 = list;
	while (p1 && p2 && p2->next)
	{
		p1 = p1->next;
		p2 = p2->next->next;
		if (p1 == p2)
			return (1);
	}
	return (0);
}

