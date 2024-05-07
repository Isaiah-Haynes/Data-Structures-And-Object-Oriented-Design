import Ballot as bal

class Candidate:
    def __init__(self, name):
        # This constuctor should be initalized with a candidate's name (a string)
        # The Candidate object should store a linear collection of ballots that were
        # cast for her. A ballot is considered cast for the candidate if that
        # candidate has the top ranking on that ballot.
        self.some_name = name
        self.some_number = list()
        pass

    def get_name(self):
        # Return the name of the candidate
        return self.some_name
        pass

    def add_ballot(self, ballot):
        # Add the ballot to the internal collection of ballots that were cast for the
        # candidate.
        self.some_number.append(ballot)

    def get_ballots(self):
        # Return the collection of ballots cast for the candidate
        return self.some_number
        pass

    def num_votes(self):
        # Return the number of ballots cast for the candidate
        #possibly sum of some_number
        num_vots = 0
        for i in self.some_number:
            num_vots += i
            
        return num_vots
        pass

    def __eq__(self, other):
        # Two candidates are the same if they have the same names
        return self.some_name == other.some_name    
        pass

    def __str__(self):
        # Print the candidate's name and the number of votes that were cast for her
        # The format should be
        # Candidate Name: some_name\n
        # Number of Votes: some_number\n
        return "Candidate Name: {}\n Number of Votes: {}".format(some_name, some_number)
        pass
  

