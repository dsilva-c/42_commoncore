/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_memory_part3.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 18:01:26 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 18:01:27 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_memmove_memchr(void)
{
	test_memmove();
	printf("\n");
	test_memchr();
}

void	test_memcmp(void)
{
	print_function("ft_memcmp", "Compare memory");
	test_memcmp_equal();
	test_memcmp_less();
	test_memcmp_greater();
}

void	test_memory_functions(void)
{
	print_title("PART 3: MEMORY FUNCTIONS");
	test_memset_bzero_memcpy();
	printf("\n");
	test_memmove_memchr();
	printf("\n");
	test_memcmp();
}
