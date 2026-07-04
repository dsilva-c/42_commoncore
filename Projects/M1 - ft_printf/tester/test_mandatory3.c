/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_mandatory3.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 03:03:13 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 03:03:19 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_percent(t_results *res)
{
	int	r1;
	int	r2;

	print_test_header("Percent %%");
	printf("    Real: ");
	fflush(stdout);
	r1 = printf("%%");
	printf("\n    Mine: ");
	fflush(stdout);
	r2 = ft_printf("%%");
	print_comparison(r1, r2);
	print_result(r1 == r2, "Percent Sign", res);
}
