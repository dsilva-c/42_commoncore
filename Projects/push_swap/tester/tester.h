/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:10:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:10:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef TESTER_H
# define TESTER_H

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <unistd.h>
# include <time.h>

/* ========== COLOR DEFINITIONS ========== */
# define BOLD_GREEN "\033[1;32m"
# define BOLD_RED "\033[1;31m"
# define BOLD_CYAN "\033[1;36m"
# define BOLD_WHITE "\033[1;37m"
# define BOLD_MAGENTA "\033[1;35m"
# define BOLD_YELLOW "\033[1;33m"
# define YELLOW "\033[0;33m"
# define RESET "\033[0m"

/* ========== RESULTS TRACKER ========== */
typedef struct s_results
{
	int	passed;
	int	failed;
}	t_results;

/* ========== PRINT FUNCTIONS ========== */
void	print_header(void);
void	print_test_header(const char *title);
void	print_result(int passed, const char *desc, t_results *res);
void	print_perf_result(int moves, int limit, int ok,
			const char *desc, t_results *res);
void	print_summary(t_results *res);

/* ========== UTILITY FUNCTIONS ========== */
int		get_move_count(const char *args);
int		verify_sort(const char *args);
int		check_error(const char *args);
int		check_no_output(const char *args);
void	gen_random_args(char *buf, int buf_size, int count);

/* ========== TEST FUNCTIONS ========== */
void	test_identity(t_results *res);
void	test_small_sort(t_results *res);
void	test_error_handling(t_results *res);
void	test_performance_100(t_results *res);
void	test_performance_500(t_results *res);
void	test_bonus_checker(t_results *res);

#endif
