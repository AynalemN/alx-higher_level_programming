#include "lists.h"
/**
 * free_dlistint - free the list
 * @head:the struct
 * @Return: void
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;

	while (head)
	{
		tmp = head;
		head = head->next;
		free(tmp);
	}
}
