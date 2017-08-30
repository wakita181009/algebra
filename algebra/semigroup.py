# -*- coding: utf-8 -*-

from typing import TypeVar
from abc import ABCMeta, abstractmethod

from .magma import Magma, AdditiveMagma

SemiGroupType = TypeVar("SemiGroupType")


class SemiGroup(Magma, metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self: SemiGroupType, x: SemiGroupType) -> bool:
        pass

    def test_associativity(self: SemiGroupType, a: SemiGroupType, b: SemiGroupType):
        assert (self * a) * b == self * (a * b)


class AdditiveSemiGroup(AdditiveMagma, metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self: SemiGroupType, x: SemiGroupType) -> bool:
        pass

    def test_additive_associativity(self: SemiGroupType, a: SemiGroupType, b: SemiGroupType):
        assert (self + a) + b == self + (a + b)
