/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_string_part2.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:46:11 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:46:14 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_strchr_not_found(void)
{
	char	*test_str;
	char	*chr;

	test_str = "Hello World";
	chr = ft_strchr(test_str, 'x');
	print_test("ft_strchr(\"Hello World\", 'x')");
	print_output("NULL");
	test_result(chr == NULL, "not found");
}

void	test_atoi_positive(void)
{
	int	num;

	num = ft_atoi("123");
	print_test("ft_atoi(\"123\")");
	print_output("123");
	test_result(num == 123, "positive number");
}

void	test_atoi_negative(void)
{
	int	num;

	num = ft_atoi("-456");
	print_test("ft_atoi(\"-456\")");
	print_output("-456");
	test_result(num == -456, "negative number");
	print_divider();
	num = ft_atoi("0");
	print_test("ft_atoi(\"0\")");
	print_output("0");
	test_result(num == 0, "zero");
	print_divider();
	num = ft_atoi("  42");
	print_test("ft_atoi(\"  42\")");
	print_output("42");
	test_result(num == 42, "skip whitespace");
}

void	test_atoi(void)
{
	print_function("ft_atoi", "ASCII to integer");
	test_atoi_positive();
	print_divider();
	test_atoi_negative();
}

void	test_string_functions(void)
{
	print_title("PART 2: STRING FUNCTIONS");
	test_strlen();
	printf("\n");
	test_strchr();
	printf("\n");
	test_strchr_not_found();
	printf("\n");
	test_strrchr();
	printf("\n");
	test_strncmp();
	printf("\n");
	test_strnstr();
	printf("\n");
	test_atoi();
}
