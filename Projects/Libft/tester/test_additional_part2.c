/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_additional_part2.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:48:05 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:48:08 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_itoa_positive(void)
{
	char	*result;

	result = ft_itoa(42);
	print_test("ft_itoa(42)");
	print_output("\"42\"");
	test_result(result != NULL && strcmp(result, "42") == 0,
		"positive converted");
	free(result);
}

void	test_itoa_negative(void)
{
	char	*result;

	result = ft_itoa(-42);
	print_test("ft_itoa(-42)");
	print_output("\"-42\"");
	test_result(result != NULL && strcmp(result, "-42") == 0,
		"negative converted");
	free(result);
}

void	test_itoa_zero(void)
{
	char	*result;

	result = ft_itoa(0);
	print_test("ft_itoa(0)");
	print_output("\"0\"");
	test_result(result != NULL && strcmp(result, "0") == 0,
		"zero converted");
	free(result);
	print_output("Memory freed successfully");
}

void	test_itoa(void)
{
	print_function("ft_itoa", "Integer to string");
	print_memory_check("ft_itoa");
	test_itoa_positive();
	print_divider();
	test_itoa_negative();
	print_divider();
	test_itoa_zero();
}

void	test_strmapi(void)
{
	char	*result;

	print_function("ft_strmapi", "Map function to chars");
	print_memory_check("ft_strmapi");
	result = ft_strmapi("hello", ft_upper_char);
	print_test("ft_strmapi(\"hello\", uppercase)");
	print_output("\"HELLO\"");
	test_result(result != NULL && strcmp(result, "HELLO") == 0,
		"mapped");
	free(result);
	print_divider();
	result = ft_strmapi("", ft_upper_char);
	print_test("ft_strmapi(\"\", uppercase)");
	print_output("\"\"");
	test_result(result != NULL && strcmp(result, "") == 0,
		"empty string");
	free(result);
	print_output("Memory freed successfully");
}
