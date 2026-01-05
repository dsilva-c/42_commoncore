/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus_print.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:26:34 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:27:18 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester_bonus.h"

void	print_header_bonus(void)
{
	printf("\n");
	printf(BOLD_CYAN "══════════════════════════════════════════════════\n");
	printf("                     42 PORTO\n");
	printf("           GET_NEXT_LINE TESTER (BONUS)\n");
	printf("                Author: dsilva-c\n");
	printf("══════════════════════════════════════════════════\n" RESET);
	printf("\n");
	printf(" 🚀 Let's test your bonus! You got this! 💪\n");
	printf("\n");
}

void	print_test_header_bonus(char *test_name)
{
	printf(BOLD_YELLOW "──────────────────────────────────────────────────\n");
	printf("  🧪 TEST: %s\n", test_name);
	printf("──────────────────────────────────────────────────\n" RESET);
	printf("\n");
}

void	print_result_bonus(int passed, char *desc, t_results *res)
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
}

void	print_char_bonus(char c)
{
	if (c == '\n')
		printf("\\n");
	else
		printf("%c", c);
}

void	drain_fd(int fd)
{
	char	*line;

	line = get_next_line(fd);
	while (line != NULL)
	{
		free(line);
		line = get_next_line(fd);
	}
}
