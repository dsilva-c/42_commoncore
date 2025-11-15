/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_utils_part1.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:25:50 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:25:57 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

int	*get_counters_ptr(void)
{
	static int	counters[3];

	return (counters);
}

void	init_counters(void)
{
	int	*c;

	c = get_counters_ptr();
	c[0] = 0;
	c[1] = 0;
	c[2] = 0;
}

void	test_result(int cond, const char *name)
{
	int	*c;

	c = get_counters_ptr();
	c[0]++;
	if (cond)
	{
		printf(BOLD_GREEN "      ✓ PASS" RESET " | %s\n", name);
		c[1]++;
	}
	else
	{
		printf(BOLD_RED "      ✗ FAIL" RESET " | %s\n", name);
		c[2]++;
	}
}
