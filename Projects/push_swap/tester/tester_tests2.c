/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_tests2.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:30:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:30:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_performance_100(t_results *res)
{
	char	args[8192];
	char	desc[64];
	int		moves;
	int		ok;
	int		i;

	print_test_header("⚡ PERFORMANCE TESTS - 100 elements");
	printf(YELLOW "    > Must sort in less than 700 moves\n" RESET);
	printf("      Running 5 random tests...\n\n");
	i = 0;
	while (++i <= 5)
	{
		gen_random_args(args, sizeof(args), 100);
		moves = get_move_count(args);
		ok = verify_sort(args);
		snprintf(desc, sizeof(desc), "100 elems run #%d", i);
		print_perf_result(moves, 700, ok, desc, res);
	}
}

void	test_performance_500(t_results *res)
{
	char	args[16384];
	char	desc[64];
	int		moves;
	int		ok;
	int		i;

	print_test_header("🚀 PERFORMANCE TESTS - 500 elements");
	printf(YELLOW "    > Must sort in less than 5500 moves\n" RESET);
	printf("      Running 5 random tests...\n\n");
	i = 0;
	while (++i <= 5)
	{
		gen_random_args(args, sizeof(args), 500);
		moves = get_move_count(args);
		ok = verify_sort(args);
		snprintf(desc, sizeof(desc), "500 elems run #%d", i);
		print_perf_result(moves, 5500, ok, desc, res);
	}
}
