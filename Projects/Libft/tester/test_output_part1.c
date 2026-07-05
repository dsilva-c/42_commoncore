/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_output_part1.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:58:44 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:58:46 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_putchar_fd(void)
{
	print_function("ft_putchar_fd", "Output single char");
	print_test("ft_putchar_fd('X', 1)");
	printf("      Output: ");
	fflush(stdout);
	ft_putchar_fd('X', 1);
	printf("\n");
	test_result(1, "executed");
}

void	test_putstr_fd(void)
{
	print_function("ft_putstr_fd", "Output string");
	print_test("ft_putstr_fd(\"test\", 1)");
	printf("      Output: ");
	fflush(stdout);
	ft_putstr_fd("test", 1);
	printf("\n");
	test_result(1, "executed");
}

void	test_putendl_fd(void)
{
	print_function("ft_putendl_fd", "Output string + newline");
	print_test("ft_putendl_fd(\"line\", 1)");
	printf("      Output: ");
	fflush(stdout);
	ft_putendl_fd("line", 1);
	test_result(1, "executed");
}

void	test_putchar_putstr(void)
{
	test_putchar_fd();
	printf("\n");
	test_putstr_fd();
}

void	test_putendl_putnbr(void)
{
	test_putendl_fd();
	printf("\n");
}
