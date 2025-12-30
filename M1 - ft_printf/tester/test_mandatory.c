/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_mandatory.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:31:48 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 01:32:04 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_char(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Char %c");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%c", 'A');
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%c", 'A');
	print_comparison(r1, r2);
	print_result(r1 == r2, "Basic Char 'A'", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf(" %c ", 0);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf(" %c ", 0);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Null char (ASCII 0)", res);
}

void	test_string(t_results *res)
{
	int		r1;
	int		r2;
	char	*s_null;

	s_null = (char *) NULL;
	print_test_header("String %s");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%s", "Hello");
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%s", "Hello");
	print_comparison(r1, r2);
	print_result(r1 == r2, "Basic String", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%s", s_null);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%s", s_null);
	print_comparison(r1, r2);
	print_result(r1 == r2, "NULL String", res);
}

static void	run_int_test(char *fmt, int val, char *desc, t_results *res)
{
	int	r1;
	int	r2;

	printf("    Real: ");
	fflush(stdout);
	r1 = printf(fmt, val);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf(fmt, val);
	print_comparison(r1, r2);
	print_result(r1 == r2, desc, res);
}

void	test_int(t_results *res)
{
	print_test_header("Int %d %i");
	run_int_test("%d", 42, "Basic Int 42", res);
	run_int_test("%d", INT_MAX, "INT_MAX", res);
	run_int_test("%i", INT_MIN, "INT_MIN", res);
}
