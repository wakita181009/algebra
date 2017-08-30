# -*- coding: utf-8 -*-

from typing import TypeVar
from abc import ABCMeta, abstractmethod

from .monoid import Monoid, AdditiveMonoid

GroupType = TypeVar("GroupType")


class Group(Monoid, metaclass=ABCMeta):
    @abstractmethod
    def inverse(self: GroupType) -> GroupType:
        pass

    def __truediv__(self: GroupType, x: GroupType) -> GroupType:
        return self * x.inverse()

    def test_inverse(self: GroupType):
        assert self * self.inverse() == self.identity()


class AdditiveGroup(AdditiveMonoid, metaclass=ABCMeta):
    @abstractmethod
    def zero(self: GroupType) -> GroupType:
        pass

    @abstractmethod
    def __neg__(self: GroupType) -> GroupType:
        pass

    def __sub__(self: GroupType, x: GroupType) -> GroupType:
        return self + (-x)

    def test_zero(self: GroupType):
        assert self + self.zero() == self

    def test_negative(self: GroupType):
        assert self + (-self) == self.zero()

    def test_abelian(self: GroupType, x: GroupType):
        assert self + x == x + self
