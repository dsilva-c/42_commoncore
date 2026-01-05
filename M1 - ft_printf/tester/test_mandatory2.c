/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_mandatory2.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:33:26 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 01:33:37 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static void	run_uint_test(unsigned int val, char *desc, t_results *res)
{
	int	r1;
	int	r2;

	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%u", val);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%u", val);
	print_comparison(r1, r2);
	print_result(r1 == r2, desc, res);
}

void	test_unsigned(t_results *res)
{
	print_test_header("Unsigned %u");
	run_uint_test(42, "Unsigned 42", res);
	run_uint_test(0, "Unsigned 0", res);
	run_uint_test(UINT_MAX, "UINT_MAX", res);
}

static void	run_hex_test(char *fmt, unsigned int val, char *desc, t_results *r)
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
	print_result(r1 == r2, desc, r);
}

void	test_hex(t_results *res)
{
	print_test_header("Hex %x %X");
	run_hex_test("%x", 0, "Hex 0", res);
	run_hex_test("%x", 255, "Hex Lower 255", res);
	run_hex_test("%X", 255, "Hex Upper 255", res);
}

void	test_ptr(t_results *res)
{
	int	r1;
	int	r2;
	int	a;

	a = 42;
	print_test_header("Pointer %p");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%p", &a);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%p", &a);
	print_comparison(r1, r2);
	print_result(r1 == r2, "Pointer Address", res);
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%p", (void *) NULL);
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%p", (void *) NULL);
	print_comparison(r1, r2);
	print_result(r1 == r2, "NULL Pointer", res);
}
