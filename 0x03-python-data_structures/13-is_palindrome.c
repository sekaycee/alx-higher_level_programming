#include "lists.h"

/**
 * reverse - reverse the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */
void reverse(listint_t **h_r)
{
	listint_t *prev, *curr, *next;

	prev = NULL;
	curr = *h_r;
	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*h_r = prev;
}

/**
 * compare - compare each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1, *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 && tmp2)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (!tmp1 && !tmp2)
		return (1);

	return (0);
}

/**
 * is_palindrome - check if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;
	if (*head && (*head)->next)
	{
		while (fast && fast->next)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);
		if (middle)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
