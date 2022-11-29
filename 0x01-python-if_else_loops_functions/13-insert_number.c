#include "lists.h"

/**
 * insert_node - Insert node in order mode to listint_t
 * @head: head of list
 * @number: num to be added
 * Return: the address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *prev = *head;

	if (!new)
		return (0);

	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (prev->next)
	{
		if ((prev->next)->n >= number)
		{
			new->next = prev->next;
			prev->next = new;
			return (new);
		}
		prev = prev->next;
	}

	new->next = NULL;
	prev->next = new;
	return (new);
}
