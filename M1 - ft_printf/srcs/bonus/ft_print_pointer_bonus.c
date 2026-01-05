/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_pointer_bonus.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:20:14 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:45:54 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

static void	ft_putptr_rec(unsigned long n)
{
	char	*base;

	base = "0123456789abcdef";
	if (n >= 16)
		ft_putptr_rec(n / 16);
	ft_putchar_count(base[n % 16]);
}

static int	ft_print_null_ptr(t_flags flags)
{
	int	count;

	count = 0;
	if (flags.minus)
	{
		count += ft_putstr_count("(nil)");
		count += ft_print_width(flags.width - 5, 0);
	}
	else
	{
		count += ft_print_width(flags.width - 5, 0);
		count += ft_putstr_count("(nil)");
	}
	return (count);
}

static int	ft_print_valid_ptr(unsigned long addr, t_flags flags)
{
	int	count;
	int	total;

	count = 0;
	total = ft_hexlen(addr) + 2;
	if (!flags.minus)
		count += ft_print_width(flags.width - total, 0);
	count += ft_putstr_count("0x");
	ft_putptr_rec(addr);
	count += ft_hexlen(addr);
	if (flags.minus)
		count += ft_print_width(flags. width - total, 0);
	return (count);
}

int	ft_print_pointer_bonus(void *ptr, t_flags flags)
{
	if (!ptr)
		return (ft_print_null_ptr(flags));
	return (ft_print_valid_ptr((unsigned long)ptr, flags));
}
