/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_bonus.h                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/21 03:48:53 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/21 03:50:25 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_BONUS_H
# define FT_PRINTF_BONUS_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include "../libft/libft.h"

typedef struct s_flags
{
	int	minus;
	int	zero;
	int	hash;
	int	space;
	int	plus;
	int	width;
	int	precision;
	int	dot;
}	t_flags;

int		ft_printf(const char *format, ...);
int		ft_parse_flags(const char *format, int *i, t_flags *flags);
int		ft_handle_conversion(char spec, va_list args, t_flags flags);
int		ft_print_char_bonus(char c, t_flags flags);
int		ft_print_string_bonus(char *s, t_flags flags);
int		ft_print_number_bonus(int n, t_flags flags);
int		ft_print_unsigned_bonus(unsigned int n, t_flags flags);
int		ft_print_hex_bonus(unsigned int n, char spec, t_flags flags);
int		ft_print_pointer_bonus(void *ptr, t_flags flags);
int		ft_print_percent_bonus(t_flags flags);
int		ft_putchar_count(char c);
int		ft_putstr_count(char *s);
int		ft_numlen(long n);
int		ft_hexlen(unsigned long n);
int		ft_print_width(int width, int zero);
void	ft_init_flags(t_flags *flags);
int		ft_atoi_mini(const char *str);

#endif
