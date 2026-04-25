#!/usr/bin/python3
"""Singly Linked List üçün modul."""


class Node:
    """Bağlı siyahının bir düyününü (node) təyin edir."""

    def __init__(self, data, next_node=None):
        """Düyünü inisializasiya edir."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data dəyərini oxuyur."""
        return self.__data

    @data.setter
    def data(self, value):
        """Data dəyərini təyin edir (yalnız integer)."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Növbəti düyünü oxuyur."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Növbəti düyünü təyin edir (Node və ya None)."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List strukturunu təyin edir."""

    def __init__(self):
        """Boş siyahı yaradır."""
        self.__head = None

    def __str__(self):
        """Siyahını çap üçün string formatına salır."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Yeni düyünü artan sıra ilə düzgün mövqeyə yerləşdirir."""
        new_node = Node(value)

        # Case 1: Siyahı boşdur və ya yeni dəyər başlanğıcdan kiçikdir
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Siyahının ortasında və ya sonunda uyğun yer tapmaq
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
