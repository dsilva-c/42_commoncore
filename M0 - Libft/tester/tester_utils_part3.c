/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_utils_part3.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:27:54 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:27:56 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_memory_check(const char *label)
{
	printf("      " BOLD_CYAN "%s -> Check for Memory Leaks" RESET "\n", label);
	printf("      " BOLD_CYAN "(make valgrind-check)" RESET "\n");
	printf("\n");
}

void	print_divider(void)
{
	printf("\n");
}

void	free_split(char **split)
{
	int	i;

	i = 0;
	if (!split)
		return ;
	while (split[i])
	{
		free(split[i]);
		i++;
	}
	free(split);
}

void	print_success_rate(void)
{
	double	rate;

	if (get_g_tests() == 0)
		rate = 0.0;
	else
		rate = (double)get_g_passed() / get_g_tests() * 100;
	if (get_g_failed() == 0)
	{
		printf("    Success Rate: " BOLD_GREEN "%.1f%% 🎉\n" RESET,
			rate);
	}
	else
	{
		printf("    Success Rate: " BOLD_YELLOW "%.1f%%\n" RESET, rate);
	}
}

void	print_final_message(void)
{
	if (get_g_failed() == 0)
	{
		printf(BOLD_MAGENTA "    🎊 CONGRATULATIONS! 🎊\n" RESET);
		printf(BOLD_GREEN "    ALL TESTS PASSED! 🥳\n" RESET);
	}
	else
	{
		printf(BOLD_RED "    SOME TESTS FAILED 😟\n" RESET);
	}
}
