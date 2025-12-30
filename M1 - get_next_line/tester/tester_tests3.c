/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_tests3.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/07 18:42:34 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/07 18:42:54 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_stdin(t_results *res)
{
	char	*line;

	print_test_header("Standard Input (Automated Pipe)");
	printf("    (Reading piped input...)\n");
	line = get_next_line(0);
	print_line_info(line, 1);
	print_result(line != NULL && strcmp(line, "Hello Stdin!\n") == 0,
		"Correctly read from stdin", res);
	free(line);
	line = get_next_line(0);
	print_result(line == NULL, "Stdin returns NULL at EOF", res);
	free(line);
	printf("\n");
}

void	test_stdin_manual(void)
{
	char	*line;
	int		i;

	print_test_header("Standard Input (Manual Mode)");
	printf(BOLD_CYAN "  👉 Type text and press ENTER.\n");
	printf("  👉 Press Ctrl + D to finish.\n\n" RESET);
	i = 1;
	line = get_next_line(0);
	while (line != NULL)
	{
		print_line_info(line, i++);
		free(line);
		line = get_next_line(0);
	}
	printf(BOLD_GREEN "\n  (EOF Reached. Test finished.)\n\n" RESET);
}
