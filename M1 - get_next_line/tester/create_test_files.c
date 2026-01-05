/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_test_files.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:13:42 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:13:46 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>

void	create_directory(void)
{
	struct stat	st;

	if (stat("test_files", &st) == -1)
	{
		mkdir("test_files", 0755);
		printf("  📁 Created test_files directory\n");
	}
}

void	create_basic_files(void)
{
	FILE	*f;

	f = fopen("test_files/empty.txt", "w");
	if (f)
		fclose(f);
	printf("  📄 Created empty.txt\n");
	f = fopen("test_files/one_line.txt", "w");
	if (f)
	{
		fprintf(f, "Hello World!\n");
		fclose(f);
	}
	printf("  📄 Created one_line.txt\n");
}

void	create_multiple_lines_file(void)
{
	FILE	*f;

	f = fopen("test_files/multiple_lines.txt", "w");
	if (f)
	{
		fprintf(f, "Line 1\n");
		fprintf(f, "Line 2\n");
		fprintf(f, "Line 3\n");
		fprintf(f, "Line 4\n");
		fprintf(f, "Line 5\n");
		fclose(f);
	}
	printf("  📄 Created multiple_lines.txt\n");
}

void	create_special_files(void)
{
	FILE	*f;

	f = fopen("test_files/no_newline.txt", "w");
	if (f)
	{
		fprintf(f, "Line without newline");
		fclose(f);
	}
	printf("  📄 Created no_newline.txt\n");
	f = fopen("test_files/only_newlines.txt", "w");
	if (f)
	{
		fprintf(f, "\n\n\n");
		fclose(f);
	}
	printf("  📄 Created only_newlines.txt\n");
}
