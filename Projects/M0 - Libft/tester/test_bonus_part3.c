/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_bonus_part3.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dsilva-c <dsilva-c@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 17:52:59 by dsilva-c          #+#    #+#             */
/*   Updated: 2025/10/31 17:53:03 by dsilva-c         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "tester.h"

void	test_lstdelone(void)
{
	t_list	*node;
	char	*content;

	print_function("ft_lstdelone", "Delete single node");
	print_memory_check("ft_lstdelone");
	content = ft_strdup("test");
	node = ft_lstnew(content);
	ft_lstdelone(node, del_list_content);
	print_test("Delete node");
	print_output("node deleted");
	test_result(1, "executed");
}

void	test_lstmap(void)
{
	t_list	*head;
	t_list	*mapped;
	int		size;
	char	*content;

	print_function("ft_lstmap", "Transform list");
	print_memory_check("ft_lstmap");
	head = NULL;
	content = ft_strdup("test");
	ft_lstadd_back(&head, ft_lstnew(content));
	mapped = ft_lstmap(head, dup_list_content, del_list_content);
	size = ft_lstsize(mapped);
	print_test("Transform list with map");
	print_output("new list created");
	test_result(mapped != NULL && size == 1, "mapped correctly");
	ft_lstclear(&mapped, del_list_content);
	ft_lstclear(&head, del_list_content);
}

void	test_lstclear(void)
{
	t_list	*head;
	char	*content;

	print_function("ft_lstclear", "Clear entire list");
	print_memory_check("ft_lstclear");
	head = NULL;
	content = ft_strdup("test");
	ft_lstadd_back(&head, ft_lstnew(content));
	ft_lstclear(&head, del_list_content);
	print_test("Clear list");
	print_output("all nodes freed");
	test_result(head == NULL, "list cleared");
}

void	test_bonus_functions(void)
{
	print_title("PART 8: BONUS - LINKED LIST");
	test_lstnew_lstadd_front();
	printf("\n");
	helper_bonus_part2();
	printf("\n");
	test_lstdelone();
	printf("\n");
	test_lstmap();
	printf("\n");
	test_lstclear();
}
