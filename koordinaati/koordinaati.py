# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Coordinates API."""
import os
import sys
from enum import Enum
from typing import List, Union


DEBUG_VAR = 'KOORDINAATI_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


class Dimension(Enum):
    LAT = auto()
    LON = auto()
    ALT = auto()


class Unit(Enum):
    DEGREE = auto()
    RADIAN= auto()
    METER = auto()
    FEET = auto()


class Koordinaati:
    """Coordinate representations require handling.
    
    Internal representation is per float.
    """
    def __init__(self, dimension: Dimension, value: Union[int, float, str], unit: Unit):
        self.sexagesimal = None
        self.decimal = None
        self.na = True
        self.dimension = dimension
        self.value = value
        self.unit = unit
        self.unit_label = labelUnit(self)
        self.what = labelDimension(self)
    
    def labelDimension(self):
        """Delegate labeling to enumeration."""
        return self.dimension.name

    def labelUnit(self):
        """Delegate labeling to enumeration."""
        return self.unit.name


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the coordination."""
    argv = argv if argv else sys.argv[1:]
    if not argv:
        print('ERROR arguments expected.', file=sys.stderr)
        return 2
    
    return 0
