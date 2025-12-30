/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:11:12 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:11:50 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester_bonus.h"

static void	init_results(t_results *res)
{
	res->passed = 0;
	res->failed = 0;
}

int	main(void)
{
	t_results	res;

	init_results(&res);
	print_header_bonus();
	test_invalid_fd_bonus(&res);
	test_multiple_fd(&res);
	test_alternating_reads(&res);
	test_same_file_different_fd(&res);
	test_close_and_reopen(&res);
	test_many_fds(&res);
	print_summary_bonus(&res);
	return (res.failed > 0);
}
