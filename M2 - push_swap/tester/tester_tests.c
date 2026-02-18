/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_tests.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:25:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:25:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_identity(t_results *res)
{
	print_test_header("🔄 IDENTITY TESTS (already sorted)");
	printf(YELLOW "    > Cases where push_swap should do nothing\n" RESET);
	printf("\n");
	print_result(check_no_output("42"),
		"Single element (42) -> no output", res);
	print_result(check_no_output("1 2"),
		"Two sorted (1 2) -> no output", res);
	print_result(check_no_output("1 2 3"),
		"Three sorted (1 2 3) -> no output", res);
	print_result(check_no_output("1 2 3 4 5"),
		"Five sorted (1 2 3 4 5) -> no output", res);
}

void	test_small_sort(t_results *res)
{
	int	moves;

	print_test_header("📐 SMALL SORT TESTS");
	printf(YELLOW "    > Testing with 2, 3, and 5 elements\n" RESET);
	printf("\n");
	moves = get_move_count("2 1");
	print_result(moves == 1, "2 elems (2 1): 1 move expected", res);
	moves = get_move_count("3 2 1");
	print_result(moves <= 3, "3 elems (3 2 1): max 3 moves", res);
	moves = get_move_count("2 3 1");
	print_result(moves <= 3, "3 elems (2 3 1): max 3 moves", res);
	moves = get_move_count("1 3 2");
	print_result(moves <= 3, "3 elems (1 3 2): max 3 moves", res);
	moves = get_move_count("3 1 2");
	print_result(moves <= 3, "3 elems (3 1 2): max 3 moves", res);
	moves = get_move_count("2 1 3");
	print_result(moves <= 3, "3 elems (2 1 3): max 3 moves", res);
	moves = get_move_count("5 3 1 4 2");
	print_result(moves <= 12, "5 elems (5 3 1 4 2): max 12 moves", res);
	moves = get_move_count("1 5 2 4 3");
	print_result(moves <= 12, "5 elems (1 5 2 4 3): max 12 moves", res);
	moves = get_move_count("5 4 3 2 1");
	print_result(moves <= 12, "5 elems (5 4 3 2 1): max 12 moves", res);
}

void	test_error_handling(t_results *res)
{
	print_test_header("⚠️  ERROR HANDLING TESTS");
	printf(YELLOW "    > Cases that should produce Error or no output\n"
		RESET);
	printf("\n");
	print_result(check_no_output(""),
		"No arguments -> no output", res);
	print_result(check_no_output("\"\""),
		"Empty string -> no output", res);
	print_result(check_error("1 2 1"),
		"Duplicate (1 2 1) -> Error", res);
	print_result(check_error("1 abc 3"),
		"Non-numeric (1 abc 3) -> Error", res);
	print_result(check_error("2147483648"),
		"Overflow (2147483648) -> Error", res);
	print_result(check_error("-2147483649"),
		"Underflow (-2147483649) -> Error", res);
	print_result(check_error("+"),
		"Plus alone (+) -> Error", res);
	print_result(check_error("-"),
		"Minus alone (-) -> Error", res);
	print_result(check_error("1 2 3 a"),
		"Alpha at end (1 2 3 a) -> Error", res);
}
