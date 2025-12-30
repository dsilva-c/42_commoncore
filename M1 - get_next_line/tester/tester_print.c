/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_print.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:22:17 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:22:59 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_header(void)
{
	printf("\n");
	printf(BOLD_CYAN "══════════════════════════════════════════════════\n");
	printf("                     42 PORTO\n");
	printf("          GET_NEXT_LINE TESTER (MANDATORY)\n");
	printf("                Author: dsilva-c\n");
	printf("══════════════════════════════════════════════════\n" RESET);
	printf("\n");
	printf(" 🚀 Let's test your code! Good luck! 🍀\n");
	printf("\n");
}

void	print_test_header(char *test_name)
{
	printf(BOLD_YELLOW "──────────────────────────────────────────────────\n");
	printf("  🧪 TEST: %s\n", test_name);
	printf("──────────────────────────────────────────────────\n" RESET);
	printf("\n");
}

void	print_result(int passed, char *description, t_results *res)
{
	if (passed)
	{
		printf(BOLD_GREEN "  ✓ PASS: %s\n" RESET, description);
		res->passed++;
	}
	else
	{
		printf(BOLD_RED "  ✗ FAIL: %s\n" RESET, description);
		res->failed++;
	}
}

void	print_char(char c)
{
	if (c == '\n')
		printf("\\n");
	else
		printf("%c", c);
}
