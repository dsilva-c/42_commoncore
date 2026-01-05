/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_tests.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:09:49 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:10:06 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_invalid_fd(t_results *res)
{
	char	*line;

	print_test_header("Invalid File Descriptor");
	line = get_next_line(-1);
	print_result(line == NULL, "fd = -1 returns NULL", res);
	free(line);
	line = get_next_line(-42);
	print_result(line == NULL, "fd = -42 returns NULL", res);
	free(line);
	printf("\n");
}

void	test_empty_file(t_results *res)
{
	int		fd;
	char	*line;

	print_test_header("Empty File");
	fd = open("test_files/empty.txt", O_RDONLY);
	if (fd < 0)
	{
		printf(BOLD_RED "  Could not open file\n\n" RESET);
		return ;
	}
	line = get_next_line(fd);
	print_result(line == NULL, "Empty file returns NULL", res);
	free(line);
	close(fd);
	printf("\n");
}

void	test_one_line(t_results *res)
{
	int		fd;
	char	*line;

	print_test_header("One Line File");
	fd = open("test_files/one_line.txt", O_RDONLY);
	if (fd < 0)
	{
		printf(BOLD_RED "  Could not open file\n\n" RESET);
		return ;
	}
	line = get_next_line(fd);
	print_line_info(line, 1);
	print_result(line != NULL && strcmp(line, "Hello World!\n") == 0,
		"First line is correct", res);
	free(line);
	line = get_next_line(fd);
	print_result(line == NULL, "Second call returns NULL (EOF)", res);
	free(line);
	close(fd);
	printf("\n");
}

static void	read_all_lines(int fd, int *count)
{
	char	*line;

	*count = 0;
	line = get_next_line(fd);
	while (line != NULL)
	{
		(*count)++;
		print_line_info(line, *count);
		free(line);
		line = get_next_line(fd);
	}
}

void	test_multiple_lines(t_results *res)
{
	int		fd;
	int		line_count;

	print_test_header("Multiple Lines File");
	fd = open("test_files/multiple_lines.txt", O_RDONLY);
	if (fd < 0)
	{
		printf(BOLD_RED "  Could not open file\n\n" RESET);
		return ;
	}
	read_all_lines(fd, &line_count);
	print_result(line_count == 5, "Read all 5 lines correctly", res);
	close(fd);
	printf("\n");
}
