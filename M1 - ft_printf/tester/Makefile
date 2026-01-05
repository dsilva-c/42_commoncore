# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/06 01:36:26 by dsilva-c          #+#    #+#              #
#    Updated: 2025/12/06 01:38:41 by dsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = tester
LIB_DIR = ..
LIB_NAME = libftprintf.a
LIB = $(LIB_DIR)/$(LIB_NAME)

SRCS = tester.c tester_print.c test_mandatory.c test_mandatory2.c \
       test_mandatory3.c test_bonus.c test_bonus2.c test_hardcore.c

OBJS = $(SRCS:.c=.o)

CC = cc
CFLAGS = -Wall -Wextra -Werror

all: $(NAME)

$(LIB):
	make -C $(LIB_DIR) bonus

$(NAME): $(OBJS) $(LIB)
	$(CC) $(CFLAGS) $(OBJS) -L$(LIB_DIR) -lftprintf -o $(NAME)

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

run: all
	./$(NAME)

leaks: $(NAME)
	valgrind --leak-check=full --show-leak-kinds=all ./$(NAME)

.PHONY: all clean fclean re run leaks
