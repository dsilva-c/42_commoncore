/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus_tests3.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:29:50 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:30:15 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester_bonus.h"

static void	read_two_lines(int fd)
{
	char	*line;

	line = get_next_line(fd);
	print_line_info_bonus(line, fd, 1);
	free(line);
	line = get_next_line(fd);
	print_line_info_bonus(line, fd, 2);
	free(line);
	drain_fd(fd);
}

static void	reopen_and_check(t_results *res)
{
	int		fd;
	char	*line;

	fd = open("test_files/multiple_lines.txt", O_RDONLY);
	if (fd < 0)
		return ;
	line = get_next_line(fd);
	print_line_info_bonus(line, fd, 1);
	print_result_bonus(line != NULL && strcmp(line, "Line 1\n") == 0,
		"After reopen, reads from beginning", res);
	free(line);
	drain_fd(fd);
	close(fd);
}

void	test_close_and_reopen(t_results *res)
{
	int		fd;

	print_test_header_bonus("Close and Reopen File");
	fd = open("test_files/multiple_lines.txt", O_RDONLY);
	if (fd < 0)
		return ;
	read_two_lines(fd);
	close(fd);
	reopen_and_check(res);
	printf("\n");
}
