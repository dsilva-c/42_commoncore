/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 01:28:24 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/06 01:29:38 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef TESTER_H
# define TESTER_H

# include "../includes/ft_printf_bonus.h"
# include <stdio.h>
# include <limits.h>

# define BOLD_GREEN "\033[1;32m"
# define BOLD_RED "\033[1;31m"
# define BOLD_YELLOW "\033[1;33m"
# define BOLD_CYAN "\033[1;36m"
# define BOLD_WHITE "\033[1;37m"
# define RESET "\033[0m"

typedef struct s_results
{
	int	passed;
	int	failed;
}	t_results;

void	print_header(void);
void	print_test_header(char *test_name);
void	print_result(int passed, char *desc, t_results *res);
void	print_summary(t_results *res);
void	print_comparison(int r1, int r2);

void	test_char(t_results *res);
void	test_string(t_results *res);
void	test_int(t_results *res);
void	test_unsigned(t_results *res);
void	test_hex(t_results *res);
void	test_ptr(t_results *res);
void	test_percent(t_results *res);

void	test_width(t_results *res);
void	test_precision(t_results *res);
void	test_flags(t_results *res);
void	test_combos(t_results *res);
void	test_mix(t_results *res);
void	test_hardcore(t_results *res);

#endif
