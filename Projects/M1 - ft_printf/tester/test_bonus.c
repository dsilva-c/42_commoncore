/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_bonus.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:34:10 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 01:34:20 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_width(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Bonus: Width");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%10d|", 42);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%10d|", 42);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Width 10 > Len", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%2d|", 1234);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%2d|", 1234);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Width 2 < Len", res);
}

void	test_precision(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Bonus: Precision");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%.3s|", "Hello");
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%.3s|", "Hello");
	print_comparison(r1, r2);
	print_result(r1 == r2, "Prec String", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%.0d|", 0);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%.0d|", 0);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Prec 0 Val 0 (Empty)", res);
}

void	test_flags(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Bonus: Flags");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%#x|", 42);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%#x|", 42);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Hash Flag %#x", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%#x|", 0);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%#x|", 0);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Hash Flag 0 (No Prefix)", res);
}

static void	run_combo_special(t_results *res)
{
	int	r1;
	int	r2;

	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%5c|", 'A');
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%05c|", 'A');
	print_comparison(r1, r2);
	print_result(r1 == r2, "Flag '0' ignored on Char", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|0000%%|");
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%05%|");
	print_comparison(r1, r2);
	print_result(r1 == r2, "Flag '0' works on Percent", res);
}

void	test_combos(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Bonus: Combos");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%+d|", 42);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%+ d|", 42);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Plus overrides Space", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%-5d|", 42);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%-05d|", 42);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Minus overrides Zero", res);
	run_combo_special(res);
}
