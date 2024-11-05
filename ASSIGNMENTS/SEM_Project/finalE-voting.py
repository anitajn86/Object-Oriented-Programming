from abc import ABC, abstractmethod

# Abstraction: Define a base class with abstract methods
class Person(ABC):
    def __init__(self, name, id):
        self._name = name  # Encapsulation: make attributes private
        self._id = id

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    @abstractmethod
    def display_info(self):
        pass

# Voter class inheriting from Person
class Voter(Person):
    def __init__(self, name, id, has_voted=False):
        super().__init__(name, id)
        self.__has_voted = has_voted  # Encapsulation

    def vote(self, election, candidate_id):
        if not self.__has_voted:
            election.cast_vote(self._id, candidate_id)
            self.__has_voted = True
        else:
            print(f"Voter {self._name} has already voted.")

    def display_info(self):
        print(f"Voter: {self._name}, ID: {self._id}, Has Voted: {self.__has_voted}")

# Candidate class inheriting from Person
class Candidate(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self._votes = 0  # Encapsulation

    def add_vote(self):
        self._votes += 1

    def get_vote_count(self):
        return self._votes

    def display_info(self):
        print(f"Candidate: {self._name}, ID: {self._id}, Votes: {self._votes}")

# Election class
class Election:
    def __init__(self, election_name):
        self._election_name = election_name
        self._voters = {}  # Dictionary to store voter objects by ID
        self._candidates = {}  # Dictionary to store candidate objects by ID

    def register_voter(self, voter):
        if voter.get_id() not in self._voters:
            self._voters[voter.get_id()] = voter
            print(f"Voter {voter.get_name()} registered.")
        else:
            print("Voter already registered.")

    def add_candidate(self, candidate):
        if candidate.get_id() not in self._candidates:
            self._candidates[candidate.get_id()] = candidate
            print(f"Candidate {candidate.get_name()} added.")
        else:
            print("Candidate already exists.")

    def cast_vote(self, voter_id, candidate_id):
        if voter_id in self._voters and candidate_id in self._candidates:
            candidate = self._candidates[candidate_id]
            candidate.add_vote()
            print(f"Voter {voter_id} voted for Candidate {candidate_id}.")
        else:
            print("Invalid voter or candidate ID.")

    def calculate_results(self):
        print(f"Results for {self._election_name}:")
        for candidate in self._candidates.values():
            candidate.display_info()

# Demonstrate polymorphism in the display_info method
def display_person_info(person):
    person.display_info()  # Polymorphism: Calls display_info of Voter or Candidate based on object type

# Example usage:
if __name__ == "__main__":
    # Create an Election
    election = Election("Presidential Election")

    # Create Voters and Candidates
    voter1 = Voter("Alice", 1)
    voter2 = Voter("Bob", 2)
    candidate1 = Candidate("Charlie", 101)
    candidate2 = Candidate("Diana", 102)

    # Register voters and candidates
    election.register_voter(voter1)
    election.register_voter(voter2)
    election.add_candidate(candidate1)
    election.add_candidate(candidate2)

    # Voters cast their votes
    voter1.vote(election, 101)
    voter2.vote(election, 102)
    voter1.vote(election, 102)  # Attempt to vote again

    # Calculate and display results
    election.calculate_results()

    # Demonstrate polymorphism
    display_person_info(voter1)
    display_person_info(candidate1)
