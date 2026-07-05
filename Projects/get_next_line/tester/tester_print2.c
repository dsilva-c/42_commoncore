/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_print2.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:23:11 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:23:40 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_line_info(char *line, int line_num)
{
	int	i;

	if (line)
	{
		printf("    Line %d: \"", line_num);
		i = 0;
		while (line[i])
		{
			print_char(line[i]);
			i++;
		}
		printf("\"\n");
	}
	else
		printf("    Line %d: (NULL)\n", line_num);
}

static void	print_summary_header(void)
{
	printf("\n");
	printf(BOLD_CYAN "══════════════════════════════════════════════════\n");
	printf("                 📊 TEST SUMMARY\n");
	printf("══════════════════════════════════════════════════\n" RESET);
	printf("\n");
}

static void	print_summary_results(t_results *res)
{
	printf("  ✓ Tests passed: " BOLD_GREEN "%d\n" RESET, res->passed);
	printf("  ✗ Tests failed: " BOLD_RED "%d\n" RESET, res->failed);
	printf("  📝 Total tests: %d\n", res->passed + res->failed);
	printf("\n");
	if (res->failed == 0)
		printf(BOLD_GREEN " 🎉 ALL TESTS PASSED! You're amazing! 🌟 \n" RESET);
	else
		printf(BOLD_RED " 💪 Some tests failed. Keep trying! \n" RESET);
	printf("\n");
}

static void	print_leak_info(void)
{
	printf(BOLD_YELLOW "──────────────────────────────────────────────────\n");
	printf("  🔍 MEMORY LEAK CHECK\n");
	printf("──────────────────────────────────────────────────\n" RESET);
	printf("\n");
	printf("  Run with valgrind to check for memory leaks:\n");
	printf("  valgrind --leak-check=full ./tester\n");
	printf("\n\n");
}

void	print_summary(t_results *res)
{
	print_summary_header();
	print_summary_results(res);
	print_leak_info();
}
