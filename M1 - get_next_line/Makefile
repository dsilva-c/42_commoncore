# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/03 18:29:50 by dsilva-c          #+#    #+#              #
#    Updated: 2025/12/03 18:30:41 by dsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = get_next_line.a

HEADER = get_next_line.h
HEADER_BONUS = get_next_line_bonus.h

SRCS_MANDATORY = get_next_line.c get_next_line_utils.c
SRCS_BONUS = get_next_line_bonus.c get_next_line_utils_bonus.c

OBJS_MANDATORY = $(SRCS_MANDATORY:.c=.o)
OBJS_BONUS = $(SRCS_BONUS:.c=.o)

CC = cc
CFLAGS = -Wall -Wextra -Werror -I.

all: $(NAME)

$(NAME): $(OBJS_MANDATORY)
	ar rc $(NAME) $(OBJS_MANDATORY)
	ranlib $(NAME)

bonus: .bonus

.bonus: $(OBJS_BONUS)
	ar rc $(NAME) $(OBJS_BONUS)
	ranlib $(NAME)
	touch .bonus

get_next_line.o: get_next_line.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

get_next_line_utils.o: get_next_line_utils.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

get_next_line_bonus.o: get_next_line_bonus.c $(HEADER_BONUS)
	$(CC) $(CFLAGS) -c $< -o $@

get_next_line_utils_bonus.o: get_next_line_utils_bonus.c $(HEADER_BONUS)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS_MANDATORY) $(OBJS_BONUS) .bonus

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re
