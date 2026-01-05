/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus_tests2.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:29:36 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:29:44 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester_bonus.h"

static void	alternate_read_loop(int fd1, int fd2)
{
	char	*line;
	int		i;

	i = 0;
	while (i < 3)
	{
		line = get_next_line(fd1);
		print_line_info_bonus(line, fd1, i + 1);
		free(line);
		line = get_next_line(fd2);
		print_line_info_bonus(line, fd2, i + 1);
		free(line);
		i++;
	}
}

void	test_alternating_reads(t_results *res)
{
	int		fd1;
	int		fd2;

	print_test_header_bonus("Alternating Reads Between Two Files");
	fd1 = open("test_files/multiple_lines.txt", O_RDONLY);
	fd2 = open("test_files/only_newlines.txt", O_RDONLY);
	if (fd1 < 0 || fd2 < 0)
	{
		printf(BOLD_RED "  Could not open test files\n\n" RESET);
		return ;
	}
	alternate_read_loop(fd1, fd2);
	print_result_bonus(1, "Alternating reads completed", res);
	drain_fd(fd1);
	close(fd1);
	close(fd2);
	printf("\n");
}

static void	compare_fd_positions(int fd1, int fd2, t_results *res)
{
	char	*line1;
	char	*line2;

	line1 = get_next_line(fd1);
	line2 = get_next_line(fd2);
	print_line_info_bonus(line1, fd1, 1);
	print_line_info_bonus(line2, fd2, 1);
	print_result_bonus(line1 != NULL && line2 != NULL
		&& strcmp(line1, line2) == 0, "Both FDs read same first line", res);
	free(line1);
	free(line2);
	line1 = get_next_line(fd1);
	free(line1);
	line1 = get_next_line(fd1);
	line2 = get_next_line(fd2);
	print_line_info_bonus(line1, fd1, 3);
	print_line_info_bonus(line2, fd2, 2);
	print_result_bonus(line1 != NULL && line2 != NULL
		&& strcmp(line1, line2) != 0, "FDs maintain separate positions", res);
	free(line1);
	free(line2);
}

void	test_same_file_different_fd(t_results *res)
{
	int		fd1;
	int		fd2;

	print_test_header_bonus("Same File Opened Twice (Different FDs)");
	fd1 = open("test_files/multiple_lines.txt", O_RDONLY);
	fd2 = open("test_files/multiple_lines.txt", O_RDONLY);
	if (fd1 < 0 || fd2 < 0)
	{
		printf(BOLD_RED "  Could not open test files\n\n" RESET);
		return ;
	}
	compare_fd_positions(fd1, fd2, res);
	drain_fd(fd1);
	drain_fd(fd2);
	close(fd1);
	close(fd2);
	printf("\n");
}
