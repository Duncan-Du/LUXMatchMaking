"""
Duncan Du
January, 2022
This class defines a quarterly production at LUX
"""
import csv


class Production:

    def __init__(self, name: str, roles: list, assignments: list):
        """
        Creats a new Production
        :param name: the name of the production
        :param roles: a list of roles that need to be filled. Duplicates are allowed if a
                      production needs multiple people for a certain role
        :param assignments: a list of crew assignments. assignments[i] is assigned to role
                            roles[i]. assignments[i] is None if roles[i] need to be filled.
        """
        assert len(roles) == len(assignments)
        crew_size = len(roles)
        crew = []
        for i in range(crew_size):
            role = roles[i]
            if assignments[i] is None:
                # role need to be assigned
                crew.append([role, None])
            else:
                # role is predetermined
                crew.append([role, assignments[i]])
        self.crew = crew
        self.name = name

    def place(self, person, intended_role) -> bool:
        """
        Attempts to place person into the production as their intended role.
        :param person: the name of the person to be placed.
        :param intended_role: the role to be placed.
        :return: True if this Production has an intended_role that is not placed; False if
                 intended_role has been filled.
        """
        for role in self.crew:
            if role[0] == intended_role and role[1] is None:
                # intended role is available
                role[1] = person
                return True
        return False

    def to_csv(self):
        """
        Outputs the crew assignments of this Production to a csv file named
        self.name + "_assignment.csv"
        """
        with open(self.name + "_assignment.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for role in self.crew:
                if role[1] is None:
                    writer.writerow([role[0]])
                else:
                    writer.writerow(role)

    def __str__(self):
        return "Production: " + self.name

    def __repr__(self):
        return "Production: " + self.name
