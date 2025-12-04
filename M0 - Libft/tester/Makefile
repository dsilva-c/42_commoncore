# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/31 18:05:54 by dsilva-c          #+#    #+#              #
#    Updated: 2025/10/31 18:05:56 by dsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = tester

SRC = test_main.c tester_utils_part1.c tester_utils_part2.c \
      tester_utils_part3.c tester_utils_part4.c test_character_part1.c \
      test_character_part2.c test_string_part1.c test_string_part2.c \
      test_memory_part1.c test_memory_part2.c test_memory_part3.c test_copy.c \
      test_allocation.c test_additional_part1.c test_additional_part2.c \
      test_additional_functions.c test_output_part1.c test_output_part2.c \
      test_bonus_part1.c test_bonus_part2.c test_bonus_part3.c

OBJ = $(SRC:.c=.o)

LIBFT_DIR = ../
LIBFT = $(LIBFT_DIR)libft.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
LFLAGS = -L$(LIBFT_DIR) -lft

VALGRIND ?= valgrind
VGFLAGS ?= --leak-check=full --show-leak-kinds=all --track-origins=yes
VG_ERROR_EXITCODE ?= --error-exitcode=1

DBG_CFLAGS = -g -O0

all: $(NAME)

$(LIBFT):
	$(MAKE) -C $(LIBFT_DIR) bonus

$(NAME): $(OBJ) $(LIBFT)
	$(CC) $(CFLAGS) $(OBJ) $(LFLAGS) -o $(NAME)

%.o: %.c tester.h
	$(CC) $(CFLAGS) -I$(LIBFT_DIR) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME) valgrind.log

re: fclean all

run: all
	./$(NAME)

valgrind-log: all
	$(VALGRIND) $(VGFLAGS) ./$(NAME) 2>&1 | tee valgrind.log

valgrind-check: clean
	$(MAKE) CFLAGS="$(CFLAGS) $(DBG_CFLAGS)" all
	$(VALGRIND) $(VGFLAGS) $(VG_ERROR_EXITCODE) ./$(NAME) 2>&1 | tee valgrind.log

valgrind-check-rebuild: valgrind-check
	$(MAKE) CFLAGS="$(CFLAGS)" all

.PHONY: all clean fclean re run valgrind-log valgrind-check valgrind-check-rebuild
