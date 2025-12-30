/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus_print2.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:28:22 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:28:29 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester_bonus.h"

void	print_line_info_bonus(char *line, int fd, int line_num)
{
	int	i;

	if (line)
	{
		printf("    [fd=%d] Line %d: \"", fd, line_num);
		i = 0;
		while (line[i])
		{
			print_char_bonus(line[i]);
			i++;
		}
		printf("\"\n");
	}
	else
		printf("    [fd=%d] Line %d: (NULL)\n", fd, line_num);
}

static void	print_summary_header_bonus(void)
{
	printf("\n");
	printf(BOLD_CYAN "══════════════════════════════════════════════════\n");
	printf("                 📊 TEST SUMMARY\n");
	printf("══════════════════════════════════════════════════\n" RESET);
	printf("\n");
}

static void	print_summary_results_bonus(t_results *res)
{
	printf("  ✓ Tests passed: " BOLD_GREEN "%d\n" RESET, res->passed);
	printf("  ✗ Tests failed: " BOLD_RED "%d\n" RESET, res->failed);
	printf("  📝 Total tests: %d\n", res->passed + res->failed);
	printf("\n");
	if (res->failed == 0)
		printf(BOLD_GREEN " 🎉 ALL TESTS PASSED! You're a rockstar! ⭐ \n" RESET);
	else
		printf(BOLD_RED " 💪 Some tests failed. Never give up! \n" RESET);
	printf("\n");
}

static void	print_leak_info_bonus(void)
{
	printf(BOLD_YELLOW "──────────────────────────────────────────────────\n");
	printf("  🔍 MEMORY LEAK CHECK\n");
	printf("──────────────────────────────────────────────────\n" RESET);
	printf("\n");
	printf("  Run with valgrind to check for memory leaks:\n");
	printf("  valgrind --leak-check=full ./tester_bonus\n");
	printf("\n\n");
}

void	print_summary_bonus(t_results *res)
{
	print_summary_header_bonus();
	print_summary_results_bonus(res);
	print_leak_info_bonus();
}
