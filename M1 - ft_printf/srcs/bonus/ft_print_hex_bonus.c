/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hex_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:19:29 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:19:41 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

static void	ft_puthex_rec(unsigned int n, char spec)
{
	char	*base;

	if (spec == 'x')
		base = "0123456789abcdef";
	else
		base = "0123456789ABCDEF";
	if (n >= 16)
		ft_puthex_rec(n / 16, spec);
	ft_putchar_count(base[n % 16]);
}

static int	ft_print_hex_prefix(char spec, t_flags flags, unsigned int n)
{
	int	count;

	count = 0;
	if (flags.hash && n != 0)
	{
		if (spec == 'x')
			count += ft_putstr_count("0x");
		else
			count += ft_putstr_count("0X");
	}
	return (count);
}

static void	ft_init_hex_vars(unsigned int n, t_flags *flags,
	int *hexlen, int *prefix_len)
{
	if (flags->dot)
		flags->zero = 0;
	*hexlen = ft_hexlen(n);
	if (n == 0 && flags->dot && flags->precision == 0)
		*hexlen = 0;
	*prefix_len = 0;
	if (flags->hash && n != 0)
		*prefix_len = 2;
}

int	ft_print_hex_bonus(unsigned int n, char spec, t_flags flags)
{
	int	count;
	int	hexlen;
	int	total;
	int	prefix_len;

	ft_init_hex_vars(n, &flags, &hexlen, &prefix_len);
	total = hexlen + prefix_len;
	if (flags.dot && flags.precision > hexlen)
		total = flags.precision + prefix_len;
	count = 0;
	if (!flags.minus && !flags.zero)
		count += ft_print_width(flags.width - total, 0);
	count += ft_print_hex_prefix(spec, flags, n);
	if (!flags.minus && flags.zero)
		count += ft_print_width(flags.width - total, 1);
	if (flags.dot)
		count += ft_print_width(flags.precision - hexlen, 1);
	if (hexlen > 0)
		ft_puthex_rec(n, spec);
	count += hexlen;
	if (flags.minus)
		count += ft_print_width(flags.width - total, 0);
	return (count);
}
