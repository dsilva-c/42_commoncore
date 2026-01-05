/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:07:58 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:09:06 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static void	init_results(t_results *res)
{
	res->passed = 0;
	res->failed = 0;
}

static void	run_file_tests(t_results *res)
{
	test_invalid_fd(res);
	test_empty_file(res);
	test_one_line(res);
	test_multiple_lines(res);
	test_no_newline_at_end(res);
	test_only_newlines(res);
	test_large_file(res);
}

int	main(int argc, char **argv)
{
	t_results	res;

	init_results(&res);
	print_header();
	if (argc > 1 && strcmp(argv[1], "manual") == 0)
	{
		test_stdin_manual();
		return (0);
	}
	if (!isatty(0))
	{
		test_stdin(&res);
		print_summary(&res);
		return (res.failed > 0);
	}
	run_file_tests(&res);
	print_summary(&res);
	return (res.failed > 0);
}
