"""
Duncan Du
January, 2022
This class performs match making for LUX quarterly productions.
The greedy algorithm used in this program was developed by Rachel Kisela.
"""

from Candidate import Candidate


class MatchMaker:

    def __init__(self, productions: list):
        """
        Creates a new MatchMaker
        :param productions: a list of Productions that need to be filled
        """
        self.productions = productions

    def match(self, candidates: list):
        """
        Uses the following greedy algorithm to place Candidates into Productions:
            Sort candidates first by years in LUX, then by years at UW
            for each candidate in candidates:
                if candidate prioritizes production:
                    for each production in candidate's production preference list:
                        for each role in candidate's role preference list:
                            if production has role open:
                                Place candidate into production. (Done with this candidate)
                else:
                    for each role in candidate's role preference list:
                        for each production in candidate's production preference list:
                            if production has role open:
                                Place candidate into production. (Done with this candidate)

        :param candidates a list of Candidates
        :return: the list of production, but matched! and a list of Candidates who were not matched to productions
        """
        candidates = candidates.copy()
        candidates_left = candidates.copy()
        # sort candidates first by years in LUX then by years at UW, both in descending order
        sorted(candidates, key=lambda person: person.yr_at_uw, reverse=True)
        sorted(candidates, key=lambda person: person.yr_in_lux, reverse=True)

        for candidate in candidates:
            assigned = False
            if candidate.prod_first:
                for prod in candidate.prods:
                    for production in self.productions:
                        if production.name == prod:
                            for role in candidate.roles:
                                if production.place(candidate.name, role):
                                    assigned = True
                                    break
                            if assigned:
                                break
                    if assigned:
                        break
            else:
                for role in candidate.roles:
                    for prod in candidate.prods:
                        for production in self.productions:
                            if production.name == prod:
                                if production.place(candidate.name, role):
                                    assigned = True
                                    break
                        if assigned:
                            break
                    if assigned:
                        break

            if assigned:
                candidates_left.remove(candidate)

        return self.productions, candidates_left
