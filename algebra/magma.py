# -*- coding: utf-8 -*-

from typing import TypeVar
from abc import ABCMeta, abstractmethod

MagmaType = TypeVar("MagmaType")


class Magma(metaclass=ABCMeta):
    @abstractmethod
    def __mul__(self: MagmaType, x: MagmaType) -> MagmaType:
        pass


class AdditiveMagma(metaclass=ABCMeta):
    @abstractmethod
    def __add__(self: MagmaType, x: MagmaType) -> MagmaType:
        pass
