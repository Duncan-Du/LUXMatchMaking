import pandas as pd
import os
import numpy as np

from Candidate import Candidate
from MatchMaker import MatchMaker
from Production import Production

NAME_QUESTION = "What is your name? (first and last)"
YR_IN_LUX_QUESTION = "How many years have you been in LUX Film Production Club, including this year? (for example, " \
                     "a freshman new to LUX would enter \"1\")"
YR_AT_UW_QUESTION = "How many years have you been a student at UW, including this year? (for example, a sophomore " \
                    "would enter \"2\")"
ACTING_QUESTION = "Are you interested in acting (and not being on a production crew)?"
PROD_1_QUESTION = "First choice in production:"
PROD_2_QUESTION = "Second choice in production:"
PROD_3_QUESTION = "Third choice in production:"
ROLE_1_QUESTION = "First choice in role:"
ROLE_2_QUESTION = "Second choice in role:"
ROLE_3_QUESTION = "Third choice in role:"
PRIORITY_QUESTION = "Would you rather have your preferred ROLE or your preferred PRODUCTION?"

RESPONSE_PATH = "LUX Role Survey 22WI (Responses) - Form Responses 1.csv"
PRODUCTION_FORM_DIR = "Production Definition Forms"

if __name__ == '__main__':

    productions = []
    for pdf in os.listdir(PRODUCTION_FORM_DIR):
        if pdf.endswith(".csv"):
            production_name = pdf[0: -len(".csv")]
            production_df = pd.read_csv(PRODUCTION_FORM_DIR + "/" + pdf, header=None)
            roles = production_df[0].values.tolist()
            values = production_df[1].values.tolist()
            for i in range(len(values)):
                if not isinstance(values[i], str):
                    values[i] = None
            production = Production(production_name, roles, values)
            productions.append(production)
    print(productions)

    response_df = pd.read_csv(RESPONSE_PATH, header=0)
    candidates = []
    for i in range(len(response_df)):
        if response_df[ACTING_QUESTION][i] == "No":
            if response_df[PRIORITY_QUESTION][i] == "Production":
                prod_first = True
            else:
                prod_first = False
            candidate = Candidate(response_df[NAME_QUESTION][i],
                                  response_df[YR_IN_LUX_QUESTION][i],
                                  response_df[YR_AT_UW_QUESTION][i],
                                  prod_first,
                                  response_df[PROD_1_QUESTION][i],
                                  response_df[PROD_2_QUESTION][i],
                                  response_df[PROD_3_QUESTION][i],
                                  response_df[ROLE_1_QUESTION][i],
                                  response_df[ROLE_2_QUESTION][i],
                                  response_df[ROLE_3_QUESTION][i])
            candidates.append(candidate)

    match_maker = MatchMaker(productions)
    assigned_productions, unassigned_people = match_maker.match(candidates)
    print(assigned_productions)
    print(unassigned_people)

    for production in assigned_productions:
        production.to_csv()

    for person in unassigned_people:
        print(person.name)
