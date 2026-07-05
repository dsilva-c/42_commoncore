/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_copy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:55:51 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:55:53 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_strlcpy(void)
{
	char	dst[20];
	char	src[20];
	size_t	ret;

	print_function("ft_strlcpy", "Safe string copy");
	strcpy(src, "hello");
	ret = ft_strlcpy(dst, src, sizeof(dst));
	print_test("Copy \"hello\"");
	print_output("destination: \"hello\"");
	test_result(strcmp(dst, src) == 0 && ret == strlen(src),
		"strlcpy correctly");
	print_divider();
	strcpy(src, "truncate");
	ret = ft_strlcpy(dst, src, 4);
	print_test("Truncate \"truncate\" to 3 chars");
	print_output("destination: \"tru\"");
	test_result(ret == strlen(src), "strlcpy returns source length");
}

void	test_strlcat(void)
{
	char	dst[20];
	char	src[20];
	size_t	ret;
	size_t	expected;

	print_function("ft_strlcat", "Safe string concat");
	strcpy(dst, "hello");
	strcpy(src, " world");
	ret = ft_strlcat(dst, src, sizeof(dst));
	print_test("Concatenate strings");
	print_output("\"hello world\"");
	expected = strlen("hello") + strlen(" world");
	test_result(strcmp(dst, "hello world") == 0
		&& ret == expected, "strlcat correctly");
}

void	test_copy_functions(void)
{
	print_title("PART 4: STRING COPY AND CONCATENATION");
	test_strlcpy();
	printf("\n");
	test_strlcat();
}
