/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus_tests.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:12:27 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:12:45 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester_bonus.h"

void	test_invalid_fd_bonus(t_results *res)
{
	char	*line;

	print_test_header_bonus("Invalid File Descriptor");
	line = get_next_line(-1);
	print_result_bonus(line == NULL, "fd = -1 returns NULL", res);
	free(line);
	line = get_next_line(-42);
	print_result_bonus(line == NULL, "fd = -42 returns NULL", res);
	free(line);
	line = get_next_line(10000);
	print_result_bonus(line == NULL, "fd >= FD_MAX returns NULL", res);
	free(line);
	printf("\n");
}

static void	test_fd1(int fd1, t_results *res)
{
	char	*line;

	line = get_next_line(fd1);
	print_line_info_bonus(line, fd1, 1);
	print_result_bonus(line != NULL && strcmp(line, "Hello World!\n") == 0,
		"fd1: First line correct", res);
	free(line);
}

static void	test_fd2_fd3(int fd2, int fd3, t_results *res)
{
	char	*line2;
	char	*line3;

	line2 = get_next_line(fd2);
	print_line_info_bonus(line2, fd2, 1);
	print_result_bonus(line2 != NULL && strcmp(line2, "Line 1\n") == 0,
		"fd2: First line correct", res);
	line3 = get_next_line(fd3);
	print_line_info_bonus(line3, fd3, 1);
	print_result_bonus(line3 != NULL, "fd3: First line correct", res);
	free(line2);
	free(line3);
	line2 = get_next_line(fd2);
	print_line_info_bonus(line2, fd2, 2);
	print_result_bonus(line2 != NULL && strcmp(line2, "Line 2\n") == 0,
		"fd2: Second line correct", res);
	free(line2);
}

void	test_multiple_fd(t_results *res)
{
	int		fd1;
	int		fd2;
	int		fd3;

	print_test_header_bonus("Multiple File Descriptors Simultaneously");
	fd1 = open("test_files/one_line.txt", O_RDONLY);
	fd2 = open("test_files/multiple_lines.txt", O_RDONLY);
	fd3 = open("test_files/no_newline.txt", O_RDONLY);
	if (fd1 < 0 || fd2 < 0 || fd3 < 0)
	{
		printf(BOLD_RED "  Could not open test files\n\n" RESET);
		return ;
	}
	test_fd1(fd1, res);
	test_fd2_fd3(fd2, fd3, res);
	drain_fd(fd2);
	close(fd1);
	close(fd2);
	close(fd3);
	printf("\n");
}
