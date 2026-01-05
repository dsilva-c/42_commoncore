/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 18:32:53 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/12/03 18:32:57 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static char	*ft_extract_line(char *buffer)
{
	char	*line;
	int		i;

	i = 0;
	while (buffer[i] && buffer[i] != '\n')
		i++;
	if (buffer[i] == '\n')
		i++;
	line = malloc(sizeof(char) * (i + 1));
	if (!line)
		return (NULL);
	i = 0;
	while (buffer[i] && buffer[i] != '\n')
	{
		line[i] = buffer[i];
		i++;
	}
	if (buffer[i] == '\n')
		line[i++] = '\n';
	line[i] = '\0';
	return (line);
}

static char	*ft_update_buffer(char *buffer)
{
	char	*new_buf;
	int		i;
	int		j;

	i = 0;
	while (buffer[i] && buffer[i] != '\n')
		i++;
	if (!buffer[i])
	{
		free(buffer);
		return (NULL);
	}
	new_buf = malloc(sizeof(char) * (ft_strlen_bonus(buffer + i + 1) + 1));
	if (!new_buf)
		return (NULL);
	i++;
	j = 0;
	while (buffer[i])
		new_buf[j++] = buffer[i++];
	new_buf[j] = '\0';
	free(buffer);
	return (new_buf);
}

static char	*ft_read_file(int fd, char *buffer, char *buf)
{
	char	*temp;
	ssize_t	bytes;

	bytes = 1;
	while (bytes > 0)
	{
		bytes = read(fd, buf, BUFFER_SIZE);
		if (bytes == -1)
		{
			free(buffer);
			return (NULL);
		}
		if (bytes == 0)
			break ;
		buf[bytes] = '\0';
		temp = ft_strjoin_bonus(buffer, buf);
		free(buffer);
		buffer = temp;
		if (!buffer)
			return (NULL);
		if (ft_strchr_bonus(buffer, '\n'))
			break ;
	}
	return (buffer);
}

static char	*ft_process(char **buffer)
{
	char	*line;

	line = ft_extract_line(*buffer);
	if (!line)
	{
		free(*buffer);
		*buffer = NULL;
		return (NULL);
	}
	*buffer = ft_update_buffer(*buffer);
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*bufs[FD_MAX];
	char		*buf;

	if (fd < 0 || fd >= FD_MAX || BUFFER_SIZE <= 0)
		return (NULL);
	buf = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!buf)
		return (NULL);
	if (!bufs[fd])
	{
		bufs[fd] = malloc(sizeof(char) * 1);
		if (!bufs[fd])
			return (free(buf), NULL);
		bufs[fd][0] = '\0';
	}
	bufs[fd] = ft_read_file(fd, bufs[fd], buf);
	free(buf);
	if (!bufs[fd] || !bufs[fd][0])
	{
		free(bufs[fd]);
		bufs[fd] = NULL;
		return (NULL);
	}
	return (ft_process(&bufs[fd]));
}
