/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/11 21:35:33 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/01/11 21:35:45 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "get_next_line.h"

static int	ft_strcmp(const char *s1, const char *s2)
{
	while (*s1 && *s2 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

static void	parse_command(t_stack_node **a, t_stack_node **b, char *line)
{
	if (!ft_strcmp(line, "sa\n"))
		sa(a, false);
	else if (!ft_strcmp(line, "sb\n"))
		sb(b, false);
	else if (!ft_strcmp(line, "ss\n"))
		ss(a, b, false);
	else if (!ft_strcmp(line, "pa\n"))
		pa(a, b, false);
	else if (!ft_strcmp(line, "pb\n"))
		pb(b, a, false);
	else if (!ft_strcmp(line, "ra\n"))
		ra(a, false);
	else if (!ft_strcmp(line, "rb\n"))
		rb(b, false);
	else if (!ft_strcmp(line, "rr\n"))
		rr(a, b, false);
	else if (!ft_strcmp(line, "rra\n"))
		rra(a, false);
	else if (!ft_strcmp(line, "rrb\n"))
		rrb(b, false);
	else if (!ft_strcmp(line, "rrr\n"))
		rrr(a, b, false);
	else
		free_errors(a);
}

static void	run_checker(t_stack_node **a, t_stack_node **b)
{
	char	*line;

	line = get_next_line(0);
	while (line)
	{
		parse_command(a, b, line);
		free(line);
		line = get_next_line(0);
	}
	if (stack_sorted(*a) && stack_len(*b) == 0)
		write(1, "OK\n", 3);
	else
		write(1, "KO\n", 3);
}

int	main(int argc, char **argv)
{
	t_stack_node	*a;
	t_stack_node	*b;

	a = NULL;
	b = NULL;
	if (argc == 1)
		return (1);
	if (argc == 2)
		argv = split(argv[1], ' ');
	else
		argv = argv + 1;
	init_stack_a(&a, argv);
	run_checker(&a, &b);
	free_stack(&a);
	free_stack(&b);
	if (argc == 2)
		free_matrix(argv);
	return (0);
}
