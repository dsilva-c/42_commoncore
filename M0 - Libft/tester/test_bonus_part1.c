/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_bonus_part1.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:49:19 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:49:21 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	print_list_node(void *content)
{
	printf("      -> \"%s\"\n", (char *)content);
}

void	del_list_content(void *content)
{
	free(content);
}

void	*dup_list_content(void *content)
{
	return (ft_strdup((char *)content));
}

void	test_lstnew_lstadd_front(void)
{
	t_list	*node;
	t_list	*head;
	char	*content;

	print_function("ft_lstnew", "Create new list node");
	print_memory_check("ft_lstnew");
	content = ft_strdup("test");
	node = ft_lstnew(content);
	print_test("ft_lstnew(\"test\")");
	print_output("Node created with content");
	test_result(node != NULL, "node created");
	printf("\n");
	print_function("ft_lstadd_front", "Add node to front");
	head = NULL;
	ft_lstadd_front(&head, node);
	print_test("Add node to front");
	print_output("head now points to node");
	test_result(head == node, "added to front");
	free(content);
	free(node);
}

void	helper_bonus_part1(void)
{
	test_lstnew_lstadd_front();
}
