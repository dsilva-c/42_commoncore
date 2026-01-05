/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_additional_part1.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:47:22 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:47:23 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_substr(void)
{
	char	*result;

	print_function("ft_substr", "Extract substring");
	print_memory_check("ft_substr");
	result = ft_substr("hello", 1, 3);
	print_test("ft_substr(\"hello\", 1, 3)");
	print_output("\"ell\"");
	test_result(result != NULL && strcmp(result, "ell") == 0,
		"substring extracted");
	free(result);
	print_divider();
	result = ft_substr("hello", 0, 5);
	print_test("ft_substr(\"hello\", 0, 5)");
	print_output("\"hello\"");
	test_result(result != NULL && strcmp(result, "hello") == 0,
		"full string");
	free(result);
	print_output("Memory freed successfully");
}

void	test_strjoin(void)
{
	char	*result;

	print_function("ft_strjoin", "Concatenate strings");
	print_memory_check("ft_strjoin");
	result = ft_strjoin("hello", " world");
	print_test("ft_strjoin(\"hello\", \" world\")");
	print_output("\"hello world\"");
	test_result(result != NULL && strcmp(result, "hello world") == 0,
		"joined");
	free(result);
	print_divider();
	result = ft_strjoin("", "test");
	print_test("ft_strjoin(\"\", \"test\")");
	print_output("\"test\"");
	test_result(result != NULL && strcmp(result, "test") == 0,
		"empty first");
	free(result);
	print_output("Memory freed successfully");
}

void	test_strtrim(void)
{
	char	*result;

	print_function("ft_strtrim", "Trim string");
	print_memory_check("ft_strtrim");
	result = ft_strtrim("  hello  ", " ");
	print_test("ft_strtrim(\"  hello  \", \" \")");
	print_output("\"hello\"");
	test_result(result != NULL && strcmp(result, "hello") == 0,
		"trimmed");
	free(result);
	print_divider();
	result = ft_strtrim("hello", " ");
	print_test("ft_strtrim(\"hello\", \" \")");
	print_output("\"hello\"");
	test_result(result != NULL && strcmp(result, "hello") == 0,
		"no trim needed");
	free(result);
	print_output("Memory freed successfully");
}

void	test_split(void)
{
	char	**split;
	int		i;

	print_function("ft_split", "Split string by delimiter");
	print_memory_check("ft_split");
	split = ft_split("a,b,c", ',');
	print_test("ft_split(\"a,b,c\", ',')");
	print_output("Array: [\"a\", \"b\", \"c\", NULL]");
	if (split)
	{
		i = 0;
		while (split[i])
		{
			printf("      [%d]: \"%s\"\n", i, split[i]);
			i++;
		}
		test_result(strcmp(split[0], "a") == 0, "split correctly");
		free_split(split);
	}
}

void	test_additional_part1(void)
{
	test_substr();
	printf("\n");
	test_strjoin();
	printf("\n");
	test_strtrim();
	printf("\n");
	test_split();
}
