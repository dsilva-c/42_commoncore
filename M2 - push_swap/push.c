/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/11 21:22:55 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/01/11 21:23:59 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	push(t_stack_node **dest, t_stack_node **src)
{
	t_stack_node	*push_node;

	if (!*src)
		return ;
	push_node = *src;
	*src = (*src)->next;
	if (*src)
		(*src)->prev = NULL;
	push_node->prev = NULL;
	if (!*dest)
	{
		*dest = push_node;
		push_node->next = NULL;
	}
	else
	{
		push_node->next = *dest;
		push_node->next->prev = push_node;
		*dest = push_node;
	}
}

void	pa(t_stack_node **a, t_stack_node **b, bool print)
{
	push(a, b);
	if (print)
		write(1, "pa\n", 3);
}

void	pb(t_stack_node **b, t_stack_node **a, bool print)
{
	push(b, a);
	if (print)
		write(1, "pb\n", 3);
}
