#include "lists.h"

/**
 * check_cycle - Function to check if there is cycle in list
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	if (!list)
		return (0);

	while (1)
	{
		if (hare->next != NULL && hare->next->next != NULL)
		{
			hare = hare->next->next;
			tortoise = tortoise->next;

			/* Circle is found if nodes match*/
			if (hare == tortoise)
				return (1);
		}
		else
			return (0);
	}
}
