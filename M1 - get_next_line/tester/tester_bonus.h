/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus.h                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 19:13:11 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 19:13:17 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef TESTER_BONUS_H
# define TESTER_BONUS_H

# include "../get_next_line_bonus.h"
# include <stdio.h>
# include <fcntl.h>
# include <string.h>

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

void		print_header_bonus(void);
void		print_test_header_bonus(char *test_name);
void		print_result_bonus(int passed, char *desc, t_results *res);
void		print_line_info_bonus(char *line, int fd, int line_num);
void		print_summary_bonus(t_results *res);
void		print_char_bonus(char c);
void		drain_fd(int fd);

void		test_invalid_fd_bonus(t_results *res);
void		test_multiple_fd(t_results *res);
void		test_alternating_reads(t_results *res);
void		test_same_file_different_fd(t_results *res);
void		test_close_and_reopen(t_results *res);
void		test_many_fds(t_results *res);

#endif
