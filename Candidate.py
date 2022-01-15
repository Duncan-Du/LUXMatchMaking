"""
This class represents a candidate applying for a role at a LUX production
"""


class Candidate:
    def __init__(self, name: str, yr_in_lux: int, yr_at_uw: int, prod_first: bool, prod_1: str,
                 prod_2: str, prod_3: str, role_1: str, role_2: str, role_3: str):
        self.name = name
        self.yr_in_lux = yr_in_lux
        self.yr_at_uw = yr_at_uw
        self.prod_first = prod_first
        self.prods = [prod_1, prod_2, prod_3]
        self.roles = [role_1, role_2, role_3]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
