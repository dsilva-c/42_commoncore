/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_main.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 18:02:10 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 18:02:12 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_header(void)
{
	printf(BOLD_CYAN "\n  ╔════════════════════════════════════════════╗\n"
		RESET);
	printf(BOLD_CYAN "  ║" RESET BOLD_WHITE "                  42 PORTO"
		"                  " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ║" RESET BOLD_WHITE "                LIBFT TESTER"
		"                " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ║" RESET "              Author: dsilva-c"
		"              " BOLD_CYAN "║\n" RESET);
	printf(BOLD_CYAN "  ╚════════════════════════════════════════════╝\n"
		RESET);
	printf("\n");
}

void	run_all_tests(void)
{
	test_character_functions();
	printf("\n\n");
	test_string_functions();
	printf("\n\n");
	test_memory_functions();
	printf("\n\n");
	test_copy_functions();
	printf("\n\n");
	test_allocation_functions();
	printf("\n\n");
	test_additional_functions();
	printf("\n\n");
	test_output_functions();
	printf("\n\n");
	test_bonus_functions();
}

int	main(void)
{
	int	exit_code;

	init_counters();
	print_header();
	run_all_tests();
	print_summary();
	if (get_g_failed() == 0)
		exit_code = 0;
	else
		exit_code = 1;
	return (exit_code);
}
