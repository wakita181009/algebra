# -*- coding: utf-8 -*-


from typing import TypeVar
from abc import ABCMeta

from .group import Group, AdditiveGroup

RingType = TypeVar("RingType")


class Ring(Group, AdditiveGroup, metaclass=ABCMeta):
    def test_distributive(self: RingType, x: RingType, y: RingType) -> bool:
        return self * (x + y) == self * x + self * y
