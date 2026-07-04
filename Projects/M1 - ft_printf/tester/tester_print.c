/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_print.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:31:16 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 01:31:23 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_header(void)
{
	printf("\n");
	printf(BOLD_CYAN "══════════════════════════════════════════════════\n");
	printf("                    42 PORTO\n");
	printf("                FT_PRINTF TESTER\n");
	printf("                Author: dsilva-c\n");
	printf("══════════════════════════════════════════════════\n" RESET);
	printf("\n");
	printf(" 🚀 Let's test your printf! You got this! 💪\n");
	printf("\n");
}

void	print_test_header(char *test_name)
{
	printf(BOLD_YELLOW "──────────────────────────────────────────────────\n");
	printf("  🧪 TEST: %s\n", test_name);
	printf("──────────────────────────────────────────────────\n" RESET);
	printf("\n");
}

void	print_comparison(int r1, int r2)
{
	printf("\n");
	printf("    " BOLD_WHITE "Real Ret:" RESET " %d\n", r1);
	printf("    " BOLD_WHITE "Mine Ret:" RESET " %d\n", r2);
}

void	print_result(int passed, char *desc, t_results *res)
{
	if (passed)
	{
		printf(BOLD_GREEN "  ✓ PASS: %s\n" RESET, desc);
		res->passed++;
	}
	else
	{
		printf(BOLD_RED "  ✗ FAIL: %s\n" RESET, desc);
		res->failed++;
	}
	printf("\n");
}

void	print_summary(t_results *res)
{
	printf("\n");
	printf(BOLD_CYAN "══════════════════════════════════════════════════\n");
	printf("                 📊 TEST SUMMARY\n");
	printf("══════════════════════════════════════════════════\n" RESET);
	printf("\n");
	printf("  ✓ Tests passed: " BOLD_GREEN "%d\n" RESET, res->passed);
	printf("  ✗ Tests failed: " BOLD_RED "%d\n" RESET, res->failed);
	printf("  📝 Total tests: %d\n", res->passed + res->failed);
	printf("\n");
	if (res->failed == 0)
		printf(BOLD_GREEN " 🎉 ALL TESTS PASSED! Perfect! ⭐ \n" RESET);
	else
		printf(BOLD_RED " 💪 Some tests failed. Keep debugging! \n" RESET);
	printf("\n");
}
