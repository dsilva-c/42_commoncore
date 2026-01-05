/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_number_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:17:57 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:18:08 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

static void	ft_putnbr_rec(long n)
{
	if (n >= 10)
		ft_putnbr_rec(n / 10);
	ft_putchar_count((n % 10) + '0');
}

static int	ft_print_sign(int n, t_flags flags)
{
	int	count;

	count = 0;
	if (n < 0)
		count += ft_putchar_count('-');
	else if (flags.plus)
		count += ft_putchar_count('+');
	else if (flags.space)
		count += ft_putchar_count(' ');
	return (count);
}

static void	ft_init_num_vars(int n, t_flags *flags, long *nb, int *numlen)
{
	if (flags->dot)
		flags->zero = 0;
	*nb = n;
	if (*nb < 0)
		*nb = -*nb;
	*numlen = ft_numlen(n);
	if (n == 0 && flags->dot && flags->precision == 0)
		*numlen = 0;
	if (n < 0)
		(*numlen)--;
}

static int	ft_get_total_width(int n, t_flags flags, int numlen)
{
	int	total;

	total = numlen;
	if (n < 0 || flags.plus || flags.space)
		total++;
	if (flags.dot && flags.precision > numlen)
		total = flags.precision + (n < 0 || flags.plus || flags.space);
	return (total);
}

int	ft_print_number_bonus(int n, t_flags flags)
{
	int		count;
	long	nb;
	int		numlen;
	int		total;

	ft_init_num_vars(n, &flags, &nb, &numlen);
	total = ft_get_total_width(n, flags, numlen);
	count = 0;
	if (!flags.minus && !flags.zero)
		count += ft_print_width(flags.width - total, 0);
	count += ft_print_sign(n, flags);
	if (!flags.minus && flags.zero)
		count += ft_print_width(flags.width - total, 1);
	if (flags.dot)
		count += ft_print_width(flags.precision - numlen, 1);
	if (numlen > 0)
		ft_putnbr_rec(nb);
	count += numlen;
	if (flags.minus)
		count += ft_print_width(flags.width - total, 0);
	return (count);
}
