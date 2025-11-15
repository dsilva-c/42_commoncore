/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_bonus_part2.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:49:44 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:49:46 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_lstsize(void)
{
	t_list	*node1;
	t_list	*node2;
	t_list	*head;
	int		size;

	print_function("ft_lstsize", "Get list size");
	node1 = ft_lstnew(ft_strdup("first"));
	node2 = ft_lstnew(ft_strdup("second"));
	head = NULL;
	ft_lstadd_front(&head, node2);
	ft_lstadd_front(&head, node1);
	size = ft_lstsize(head);
	print_test("Size of list with 2 nodes");
	print_output("size = 2");
	test_result(size == 2, "size correct");
	ft_lstclear(&head, del_list_content);
}

void	test_lstlast(void)
{
	t_list	*node1;
	t_list	*node2;
	t_list	*head;

	print_function("ft_lstlast", "Get last node");
	node1 = ft_lstnew(ft_strdup("first"));
	node2 = ft_lstnew(ft_strdup("second"));
	head = NULL;
	ft_lstadd_front(&head, node2);
	ft_lstadd_front(&head, node1);
	print_test("Find last node");
	print_output("last node found");
	test_result(ft_lstlast(head) != NULL, "last node exists");
	ft_lstclear(&head, del_list_content);
}

void	test_lstadd_back(void)
{
	t_list	*node;
	t_list	*head;
	char	*content;

	print_function("ft_lstadd_back", "Add node to back");
	head = NULL;
	content = ft_strdup("new");
	node = ft_lstnew(content);
	ft_lstadd_back(&head, node);
	print_test("Add node to back");
	print_output("node added at end");
	test_result(ft_lstlast(head) == node, "added to back");
	ft_lstclear(&head, del_list_content);
}

void	test_lstiter(void)
{
	t_list	*head;
	char	*content;

	print_function("ft_lstiter", "Iterate through list");
	head = NULL;
	content = ft_strdup("test");
	ft_lstadd_back(&head, ft_lstnew(content));
	print_test("Iterate and apply function");
	printf("      Output:\n");
	ft_lstiter(head, print_list_node);
	test_result(1, "executed");
	ft_lstclear(&head, del_list_content);
}

void	helper_bonus_part2(void)
{
	test_lstsize();
	printf("\n");
	test_lstlast();
	printf("\n");
	test_lstadd_back();
	printf("\n");
	test_lstiter();
}
