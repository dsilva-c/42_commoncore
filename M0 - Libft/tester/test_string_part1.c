/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_string_part1.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:45:27 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:45:30 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_strlen(void)
{
	size_t	len;

	print_function("ft_strlen", "String length");
	len = ft_strlen("");
	print_test("ft_strlen(\"\")");
	print_output("0");
	test_result(len == 0, "empty string");
	print_divider();
	len = ft_strlen("hello");
	print_test("ft_strlen(\"hello\")");
	print_output("5");
	test_result(len == 5, "hello string");
	print_divider();
	len = ft_strlen("a");
	print_test("ft_strlen(\"a\")");
	print_output("1");
	test_result(len == 1, "single char");
}

void	test_strchr(void)
{
	char	*test_str;
	char	*chr;

	print_function("ft_strchr", "First character occurrence");
	test_str = "Hello World";
	chr = ft_strchr(test_str, 'H');
	print_test("ft_strchr(\"Hello World\", 'H')");
	print_output("\"Hello World\"");
	test_result(chr == &test_str[0], "found at start");
	print_divider();
	chr = ft_strchr(test_str, 'o');
	print_test("ft_strchr(\"Hello World\", 'o')");
	print_output("\"o World\"");
	test_result(chr == &test_str[4], "found first");
}

void	test_strrchr(void)
{
	char	*test_str;
	char	*chr;

	print_function("ft_strrchr", "Last character occurrence");
	test_str = "Hello World";
	chr = ft_strrchr(test_str, 'o');
	print_test("ft_strrchr(\"Hello World\", 'o')");
	print_output("\"orld\"");
	test_result(chr == &test_str[7], "found last");
	print_divider();
	chr = ft_strrchr(test_str, 'x');
	print_test("ft_strrchr(\"Hello World\", 'x')");
	print_output("NULL");
	test_result(chr == NULL, "not found");
}

void	test_strncmp(void)
{
	int	cmp;

	print_function("ft_strncmp", "String comparison");
	cmp = ft_strncmp("abc", "abc", 3);
	print_test("ft_strncmp(\"abc\", \"abc\", 3)");
	print_output("0");
	test_result(cmp == 0, "equal strings");
	print_divider();
	cmp = ft_strncmp("abc", "abd", 3);
	print_test("ft_strncmp(\"abc\", \"abd\", 3)");
	print_output("negative");
	test_result(cmp < 0, "less than");
	print_divider();
	cmp = ft_strncmp("abd", "abc", 3);
	print_test("ft_strncmp(\"abd\", \"abc\", 3)");
	print_output("positive");
	test_result(cmp > 0, "greater than");
}

void	test_strnstr(void)
{
	char	*chr;

	print_function("ft_strnstr", "Find substring");
	chr = ft_strnstr("hello", "ell", 10);
	print_test("ft_strnstr(\"hello\", \"ell\", 10)");
	print_output("\"ell\"");
	test_result(chr != NULL, "substring found");
	print_divider();
	chr = ft_strnstr("hello", "xyz", 10);
	print_test("ft_strnstr(\"hello\", \"xyz\", 10)");
	print_output("NULL");
	test_result(chr == NULL, "substring not found");
}
