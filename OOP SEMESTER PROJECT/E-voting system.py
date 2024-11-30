from abc import ABC, abstractmethod

class Participant(ABC):
    def __init__(self, name, gender, age, location):
        self._name = name
        self._gender = gender
        self._age = age
        self._location = location

    @property
    def name(self):
        return self._name
    
    @property
    def gender(self):
        return self._gender
    
    @abstractmethod
    def age_validity(self):
        pass

    @abstractmethod
    def location_validity(self):
        pass


class Voter(Participant): #inheritance
    def __init__(self, name, gender, age, location, voter_id, has_voted=False):
        super().__init__(name, gender, age, location)
        self._voter_id = voter_id   #encapsulation
        self._has_voted = has_voted #encapsulation

    def age_validity(self): #abstraction
        if self._age >= 18:
            return True
        else:
            return False

    def location_validity(self):
        allowed_location = "Mukono"   #set the voting location to mukono
        return self._location == allowed_location

    def register_voter(self):
        if self.age_validity() and self.location_validity():
            print(f"{self._name} has been registered to vote.")
            return True
        else:
            print(f"{self._name} is not eligible to vote.")
            return False

    def voting_status(self):
        if self._has_voted:
            print(f"{self._name} has already voted.")
        else:
            print(f"{self._name} has not yet voted.")

    def cast_vote(self):  #polymorphism
        if not self._has_voted:
            self._has_voted = True
            print(f"{self._name} has cast their vote.")
            return True
        else:
            print(f"{self._name} has already voted.")
            return False

    def __str__(self):
        return f"{self._name}, {self._gender}, {self._age}, {self._location}, {self._voter_id}, {self._has_voted}"


class Candidate(Participant):
    def __init__(self, name, gender, age, location, candidate_id, votes=0):
        super().__init__(name, gender, age, location)
        self._candidate_id = candidate_id
        self._votes = votes

    def age_validity(self): #polymorhism and abstraction
        if 25 <= self._age <= 70:
            return True
        else:
            return False

    def location_validity(self):
        allowed_location = "Mukono"  #set the voting location to mukono
        return self._location == allowed_location

    def register_candidate(self):
        if self.age_validity() and self.location_validity():
            print(f"{self._name} has been registered as a candidate.")
            return True
        else:
            print(f"{self._name} cannot be registered as a candidate.")
            return False

    def receive_vote(self):
        self._votes += 1

    def get_votes(self):
        return self._votes

    def __str__(self):   #to show formatted output instead of the memory location
        return f"{self._name}, {self._gender}, {self._age}, {self._location}, {self._candidate_id}, {self._votes}"


class Vote:
    def __init__(self, voter, candidate):
        if not isinstance(voter, Voter) or not isinstance(candidate, Candidate):
            raise ValueError("Voter and Candidate must be instances of their respective classes.")
        self._voter = voter
        self._candidate = candidate

    def cast_vote(self): #polymorphism
        if self._voter.cast_vote():
            self._candidate.receive_vote()
            print(f"Vote has been cast for {self._candidate.name} by {self._voter.name}.")


class Election:
    def __init__(self, election_name):
        self._election_name = election_name
        self._voters = []  #to store list of voters
        self._candidates = []  #to store list of candidates

    def add_voter(self, voter):
        if isinstance(voter, Voter):
            if voter.register_voter():
                self._voters.append(voter)
                print(f"{voter.name} added to the voter list.")

    def add_candidate(self, candidate):
        if isinstance(candidate, Candidate):
            if candidate.register_candidate():
                self._candidates.append(candidate)
                print(f"{candidate.name} added to the candidate list.")

    def show_results(self):
        print(f"\nResults for the {self._election_name} Election")
        for candidate in self._candidates:
            print(f"Candidate {candidate.name} received {candidate.get_votes()} votes.")
        winner = max(self._candidates, key=lambda c: c.get_votes(), default=None)
        if winner:
            print(f"\nThe winner is {winner.name} with {winner.get_votes()} votes.")


# Example usage
# Creating instances of Voter
v1 = Voter("Anita", "Female", 22, "Mukono", 1)
v2 = Voter("Tori Vega", "Female", 24, "Entebbe", 2)
v3 = Voter("Liz", "Female", 15, "Mukono", 3)
v4 = Voter("Noela","Female",29,"Mukono",4)
v5 = Voter("Joy","Female",32,"Kololo",5)
v6 = Voter("Calvin","Male",16,"Mukono",6)
v7 = Voter("Charles","Male",55,"Jinja",7)

# Creating instances of Candidate
c1 = Candidate("Christopher Robin", "Male", 35, "Mukono", 101)
c2 = Candidate("Jamie Foxx", "Male", 45, "Mukono", 102)

# Initializing the Election
election = Election("Mukono Mayor Election")

# Adding Voters and Candidates to the Election
election.add_voter(v1)
election.add_voter(v2)
election.add_voter(v3)
election.add_voter(v4)
election.add_voter(v5)
election.add_voter(v6)
election.add_voter(v7)

election.add_candidate(c1)
election.add_candidate(c2)

# Casting Votes
vote1 = Vote(v1, c1)
vote2 = Vote(v2, c1)
vote3 = Vote(v3, c1)
vote4 = Vote(v4, c2)
vote5 = Vote(v5, c2)

vote1.cast_vote()
vote2.cast_vote()
vote3.cast_vote()
vote4.cast_vote()
vote5.cast_vote()

# Displaying Results
election.show_results()
