/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_utils_part4.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 18:49:13 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 18:49:16 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

int	get_g_tests(void)
{
	return (get_counters_ptr()[0]);
}

int	get_g_passed(void)
{
	return (get_counters_ptr()[1]);
}

int	get_g_failed(void)
{
	return (get_counters_ptr()[2]);
}

void	print_summary(void)
{
	printf("\n\n");
	printf(BOLD_CYAN "  ╔════════════════════════════════════════════╗\n"
		RESET);
	printf(BOLD_CYAN "  ║" RESET "             📊 TEST SUMMARY 📊"
		"             " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ╚════════════════════════════════════════════╝\n"
		RESET);
	printf("\n");
	printf("    Total Tests:  " BOLD_WHITE "%d\n" RESET, get_g_tests());
	printf("    Passed:       " BOLD_GREEN "✓ %d\n" RESET, get_g_passed());
	printf("    Failed:       " BOLD_RED "✗ %d\n" RESET, get_g_failed());
	printf("\n");
	print_success_rate();
	printf("\n");
	print_final_message();
	printf("\n\n");
}
