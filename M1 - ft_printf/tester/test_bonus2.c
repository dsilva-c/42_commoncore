/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_bonus2.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 03:18:13 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 03:18:53 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static void	run_mix_test(int r1, int r2, char *desc, t_results *res)
{
	print_comparison(r1, r2);
	print_result(r1 == r2, desc, res);
}

static void	run_mix_safety(t_results *res)
{
	int	r1;
	int	r2;

	printf(BOLD_YELLOW "  [INFO] Testing Trailing %%...\n" RESET);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("Test %%");
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("Test %");
	run_mix_test(r1, r2, "Trailing % (No Crash)", res);
}

void	test_mix(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Mixed & Multiple Args");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("Val1: %d, Val2: %s, Val3: %x", 42, "Mix", 255);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("Val1: %d, Val2: %s, Val3: %x", 42, "Mix", 255);
	run_mix_test(r1, r2, "Multiple Args (Int, Str, Hex)", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%% %d %% %s %%", 1, "test");
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%% %d %% %s %%", 1, "test");
	run_mix_test(r1, r2, "Percent + Args", res);
	run_mix_safety(res);
}
