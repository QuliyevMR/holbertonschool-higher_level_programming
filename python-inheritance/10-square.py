#!/usr/bin/python3
"""Rectangle-dan miras alan Square klassını təyin edən modul."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle əsasında kvadratı təmsil edən klass."""

    def __init__(self, size):
        """Square klassının init metodu.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        # Öncə size dəyərinin integer və müsbət olduğunu yoxlayırıq
        self.integer_validator("size", size)

        # Valideyn klassın (Rectangle) init metodunu en və hündürlük bərabər olacaq şəkildə çağırırıq
        super().__init__(size, size)

        # Şərtə əsasən private atributu mənimsədirik
        self.__size = size
