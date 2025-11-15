/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_allocation.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:56:36 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/01 00:18:42 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_calloc(void)
{
	int	*arr;
	int	i;

	print_function("ft_calloc", "Allocate and zero");
	print_memory_check("ft_calloc");
	arr = ft_calloc(5, sizeof(int));
	print_test("Allocate 5 integers");
	print_output("Memory allocated and zeroed");
	test_result(arr != NULL, "allocation successful");
	i = 0;
	while (i < 5 && arr[i] == 0)
		i++;
	print_test("Verify memory is zeroed");
	print_output("All 5 integers are 0");
	test_result(i == 5, "memory is zeroed");
	free(arr);
	print_output("Memory freed successfully");
}

void	test_strdup(void)
{
	char	*dup;
	char	str_hello[6];

	print_function("ft_strdup", "Duplicate string");
	print_memory_check("ft_strdup");
	strcpy(str_hello, "hello");
	dup = ft_strdup(str_hello);
	print_test("Duplicate \"hello\"");
	print_output("New string allocated");
	test_result(dup != NULL && strcmp(dup, str_hello) == 0,
		"string duplicated");
	free(dup);
	print_divider();
	dup = ft_strdup("");
	print_test("Duplicate empty string");
	print_output("Empty string duplicated");
	test_result(dup != NULL && strcmp(dup, "") == 0, "empty string dup");
	free(dup);
	print_output("Memory freed successfully");
}

void	test_allocation_functions(void)
{
	print_title("PART 5: ALLOCATION AND STRING DUPLICATION");
	test_calloc();
	printf("\n");
	test_strdup();
}
