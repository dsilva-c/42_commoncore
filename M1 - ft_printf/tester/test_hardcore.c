/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_hardcore.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 00:17:17 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/08 00:17:45 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static void	test_prec_vs_zero(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Hardcore: Precision kills Zero");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%10.5d|", 42);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%010.5d|", 42);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Flag 0 ignores if Prec exists (Int)", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%10.5x|", 42);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%010.5x|", 42);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Flag 0 ignores if Prec exists (Hex)", res);
}

static void	test_edge_cases(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Hardcore: Edge Cases");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%#x|", 0);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%#x|", 0);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Hash on 0 (No 0x prefix)", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%.0d|", 0);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%.0d|", 0);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Prec .0 on 0 (Print Nothing)", res);
}

static void	test_sign_clash(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Hardcore: Sign Clashes");
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
	r1 = printf("|%+05d|", 42);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%+05d|", 42);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Plus + Zero + Width (Sign counts)", res);
}

static void	test_implicit_cast(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Hardcore: Implicit Casts");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%u|", -1);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%u|", -1);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Neg Int as Unsigned (UINT_MAX)", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("|%x|", -1);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("|%x|", -1);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Neg Int as Hex (ffffffff)", res);
}

void	test_hardcore(t_results *res)
{
	test_prec_vs_zero(res);
	test_edge_cases(res);
	test_sign_clash(res);
	test_implicit_cast(res);
}
