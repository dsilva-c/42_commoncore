/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_string_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:16:14 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:16:20 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

static int	ft_print_str_precision(char *s, int precision)
{
	int	count;
	int	i;

	count = 0;
	i = 0;
	while (s[i] && i < precision)
	{
		count += ft_putchar_count(s[i]);
		i++;
	}
	return (count);
}

int	ft_print_string_bonus(char *s, t_flags flags)
{
	int	count;
	int	len;
	int	print_len;

	count = 0;
	if (!s)
		s = "(null)";
	len = ft_strlen(s);
	print_len = len;
	if (flags.dot && flags.precision < len)
		print_len = flags.precision;
	if (flags.minus)
	{
		count += ft_print_str_precision(s, print_len);
		count += ft_print_width(flags.width - print_len, 0);
	}
	else
	{
		count += ft_print_width(flags.width - print_len, 0);
		count += ft_print_str_precision(s, print_len);
	}
	return (count);
}
