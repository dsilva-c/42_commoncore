/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_tests2.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:24:52 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:25:04 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_no_newline_at_end(t_results *res)
{
	int		fd;
	char	*line;

	print_test_header("File Without Newline at End");
	fd = open("test_files/no_newline.txt", O_RDONLY);
	if (fd < 0)
	{
		printf(BOLD_RED "  Could not open file\n\n" RESET);
		return ;
	}
	line = get_next_line(fd);
	print_line_info(line, 1);
	print_result(line != NULL && strcmp(line, "Line without newline") == 0,
		"Reads line without trailing newline", res);
	free(line);
	line = get_next_line(fd);
	print_result(line == NULL, "Second call returns NULL (EOF)", res);
	free(line);
	close(fd);
	printf("\n");
}

static void	check_newlines(int fd, int *count, t_results *res)
{
	char	*line;

	*count = 0;
	line = get_next_line(fd);
	while (line != NULL)
	{
		(*count)++;
		if (strcmp(line, "\n") == 0)
			print_result(1, "Line is just newline", res);
		else
			print_result(0, "Line is not just newline", res);
		free(line);
		line = get_next_line(fd);
	}
}

void	test_only_newlines(t_results *res)
{
	int		fd;
	int		line_count;

	print_test_header("File With Only Newlines");
	fd = open("test_files/only_newlines.txt", O_RDONLY);
	if (fd < 0)
	{
		printf(BOLD_RED "  Could not open file\n\n" RESET);
		return ;
	}
	check_newlines(fd, &line_count, res);
	print_result(line_count == 3, "Read all 3 newlines correctly", res);
	close(fd);
	printf("\n");
}

static void	count_lines(int fd, int *count)
{
	char	*line;

	*count = 0;
	line = get_next_line(fd);
	while (line != NULL)
	{
		(*count)++;
		free(line);
		line = get_next_line(fd);
	}
}

void	test_large_file(t_results *res)
{
	int		fd;
	int		line_count;

	print_test_header("Large File (stress test)");
	fd = open("test_files/large_file.txt", O_RDONLY);
	if (fd < 0)
	{
		printf(BOLD_RED "  Could not open file\n\n" RESET);
		return ;
	}
	count_lines(fd, &line_count);
	printf("    Total lines read: %d\n", line_count);
	print_result(line_count == 1000, "Read all 1000 lines correctly", res);
	close(fd);
	printf("\n");
}
