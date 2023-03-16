#include "lists.h"
/**
 * add_dnodeint_end - add new node at the end
 * @head: pointer to the first node
 * @n: data of the new node
 * Return: address of new element, or NULL if failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *last_node, *new_node = malloc(sizeof(dlistint_t));
	int i = n;

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = i;
	new_node->next = NULL;

	if (*head == NULL)
	{
		new_node->prev = NULL;
		*head = new_node;
		return (new_node);
	}
	last_node = *head;
	while (last_node->next != NULL)
	{
		last_node = last_node->next;
	}
	last_node->next = new_node;
	new_node->prev = last_node;
	return (new_node);
}
