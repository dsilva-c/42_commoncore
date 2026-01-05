/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_char_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:15:23 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:15:37 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

int	ft_print_char_bonus(char c, t_flags flags)
{
	int	count;

	count = 0;
	if (flags.minus)
	{
		count += ft_putchar_count(c);
		count += ft_print_width(flags.width - 1, 0);
	}
	else
	{
		count += ft_print_width(flags.width - 1, flags.zero);
		count += ft_putchar_count(c);
	}
	return (count);
}

int	ft_print_percent_bonus(t_flags flags)
{
	return (ft_print_char_bonus('%', flags));
}
