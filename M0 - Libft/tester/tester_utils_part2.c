/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_utils_part2.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:27:08 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:27:10 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_title(const char *title)
{
	printf("\n");
	printf(BOLD_CYAN "  ╔════════════════════════════════════════════╗\n"
		RESET);
	printf(BOLD_CYAN "  ║" RESET " %-42s " BOLD_CYAN "║\n" RESET, title);
	printf(BOLD_CYAN "  ╚════════════════════════════════════════════╝\n"
		RESET);
	printf("\n");
}

void	print_function(const char *fname, const char *description)
{
	printf(YELLOW "    > %s\n" RESET, fname);
	printf("      %s\n", description);
	printf("\n");
}

char	ft_upper_char(unsigned int i, char c)
{
	(void)i;
	if (c >= 'a' && c <= 'z')
		return (c - 32);
	return (c);
}

void	print_test(const char *test_desc)
{
	printf("      %s\n", test_desc);
}

void	print_output(const char *output_desc)
{
	printf("      Output: " BOLD_WHITE "%s\n" RESET, output_desc);
}
