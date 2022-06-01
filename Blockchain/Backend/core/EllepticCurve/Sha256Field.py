""" 
Copyright (c) 2021 Codiesalert.com
These scripts should be used for commercial purpose without Codies Alert Permission
Any violations may lead to legal action
"""
from FieldElement import FieldElement
from Point import Point

P = 2 ** 256 - 2 ** 32 - 977


class Sha256Field(FieldElement):
    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=P)

    def __repr__(self):
        return "{:x}".format(self.num).zfill(64)
