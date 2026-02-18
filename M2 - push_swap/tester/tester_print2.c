/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_print2.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:18:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:18:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static void	print_success_rate(t_results *res)
{
	double	rate;
	int		total;

	total = res->passed + res->failed;
	if (total == 0)
		rate = 0.0;
	else
		rate = (double)res->passed / total * 100;
	if (res->failed == 0)
	{
		printf("    Success Rate: " BOLD_GREEN "%.1f%% 🎉\n" RESET,
			rate);
	}
	else
	{
		printf("    Success Rate: " BOLD_YELLOW "%.1f%%\n" RESET, rate);
	}
}

static void	print_final_message(t_results *res)
{
	if (res->failed == 0)
	{
		printf(BOLD_MAGENTA "    🎊 CONGRATULATIONS! 🎊\n" RESET);
		printf(BOLD_GREEN "    ALL TESTS PASSED! 🥳\n" RESET);
	}
	else
	{
		printf(BOLD_RED "    SOME TESTS FAILED 😟\n" RESET);
	}
}

void	print_summary(t_results *res)
{
	printf("\n\n");
	printf(BOLD_CYAN "  ╔════════════════════════════════════════════╗\n"
		RESET);
	printf(BOLD_CYAN "  ║" RESET "             📊 TEST SUMMARY 📊"
		"             " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ╚════════════════════════════════════════════╝\n"
		RESET);
	printf("\n");
	printf("    Total Tests:  " BOLD_WHITE "%d\n" RESET,
		res->passed + res->failed);
	printf("    Passed:       " BOLD_GREEN "✓ %d\n" RESET, res->passed);
	printf("    Failed:       " BOLD_RED "✗ %d\n" RESET, res->failed);
	printf("\n");
	print_success_rate(res);
	printf("\n");
	print_final_message(res);
	printf("\n\n");
}
