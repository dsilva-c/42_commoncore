/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tester_bonus.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 14:35:00 by dsilva-c          #+#    #+#             */
/*   Updated: 2026/02/18 14:35:05 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

static int	checker_result(const char *cmd_str)
{
	char	buf[256];
	FILE	*fp;

	fp = popen(cmd_str, "r");
	if (!fp)
		return (-1);
	buf[0] = '\0';
	if (!fgets(buf, sizeof(buf), fp))
	{
		pclose(fp);
		return (-1);
	}
	pclose(fp);
	if (strncmp(buf, "OK", 2) == 0)
		return (1);
	if (strncmp(buf, "KO", 2) == 0)
		return (0);
	if (strncmp(buf, "Error", 5) == 0)
		return (2);
	return (-1);
}

static void	test_checker_basic(t_results *res)
{
	int	r;

	r = checker_result("../push_swap 3 2 1 | ../checker 3 2 1");
	print_result(r == 1,
		"Checker: correct sort (3 2 1) -> OK", res);
	r = checker_result("../push_swap 5 3 1 4 2 | ../checker 5 3 1 4 2");
	print_result(r == 1,
		"Checker: correct sort (5 3 1 4 2) -> OK", res);
	r = checker_result("printf '' | ../checker 1 2 3");
	print_result(r == 1,
		"Checker: sorted + no ops -> OK", res);
}

static void	test_checker_ko_error(t_results *res)
{
	int	r;

	r = checker_result("echo 'pb' | ../checker 3 2 1 2>&1");
	print_result(r == 0,
		"Checker: wrong ops (pb on 3 2 1) -> KO", res);
	r = checker_result("echo 'sa' | ../checker 1 2 3 2>&1");
	print_result(r == 0,
		"Checker: unnecessary swap on sorted -> KO", res);
	r = checker_result("echo 'invalid' | ../checker 2 1 2>&1");
	print_result(r == 2,
		"Checker: invalid command -> Error", res);
	r = checker_result("echo 'sa' | ../checker 1 a 2>&1");
	print_result(r == 2,
		"Checker: non-numeric input -> Error", res);
}

void	test_bonus_checker(t_results *res)
{
	int	r;

	print_test_header("🎯 BONUS - CHECKER TESTS");
	printf(YELLOW "    > Testing the checker program\n" RESET);
	printf("\n");
	test_checker_basic(res);
	test_checker_ko_error(res);
	r = checker_result(
			"../push_swap \"5 3 1 4 2\" | ../checker \"5 3 1 4 2\"");
	print_result(r == 1,
		"Checker: string arg (\"5 3 1 4 2\") -> OK", res);
}
