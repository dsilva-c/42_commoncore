/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus_tests4.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 20:46:45 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 20:46:51 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester_bonus.h"

static void	open_fds(int *fds, int *success)
{
	int	i;

	i = -1;
	*success = 1;
	while (++i < 10)
	{
		fds[i] = open("test_files/one_line.txt", O_RDONLY);
		if (fds[i] < 0)
			*success = 0;
	}
}

static void	read_and_close_fds(int *fds, int *success)
{
	char	*line;
	int		i;

	i = -1;
	while (++i < 10)
	{
		line = get_next_line(fds[i]);
		if (line == NULL || strcmp(line, "Hello World!\n") != 0)
			*success = 0;
		free(line);
		drain_fd(fds[i]);
		close(fds[i]);
	}
}

void	test_many_fds(t_results *res)
{
	int		fds[10];
	int		success;

	print_test_header_bonus("Many File Descriptors (10 files)");
	open_fds(fds, &success);
	if (! success)
	{
		printf(BOLD_RED "  Could not open test files\n\n" RESET);
		return ;
	}
	read_and_close_fds(fds, &success);
	print_result_bonus(success, "All 10 FDs read correctly", res);
	printf("\n");
}
