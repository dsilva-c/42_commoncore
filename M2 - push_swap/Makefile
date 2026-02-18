# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 21:36:18 by dsilva-c          #+#    #+#              #
#    Updated: 2026/01/11 21:37:23 by dsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME		= push_swap
BONUS_NAME	= checker

CC			= cc
CFLAGS		= -Wall -Wextra -Werror

# Mandatory Files
SRC			= main.c \
			  handle_errors.c \
			  stack_init.c \
			  stack_utils.c \
			  push.c \
			  swap.c \
			  rotate.c \
			  rev_rotate.c \
			  sort_three.c \
			  sort_stacks.c \
			  init_a_to_b.c \
			  init_b_to_a.c \
			  ft_split.c \
			  ft_utils.c

# Bonus Files (Uses your GNL)
BONUS_SRC	= checker.c \
			  get_next_line.c \
			  get_next_line_utils.c \
			  handle_errors.c \
			  stack_init.c \
			  stack_utils.c \
			  push.c \
			  swap.c \
			  rotate.c \
			  rev_rotate.c \
			  ft_split.c \
			  ft_utils.c

OBJ			= $(SRC:.c=.o)
BONUS_OBJ	= $(BONUS_SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

bonus: $(BONUS_OBJ)
	$(CC) $(CFLAGS) $(BONUS_OBJ) -o $(BONUS_NAME)

clean:
	rm -f $(OBJ) $(BONUS_OBJ)

fclean: clean
	rm -f $(NAME) $(BONUS_NAME)

re: fclean all

.PHONY: all clean fclean re bonus
