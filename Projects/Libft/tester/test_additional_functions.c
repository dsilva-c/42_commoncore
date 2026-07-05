/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_additional_functions.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 20:04:17 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 20:04:18 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_additional_part2(void)
{
	test_itoa();
	print_divider();
	test_strmapi();
}

void	test_additional_functions(void)
{
	print_title("PART 6: ADVANCED");
	test_additional_part1();
	printf("\n");
	test_additional_part2();
}
