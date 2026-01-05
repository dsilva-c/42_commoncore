/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_test_files2.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:31:27 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:31:34 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>

void	create_directory(void);
void	create_basic_files(void);
void	create_multiple_lines_file(void);
void	create_special_files(void);

static void	create_large_file(void)
{
	FILE	*f;
	int		i;

	f = fopen("test_files/large_file.txt", "w");
	if (f)
	{
		i = 0;
		while (i < 1000)
		{
			fprintf(f, "This is line number %d\n", i + 1);
			i++;
		}
		fclose(f);
	}
	printf("  📄 Created large_file.txt (1000 lines)\n");
}

int	main(void)
{
	printf("\n  📁 Creating test files...\n\n");
	create_directory();
	create_basic_files();
	create_multiple_lines_file();
	create_special_files();
	create_large_file();
	printf("\n ✅ All test files created! Ready to test! 🚀\n\n");
	return (0);
}
