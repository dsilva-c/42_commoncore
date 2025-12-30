/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:07:16 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/11/28 13:08:18 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/ft_printf_bonus.h"

int	ft_handle_conversion(char spec, va_list args, t_flags flags)
{
	int	count;

	count = 0;
	if (spec == 'c')
	{
		flags.zero = 0;
		count += ft_print_char_bonus(va_arg(args, int), flags);
	}
	else if (spec == 's')
		count += ft_print_string_bonus(va_arg(args, char *), flags);
	else if (spec == 'p')
		count += ft_print_pointer_bonus(va_arg(args, void *), flags);
	else if (spec == 'd' || spec == 'i')
		count += ft_print_number_bonus(va_arg(args, int), flags);
	else if (spec == 'u')
		count += ft_print_unsigned_bonus(va_arg(args, unsigned int), flags);
	else if (spec == 'x' || spec == 'X')
		count += ft_print_hex_bonus(va_arg(args, unsigned int), spec, flags);
	else if (spec == '%')
		count += ft_print_percent_bonus(flags);
	return (count);
}

static int	ft_process_string(const char *format, va_list args)
{
	t_flags	flags;
	int		count;
	int		i;

	count = 0;
	i = 0;
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			ft_parse_flags(format, &i, &flags);
			if (!format[i])
			{
				count += ft_putchar_count('%');
				break ;
			}
			count += ft_handle_conversion(format[i], args, flags);
		}
		else
			count += ft_putchar_count(format[i]);
		i++;
	}
	return (count);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;

	if (!format)
		return (-1);
	va_start(args, format);
	count = ft_process_string(format, args);
	va_end(args);
	return (count);
}
