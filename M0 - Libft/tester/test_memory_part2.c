/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_memory_part2.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 18:00:39 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 18:00:40 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_memmove(void)
{
	char	buf1[10];
	char	buf2[10];
	int		cmp;

	print_function("ft_memmove", "Move memory (overlap)");
	strcpy(buf1, "abcde");
	strcpy(buf2, "abcde");
	ft_memmove(buf1 + 1, buf1, 3);
	memmove(buf2 + 1, buf2, 3);
	cmp = memcmp(buf1, buf2, 5);
	print_test("Move overlapping memory");
	print_output("overlap handled");
	test_result(cmp == 0, "memmove correctly");
}

void	test_memchr(void)
{
	char	*chr;

	print_function("ft_memchr", "Search byte in memory");
	chr = ft_memchr("hello", 'e', 5);
	print_test("ft_memchr(\"hello\", 'e', 5)");
	print_output("byte found");
	test_result(chr != NULL, "byte found");
	print_divider();
	chr = ft_memchr("hello", 'x', 5);
	print_test("ft_memchr(\"hello\", 'x', 5)");
	print_output("NULL");
	test_result(chr == NULL, "byte not found");
}

void	test_memcmp_equal(void)
{
	int	cmp;

	cmp = ft_memcmp("abc", "abc", 3);
	print_test("ft_memcmp(\"abc\", \"abc\", 3)");
	print_output("0");
	test_result(cmp == 0, "equal memory");
}

void	test_memcmp_less(void)
{
	int	cmp;

	print_divider();
	cmp = ft_memcmp("abc", "abd", 3);
	print_test("ft_memcmp(\"abc\", \"abd\", 3)");
	print_output("negative");
	test_result(cmp < 0, "less than");
}

void	test_memcmp_greater(void)
{
	int	cmp;

	print_divider();
	cmp = ft_memcmp("abd", "abc", 3);
	print_test("ft_memcmp(\"abd\", \"abc\", 3)");
	print_output("positive");
	test_result(cmp > 0, "greater than");
}
