/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parse_bonus.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:10:40 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:10:57 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

static void	ft_parse_flag_chars(const char *format, int *i, t_flags *flags)
{
	while (format[*i] == '-' || format[*i] == '0' || format[*i] == '#'
		|| format[*i] == ' ' || format[*i] == '+')
	{
		if (format[*i] == '-')
			flags->minus = 1;
		else if (format[*i] == '0')
			flags->zero = 1;
		else if (format[*i] == '#')
			flags->hash = 1;
		else if (format[*i] == ' ')
			flags->space = 1;
		else if (format[*i] == '+')
			flags->plus = 1;
		(*i)++;
	}
}

static void	ft_parse_width(const char *format, int *i, t_flags *flags)
{
	if (ft_isdigit(format[*i]))
	{
		flags->width = ft_atoi_mini(&format[*i]);
		while (ft_isdigit(format[*i]))
			(*i)++;
	}
}

static void	ft_parse_precision(const char *format, int *i, t_flags *flags)
{
	if (format[*i] == '.')
	{
		flags->dot = 1;
		(*i)++;
		if (ft_isdigit(format[*i]))
		{
			flags->precision = ft_atoi_mini(&format[*i]);
			while (ft_isdigit(format[*i]))
				(*i)++;
		}
		else
			flags->precision = 0;
	}
}

int	ft_parse_flags(const char *format, int *i, t_flags *flags)
{
	ft_init_flags(flags);
	ft_parse_flag_chars(format, i, flags);
	ft_parse_width(format, i, flags);
	ft_parse_precision(format, i, flags);
	if (flags->minus)
		flags->zero = 0;
	return (0);
}
