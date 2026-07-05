/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_memory_part1.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 18:00:07 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 18:00:08 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_memset(void)
{
	char	buf1[10];
	char	buf2[10];
	int		cmp;

	print_function("ft_memset", "Set bytes to value");
	ft_memset(buf1, 'A', 5);
	memset(buf2, 'A', 5);
	cmp = memcmp(buf1, buf2, 5);
	print_test("Set 5 bytes to 'A'");
	print_output("5 bytes filled");
	test_result(cmp == 0, "memory set correctly");
}

void	test_bzero(void)
{
	char	buf1[10];
	char	buf2[10];
	int		cmp;

	print_function("ft_bzero", "Set bytes to zero");
	strcpy(buf1, "abcde");
	strcpy(buf2, "abcde");
	ft_bzero(buf1, 3);
	bzero(buf2, 3);
	cmp = memcmp(buf1, buf2, 5);
	print_test("Zero first 3 bytes");
	print_output("3 bytes zeroed");
	test_result(cmp == 0, "memory zeroed");
}

void	test_memcpy(void)
{
	char	buf1[10];
	char	buf2[10];
	int		cmp;

	print_function("ft_memcpy", "Copy memory");
	strcpy(buf1, "hello");
	strcpy(buf2, "hello");
	ft_memcpy(buf1, "test", 4);
	memcpy(buf2, "test", 4);
	cmp = memcmp(buf1, buf2, 5);
	print_test("Copy 4 bytes");
	print_output("memory copied");
	test_result(cmp == 0, "copy correctly");
}

void	test_memset_bzero_memcpy(void)
{
	test_memset();
	printf("\n");
	test_bzero();
	printf("\n");
	test_memcpy();
}
