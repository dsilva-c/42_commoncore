/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_output_part2.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:59:29 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:59:31 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_putnbr_negative(void)
{
	print_function("ft_putnbr_fd", "Output integer");
	print_test("ft_putnbr_fd(-42, 1)");
	printf("      Output: ");
	fflush(stdout);
	ft_putnbr_fd(-42, 1);
	printf("\n");
	test_result(1, "executed");
}

void	test_putnbr_int_min(void)
{
	print_divider();
	print_test("ft_putnbr_fd(INT_MIN, 1)");
	printf("      Output: ");
	fflush(stdout);
	ft_putnbr_fd(INT_MIN, 1);
	printf("\n");
	test_result(1, "executed");
}

void	test_putnbr_zero(void)
{
	print_divider();
	print_test("ft_putnbr_fd(0, 1)");
	printf("      Output: ");
	fflush(stdout);
	ft_putnbr_fd(0, 1);
	printf("\n");
	test_result(1, "executed");
}

void	test_putnbr_all(void)
{
	test_putnbr_negative();
	test_putnbr_int_min();
	test_putnbr_zero();
}

void	test_output_functions(void)
{
	print_title("PART 7: OUTPUT FUNCTIONS");
	test_putchar_putstr();
	printf("\n");
	test_putendl_putnbr();
	test_putnbr_all();
}
