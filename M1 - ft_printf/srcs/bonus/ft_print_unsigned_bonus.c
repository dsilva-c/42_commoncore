/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_unsigned_bonus.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:18:54 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:19:01 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

static void	ft_putunsigned_rec(unsigned int n)
{
	if (n >= 10)
		ft_putunsigned_rec(n / 10);
	ft_putchar_count((n % 10) + '0');
}

static int	ft_unsigned_len(unsigned int n)
{
	int	len;

	len = 0;
	if (n == 0)
		return (1);
	while (n != 0)
	{
		n /= 10;
		len++;
	}
	return (len);
}

int	ft_print_unsigned_bonus(unsigned int n, t_flags flags)
{
	int	count;
	int	numlen;
	int	total;

	if (flags.dot)
		flags.zero = 0;
	count = 0;
	numlen = ft_unsigned_len(n);
	if (n == 0 && flags.dot && flags.precision == 0)
		numlen = 0;
	total = numlen;
	if (flags.dot && flags.precision > numlen)
		total = flags.precision;
	if (!flags.minus && !flags.zero)
		count += ft_print_width(flags.width - total, 0);
	if (!flags.minus && flags.zero)
		count += ft_print_width(flags.width - total, 1);
	if (flags.dot)
		count += ft_print_width(flags.precision - numlen, 1);
	if (numlen > 0)
		ft_putunsigned_rec(n);
	count += numlen;
	if (flags.minus)
		count += ft_print_width(flags.width - total, 0);
	return (count);
}
