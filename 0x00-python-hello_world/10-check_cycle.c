#include "lists.h"
/**
 * check_cycle - checks if the linked list has a cycle
 * @list: a listint_
 * Return: 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *node1, *node2;

	node1 = list;
	node2 = list;

	while (node1 != NULL && node1->next != NULL)
	{
		node1 = node1->next->next;
		node2 = node2->next;

		if (node1 == node2)
		{
			return (1);
		}
	}
	return (0);
}
