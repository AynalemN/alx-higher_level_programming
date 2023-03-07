#include "lists.h"
/**
 * insert_node - insert node in a sorted list
 * @head: pointer to the head node
 * @number: integer value of the new node
 * Return: address of new node if success else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	current = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (!current || new_node->n < current->n)
	{
		new_node->next = current;
		return (*head = new_node);
	}

	while (current)
	{
		if (!current->next || new_node->n < current->next->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}
