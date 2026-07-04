/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_print.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:15:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:15:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_header(void)
{
	printf(BOLD_CYAN "\n  ╔════════════════════════════════════════════╗\n"
		RESET);
	printf(BOLD_CYAN "  ║" RESET BOLD_WHITE "                  42 PORTO"
		"                  " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ║" RESET BOLD_WHITE "              PUSH_SWAP TESTER"
		"              " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ║" RESET "              Author: dsilva-c"
		"              " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ╚════════════════════════════════════════════╝\n"
		RESET);
	printf("\n");
}

void	print_test_header(const char *title)
{
	printf("\n");
	printf(BOLD_CYAN "  ╔════════════════════════════════════════════╗\n"
		RESET);
	printf(BOLD_CYAN "  ║" RESET " %-42s " BOLD_CYAN "║\n" RESET, title);
	printf(BOLD_CYAN "  ╚════════════════════════════════════════════╝\n"
		RESET);
	printf("\n");
}

void	print_result(int passed, const char *desc, t_results *res)
{
	if (passed)
	{
		printf(BOLD_GREEN "      ✓ PASS" RESET " | %s\n", desc);
		res->passed++;
	}
	else
	{
		printf(BOLD_RED "      ✗ FAIL" RESET " | %s\n", desc);
		res->failed++;
	}
}

void	print_perf_result(int moves, int limit, int ok,
		const char *desc, t_results *res)
{
	int		passed;
	char	info[256];

	passed = (moves <= limit && moves >= 0 && ok);
	snprintf(info, sizeof(info), "%s: %d moves (max %d) %s",
		desc, moves, limit, ok ? "[OK]" : "[KO]");
	if (passed)
	{
		printf(BOLD_GREEN "      ✓ PASS" RESET " | %s\n", info);
		res->passed++;
	}
	else
	{
		printf(BOLD_RED "      ✗ FAIL" RESET " | %s\n", info);
		res->failed++;
	}
}
