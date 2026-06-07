#!/usr/bin/python3
"""Standart int klassından miras alan MyInt klassını təyin edən modul."""


class MyInt(int):
    """int klassının == və != operatorlarını tərsinə işlədən asi klass."""

    def __eq__(self, other):
        """== operatorunun davranışını tərsinə çevirir (bərabərsə False)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """!= operatorunun davranışını tərsinə çevirir (bərabərsə True)."""
        return super().__eq__(other)
