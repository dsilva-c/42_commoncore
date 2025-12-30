# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/21 03:01:36 by dsilva-c          #+#    #+#              #
#    Updated: 2025/11/21 03:04:58 by dsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs

LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a
INCLUDES = -I./includes -I$(LIBFT_DIR)
SRC_DIR = srcs
MANDATORY_DIR = $(SRC_DIR)/mandatory
BONUS_DIR = $(SRC_DIR)/bonus

MANDATORY_SRC = $(MANDATORY_DIR)/ft_printf.c \
                $(MANDATORY_DIR)/ft_putchar.c \
                $(MANDATORY_DIR)/ft_putstr.c \
                $(MANDATORY_DIR)/ft_putnbr.c \
                $(MANDATORY_DIR)/ft_putnbr_unsigned.c \
                $(MANDATORY_DIR)/ft_puthex.c \
                $(MANDATORY_DIR)/ft_putptr.c \
                $(MANDATORY_DIR)/ft_print_char.c \
                $(MANDATORY_DIR)/ft_print_string.c \
                $(MANDATORY_DIR)/ft_print_number.c \
                $(MANDATORY_DIR)/ft_print_unsigned.c \
                $(MANDATORY_DIR)/ft_print_hex.c \
                $(MANDATORY_DIR)/ft_print_pointer.c

BONUS_SRC = $(BONUS_DIR)/ft_printf_bonus.c \
            $(BONUS_DIR)/ft_parse_bonus.c \
            $(BONUS_DIR)/ft_print_char_bonus.c \
            $(BONUS_DIR)/ft_print_string_bonus.c \
            $(BONUS_DIR)/ft_print_number_bonus.c \
            $(BONUS_DIR)/ft_print_unsigned_bonus.c \
            $(BONUS_DIR)/ft_print_hex_bonus.c \
            $(BONUS_DIR)/ft_print_pointer_bonus.c \
            $(BONUS_DIR)/ft_utils_bonus.c \
            $(BONUS_DIR)/ft_utils_bonus2.c

MANDATORY_OBJ = $(MANDATORY_SRC:.c=.o)
BONUS_OBJ = $(BONUS_SRC:.c=.o)

BONUS_CACHE = .bonus

all: $(LIBFT) $(NAME)

$(LIBFT):
	make -C $(LIBFT_DIR) bonus

$(NAME): $(LIBFT) $(MANDATORY_OBJ)
	cp $(LIBFT) $(NAME)
	$(AR) $(NAME) $(MANDATORY_OBJ)

bonus: $(LIBFT) $(BONUS_CACHE)

$(BONUS_CACHE): $(BONUS_OBJ)
	cp $(LIBFT) $(NAME)
	$(AR) $(NAME) $(BONUS_OBJ)
	touch $(BONUS_CACHE)

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(MANDATORY_OBJ) $(BONUS_OBJ) $(BONUS_CACHE)
	make -C $(LIBFT_DIR) clean

fclean: clean
	rm -f $(NAME)
	make -C $(LIBFT_DIR) fclean

re: fclean all

.PHONY: all bonus clean fclean re
