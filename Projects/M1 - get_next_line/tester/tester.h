/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:10:32 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:54:10 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef TESTER_H
# define TESTER_H

# include "../get_next_line.h"
# include <stdio.h>
# include <fcntl.h>
# include <string.h>
# include <unistd.h>

# define BOLD_GREEN "\033[1;32m"
# define BOLD_RED "\033[1;31m"
# define BOLD_YELLOW "\033[1;33m"
# define BOLD_CYAN "\033[1;36m"
# define RESET "\033[0m"

typedef struct s_results
{
	int	passed;
	int	failed;
}	t_results;

void		print_header(void);
void		print_test_header(char *test_name);
void		print_result(int passed, char *description, t_results *res);
void		print_line_info(char *line, int line_num);
void		print_summary(t_results *res);
void		print_char(char c);

void		test_invalid_fd(t_results *res);
void		test_empty_file(t_results *res);
void		test_one_line(t_results *res);
void		test_multiple_lines(t_results *res);
void		test_no_newline_at_end(t_results *res);
void		test_only_newlines(t_results *res);
void		test_large_file(t_results *res);
void		test_stdin(t_results *res);
void		test_stdin_manual(void);

#endif
