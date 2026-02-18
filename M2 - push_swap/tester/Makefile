# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 14:40:00 by dsilva-c          #+#    #+#              #
#    Updated: 2026/02/18 14:40:05 by dsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME		= tester
PS_DIR		= ..

SRC			= tester.c \
			  tester_print.c \
			  tester_print2.c \
			  tester_utils.c \
			  tester_tests.c \
			  tester_tests2.c \
			  tester_bonus.c

OBJ			= $(SRC:.c=.o)

CC			= cc
CFLAGS		= -Wall -Wextra -Werror

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

%.o: %.c tester.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

build-ps:
	$(MAKE) -C $(PS_DIR)
	$(MAKE) -C $(PS_DIR) bonus

run: build-ps all
	./$(NAME)

leaks: build-ps all
	valgrind --leak-check=full --show-leak-kinds=all \
		../push_swap 5 3 1 4 2 2>&1 | head -20
	@echo ""
	valgrind --leak-check=full --show-leak-kinds=all \
		../push_swap "5 3 1 4 2" 2>&1 | head -20

.PHONY: all clean fclean re run build-ps leaks
