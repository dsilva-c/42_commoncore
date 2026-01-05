/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_character_part2.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:30:19 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:30:21 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_toupper(void)
{
	int	result;

	print_function("ft_toupper", "Lowercase to uppercase");
	result = ft_toupper('a');
	print_test("ft_toupper('a')");
	print_output("'A'");
	test_result(result == 'A', "lowercase converts");
	print_divider();
	result = ft_toupper('A');
	print_test("ft_toupper('A')");
	print_output("'A'");
	test_result(result == 'A', "uppercase unchanged");
	print_divider();
	result = ft_toupper('5');
	print_test("ft_toupper('5')");
	print_output("'5'");
	test_result(result == '5', "digit unchanged");
}

void	test_tolower(void)
{
	int	result;

	print_function("ft_tolower", "Uppercase to lowercase");
	result = ft_tolower('A');
	print_test("ft_tolower('A')");
	print_output("'a'");
	test_result(result == 'a', "uppercase converts");
	print_divider();
	result = ft_tolower('a');
	print_test("ft_tolower('a')");
	print_output("'a'");
	test_result(result == 'a', "lowercase unchanged");
	print_divider();
	result = ft_tolower('5');
	print_test("ft_tolower('5')");
	print_output("'5'");
	test_result(result == '5', "digit unchanged");
}

void	test_character_part1(void)
{
	test_isalpha();
	printf("\n");
	test_isdigit();
	printf("\n");
	test_isalnum();
	printf("\n");
	test_isascii();
	printf("\n");
	test_isprint();
}

void	test_character_part2(void)
{
	test_toupper();
	printf("\n");
	test_tolower();
}

void	test_character_functions(void)
{
	print_title("PART 1: CHARACTER CLASSIFICATION");
	test_character_part1();
	printf("\n");
	test_character_part2();
}
