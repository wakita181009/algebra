# -*- coding: utf-8 -*-

from typing import TypeVar
from abc import ABCMeta, abstractmethod

from .semigroup import SemiGroup, AdditiveSemiGroup

MonoidType = TypeVar("MonoidType")


class Monoid(SemiGroup, metaclass=ABCMeta):
    @abstractmethod
    def identity(self: MonoidType) -> MonoidType:
        pass

    def test_identity(self: MonoidType):
        assert self * self.identity() == self


class AdditiveMonoid(AdditiveSemiGroup, metaclass=ABCMeta):
    @abstractmethod
    def zero(self: MonoidType) -> MonoidType:
        pass

    def test_zero(self: MonoidType):
        assert self + self.zero() == self
