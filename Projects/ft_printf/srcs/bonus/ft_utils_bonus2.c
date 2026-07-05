/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils_bonus2.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:13:56 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:14:22 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

int	ft_atoi_mini(const char *str)
{
	int	result;

	result = 0;
	while (*str && ft_isdigit(*str))
	{
		result = result * 10 + (*str - '0');
		str++;
	}
	return (result);
}

void	ft_init_flags(t_flags *flags)
{
	flags->minus = 0;
	flags->zero = 0;
	flags->hash = 0;
	flags->space = 0;
	flags->plus = 0;
	flags->width = 0;
	flags->precision = -1;
	flags->dot = 0;
}

int	ft_print_width(int width, int zero)
{
	int		count;
	char	pad;

	count = 0;
	if (zero)
		pad = '0';
	else
		pad = ' ';
	while (width > 0)
	{
		count += ft_putchar_count(pad);
		width--;
	}
	return (count);
}
