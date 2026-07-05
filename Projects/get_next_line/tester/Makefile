# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/03 19:06:13 by dsilva-c          #+#    #+#              #
#    Updated: 2025/12/03 19:07:41 by dsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = tester
NAME_BONUS = tester_bonus
NAME_SMALL = tester_small
NAME_HUGE = tester_huge
NAME_CREATE = create_test_files
TEST_DIR = test_files

GNL_DIR = ..

SRCS = tester.c tester_print.c tester_print2.c tester_tests.c tester_tests2.c \
       tester_tests3.c
SRCS_BONUS = tester_bonus.c tester_bonus_print.c tester_bonus_print2.c \
             tester_bonus_tests.c tester_bonus_tests2.c tester_bonus_tests3.c \
             tester_bonus_tests4.c
SRCS_CREATE = create_test_files.c create_test_files2.c

GNL_SRCS = $(GNL_DIR)/get_next_line.c $(GNL_DIR)/get_next_line_utils.c
GNL_BONUS = $(GNL_DIR)/get_next_line_bonus.c \
            $(GNL_DIR)/get_next_line_utils_bonus.c

OBJS = $(SRCS:.c=.o)
OBJS_BONUS = $(SRCS_BONUS:.c=.o)
OBJS_CREATE = $(SRCS_CREATE:.c=.o)

CC = cc
BUFFER_SIZE = 42
CFLAGS = -Wall -Wextra -Werror -I$(GNL_DIR)

all: test

$(NAME): $(OBJS) $(GNL_SRCS)
	$(CC) $(CFLAGS) -D BUFFER_SIZE=$(BUFFER_SIZE) $(OBJS) $(GNL_SRCS) -o \
	$(NAME)

$(NAME_BONUS): $(OBJS_BONUS) $(GNL_BONUS)
	$(CC) $(CFLAGS) -D BUFFER_SIZE=$(BUFFER_SIZE) $(OBJS_BONUS) \
	$(GNL_BONUS) -o $(NAME_BONUS)

$(NAME_CREATE): $(OBJS_CREATE)
	$(CC) $(CFLAGS) $(OBJS_CREATE) -o $(NAME_CREATE)

$(TEST_DIR): $(NAME_CREATE)
	./$(NAME_CREATE)

%.o: %.c
	$(CC) $(CFLAGS) -D BUFFER_SIZE=$(BUFFER_SIZE) -c $< -o $@

test: $(NAME) $(TEST_DIR)
	./$(NAME)

test_stdin: $(NAME)
	@echo "Hello Stdin!" | ./$(NAME)

$(NAME_SMALL): $(OBJS) $(GNL_SRCS)
	$(CC) $(CFLAGS) -D BUFFER_SIZE=1 $(OBJS) $(GNL_SRCS) -o $(NAME_SMALL)

test_small: $(NAME_SMALL) $(TEST_DIR)
	./$(NAME_SMALL)

$(NAME_HUGE): $(OBJS) $(GNL_SRCS)
	$(CC) $(CFLAGS) -D BUFFER_SIZE=10000000 $(OBJS) $(GNL_SRCS) -o \
	$(NAME_HUGE)

test_huge: $(NAME_HUGE) $(TEST_DIR)
	./$(NAME_HUGE)

bonus: $(NAME_BONUS) $(TEST_DIR)
	./$(NAME_BONUS)

leaks: $(NAME) $(TEST_DIR)
	valgrind --leak-check=full --show-leak-kinds=all ./$(NAME)

leaks_bonus: $(NAME_BONUS) $(TEST_DIR)
	valgrind --leak-check=full --show-leak-kinds=all ./$(NAME_BONUS)

clean:
	rm -f $(OBJS) $(OBJS_BONUS) $(OBJS_CREATE)

fclean: clean
	rm -f $(NAME) $(NAME_BONUS) $(NAME_CREATE) $(NAME_SMALL) $(NAME_HUGE)
	rm -rf $(TEST_DIR)

re: fclean all

.PHONY: all test bonus leaks leaks_bonus clean fclean re test_stdin \
        test_small test_huge
