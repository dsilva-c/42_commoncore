/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:12:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:12:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static void	init_results(t_results *res)
{
	res->passed = 0;
	res->failed = 0;
}

static int	check_binaries(void)
{
	if (access("../push_swap", F_OK) != 0)
	{
		printf(BOLD_RED "  Error: ../push_swap not found!\n" RESET);
		printf("  Run 'make' in the project root first.\n\n");
		return (0);
	}
	if (access("../checker", F_OK) != 0)
	{
		printf(BOLD_YELLOW "  Warning: ../checker not found.\n" RESET);
		printf("  Bonus tests will be skipped.\n");
		printf("  Run 'make bonus' in the project root.\n\n");
		return (1);
	}
	return (2);
}

int	main(void)
{
	t_results	res;
	int			bins;

	srand(time(NULL));
	init_results(&res);
	print_header();
	bins = check_binaries();
	if (bins == 0)
		return (1);
	test_identity(&res);
	test_small_sort(&res);
	test_error_handling(&res);
	test_performance_100(&res);
	test_performance_500(&res);
	if (bins == 2)
		test_bonus_checker(&res);
	print_summary(&res);
	return (res.failed > 0);
}
