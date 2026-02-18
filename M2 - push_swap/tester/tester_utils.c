/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_utils.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:20:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:20:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

int	get_move_count(const char *args)
{
	char	cmd[16384];
	char	buf[256];
	int		count;
	FILE	*fp;

	snprintf(cmd, sizeof(cmd), "../push_swap %s 2>/dev/null", args);
	fp = popen(cmd, "r");
	if (!fp)
		return (-1);
	count = 0;
	while (fgets(buf, sizeof(buf), fp))
		count++;
	pclose(fp);
	return (count);
}

int	verify_sort(const char *args)
{
	char	cmd[32768];
	char	buf[256];
	FILE	*fp;

	snprintf(cmd, sizeof(cmd),
		"../push_swap %s | ../checker %s", args, args);
	fp = popen(cmd, "r");
	if (!fp)
		return (0);
	buf[0] = '\0';
	if (!fgets(buf, sizeof(buf), fp))
	{
		pclose(fp);
		return (0);
	}
	pclose(fp);
	return (strncmp(buf, "OK", 2) == 0);
}

int	check_error(const char *args)
{
	char	cmd[16384];
	char	buf[256];
	FILE	*fp;

	snprintf(cmd, sizeof(cmd), "../push_swap %s 2>&1", args);
	fp = popen(cmd, "r");
	if (!fp)
		return (0);
	buf[0] = '\0';
	if (!fgets(buf, sizeof(buf), fp))
	{
		pclose(fp);
		return (0);
	}
	pclose(fp);
	return (strncmp(buf, "Error", 5) == 0);
}

int	check_no_output(const char *args)
{
	char	cmd[16384];
	char	buf[256];
	FILE	*fp;
	int		got_output;

	snprintf(cmd, sizeof(cmd), "../push_swap %s 2>&1", args);
	fp = popen(cmd, "r");
	if (!fp)
		return (0);
	got_output = (fgets(buf, sizeof(buf), fp) != NULL);
	pclose(fp);
	return (!got_output);
}

void	gen_random_args(char *buf, int buf_size, int count)
{
	int	*arr;
	int	i;
	int	j;
	int	tmp;
	int	offset;

	arr = malloc(sizeof(int) * count);
	if (!arr)
		return ;
	i = -1;
	while (++i < count)
		arr[i] = i + 1;
	i = count;
	while (--i > 0)
	{
		j = rand() % (i + 1);
		tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
	offset = 0;
	i = -1;
	while (++i < count && offset < buf_size - 16)
	{
		if (i > 0)
			offset += snprintf(buf + offset, buf_size - offset, " ");
		offset += snprintf(buf + offset, buf_size - offset, "%d", arr[i]);
	}
	free(arr);
}
