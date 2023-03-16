#include "lists.h"
/**
 * add_dnodeint - add node at the beginning of list
 * @head: pointer
 * @n: new node data
 * Return:the address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *tmp, *new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = NULL;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (*head);
	}
	tmp = *head;
	new_node->next = tmp;
	tmp->prev = new_node;
	*head = new_node;
	return (new_node);
}
