/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_character_part1.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:29:10 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:29:14 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_isalpha(void)
{
	int	result;

	print_function("ft_isalpha", "Alphabetic character check");
	result = ft_isalpha('a');
	print_test("ft_isalpha('a')");
	print_output("non-zero (1)");
	test_result(result != 0, "lowercase letter");
	print_divider();
	result = ft_isalpha('Z');
	print_test("ft_isalpha('Z')");
	print_output("non-zero (1)");
	test_result(result != 0, "uppercase letter");
	print_divider();
	result = ft_isalpha('5');
	print_test("ft_isalpha('5')");
	print_output("0 (not alpha)");
	test_result(result == 0, "digit returns 0");
	print_divider();
	result = ft_isalpha(' ');
	print_test("ft_isalpha(' ')");
	print_output("0 (not alpha)");
	test_result(result == 0, "space returns 0");
}

void	test_isdigit(void)
{
	int	result;

	print_function("ft_isdigit", "Digit check (0-9)");
	result = ft_isdigit('0');
	print_test("ft_isdigit('0')");
	print_output("non-zero (1)");
	test_result(result != 0, "zero digit");
	print_divider();
	result = ft_isdigit('9');
	print_test("ft_isdigit('9')");
	print_output("non-zero (1)");
	test_result(result != 0, "nine digit");
	print_divider();
	result = ft_isdigit('a');
	print_test("ft_isdigit('a')");
	print_output("0 (not digit)");
	test_result(result == 0, "letter returns 0");
}

void	test_isalnum(void)
{
	int	result;

	print_function("ft_isalnum", "Alphanumeric check");
	result = ft_isalnum('a');
	print_test("ft_isalnum('a')");
	print_output("non-zero (1)");
	test_result(result != 0, "letter is alphanumeric");
	print_divider();
	result = ft_isalnum('5');
	print_test("ft_isalnum('5')");
	print_output("non-zero (1)");
	test_result(result != 0, "digit is alphanumeric");
	print_divider();
	result = ft_isalnum('@');
	print_test("ft_isalnum('@')");
	print_output("0 (not alphanumeric)");
	test_result(result == 0, "symbol returns 0");
}

void	test_isascii(void)
{
	int	result;

	print_function("ft_isascii", "ASCII check (0-127)");
	result = ft_isascii(0);
	print_test("ft_isascii(0)");
	print_output("non-zero (1)");
	test_result(result != 0, "null character");
	print_divider();
	result = ft_isascii(127);
	print_test("ft_isascii(127)");
	print_output("non-zero (1)");
	test_result(result != 0, "DEL character");
	print_divider();
	result = ft_isascii(128);
	print_test("ft_isascii(128)");
	print_output("0 (extended ASCII)");
	test_result(result == 0, "extended ASCII returns 0");
}

void	test_isprint(void)
{
	int	result;

	print_function("ft_isprint", "Printable character check");
	result = ft_isprint(' ');
	print_test("ft_isprint(' ')");
	print_output("non-zero (1)");
	test_result(result != 0, "space is printable");
	print_divider();
	result = ft_isprint('~');
	print_test("ft_isprint('~')");
	print_output("non-zero (1)");
	test_result(result != 0, "tilde is printable");
	print_divider();
	result = ft_isprint(31);
	print_test("ft_isprint(31)");
	print_output("0 (control char)");
	test_result(result == 0, "control character returns 0");
}
