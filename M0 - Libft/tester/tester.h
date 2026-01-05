/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:16:58 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:44:38 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef TESTER_H
# define TESTER_H

# include "libft.h"
# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <unistd.h>
# include <limits.h>

/* ========== COLOR DEFINITIONS ========== */
# define BOLD_GREEN "\033[1;32m"
# define BOLD_RED "\033[1;31m"
# define BOLD_CYAN "\033[1;36m"
# define BOLD_WHITE "\033[1;37m"
# define BOLD_MAGENTA "\033[1;35m"
# define BOLD_YELLOW "\033[1;33m"
# define YELLOW "\033[0;33m"
# define RESET "\033[0m"

/* ========== COUNTERS STORAGE ACCESSOR ========== */
int		*get_counters_ptr(void);

/* ========== GETTERS FOR OTHER FILES ========== */
int		get_g_tests(void);
int		get_g_passed(void);
int		get_g_failed(void);

/* ========== UTILITY FUNCTIONS ========== */
void	init_counters(void);
void	test_result(int cond, const char *name);
void	print_title(const char *title);
void	print_function(const char *fname, const char *description);
char	ft_upper_char(unsigned int i, char c);
void	print_test(const char *test_desc);
void	print_output(const char *output_desc);
void	print_memory_check(const char *label);
void	print_divider(void);
void	free_split(char **split);
void	print_success_rate(void);
void	print_final_message(void);
void	print_summary(void);

/* ========== CHARACTER TESTS (helpers) ========== */
void	test_isalpha(void);
void	test_isdigit(void);
void	test_isalnum(void);
void	test_isascii(void);
void	test_isprint(void);
void	test_toupper(void);
void	test_tolower(void);
void	test_character_part1(void);
void	test_character_part2(void);
void	test_character_functions(void);

/* ========== STRING TESTS (helpers) ========== */
void	test_strlen(void);
void	test_strchr(void);
void	test_strchr_not_found(void);
void	test_strrchr(void);
void	test_strncmp(void);
void	test_strnstr(void);
void	test_atoi_positive(void);
void	test_atoi_negative(void);
void	test_atoi(void);
void	test_string_functions(void);

/* ========== MEMORY TESTS (helpers) ========== */
void	test_memset(void);
void	test_bzero(void);
void	test_memcpy(void);
void	test_memset_bzero_memcpy(void);
void	test_memmove(void);
void	test_memchr(void);
void	test_memmove_memchr(void);
void	test_memcmp_equal(void);
void	test_memcmp_less(void);
void	test_memcmp_greater(void);
void	test_memcmp(void);
void	test_memory_functions(void);

/* ========== COPY TESTS (helpers) ========== */
void	test_strlcpy(void);
void	test_strlcat(void);
void	test_copy_functions(void);

/* ========== ALLOCATION TESTS (helpers) ========== */
void	test_calloc(void);
void	test_strdup(void);
void	test_allocation_functions(void);

/* ========== ADVANCED / ADDITIONAL TESTS (helpers) ========== */
void	test_substr(void);
void	test_strjoin(void);
void	test_strtrim(void);
void	test_split(void);
void	test_additional_part1(void);
void	test_itoa_positive(void);
void	test_itoa_negative(void);
void	test_itoa_zero(void);
void	test_itoa(void);
void	test_strmapi(void);
void	test_additional_part2(void);
void	test_additional_part1(void);
void	test_additional_functions(void);

/* ========== OUTPUT TESTS (helpers) ========== */
void	test_putchar_fd(void);
void	test_putstr_fd(void);
void	test_putendl_fd(void);
void	test_putchar_putstr(void);
void	test_putendl_putnbr(void);
void	test_putnbr_negative(void);
void	test_putnbr_int_min(void);
void	test_putnbr_zero(void);
void	test_putnbr_all(void);
void	test_output_functions(void);

/* ========== BONUS - LIST HELPERS & TESTS ========== */
void	print_list_node(void *content);
void	del_list_content(void *content);
void	*dup_list_content(void *content);
void	test_lstnew_lstadd_front(void);
void	helper_bonus_part1(void);
void	test_lstsize(void);
void	test_lstlast(void);
void	test_lstadd_back(void);
void	test_lstiter(void);
void	helper_bonus_part2(void);
void	test_lstdelone(void);
void	test_lstmap(void);
void	test_lstclear(void);
void	test_bonus_functions(void);

/* ========== MAIN ENTRYPOINT ========== */
void	print_header(void);
void	run_all_tests(void);

#endif
