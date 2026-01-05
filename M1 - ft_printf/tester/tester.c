/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 02:40:06 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 02:40:17 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static void	init_results(t_results *res)
{
	res->passed = 0;
	res->failed = 0;
}

int	main(void)
{
	t_results	res;

	init_results(&res);
	print_header();
	test_char(&res);
	test_string(&res);
	test_int(&res);
	test_unsigned(&res);
	test_hex(&res);
	test_ptr(&res);
	test_percent(&res);
	test_width(&res);
	test_precision(&res);
	test_flags(&res);
	test_combos(&res);
	test_mix(&res);
	test_hardcore(&res);
	print_summary(&res);
	return (res.failed > 0);
}
