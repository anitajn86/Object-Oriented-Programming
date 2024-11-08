import tkinter as tk
from tkinter import messagebox
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
            messagebox.showwarning("Voting Error", f"Voter {self._name} has already voted.")

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
            messagebox.showinfo("Registration", f"Voter {voter.get_name()} registered.")
        else:
            messagebox.showwarning("Registration Error", "Voter already registered.")

    def add_candidate(self, candidate):
        if candidate.get_id() not in self._candidates:
            self._candidates[candidate.get_id()] = candidate
            messagebox.showinfo("Candidate Registration", f"Candidate {candidate.get_name()} added.")
        else:
            messagebox.showwarning("Registration Error", "Candidate already exists.")

    def cast_vote(self, voter_id, candidate_id):
        if voter_id in self._voters and candidate_id in self._candidates:
            candidate = self._candidates[candidate_id]
            candidate.add_vote()
            messagebox.showinfo("Vote", f"Voter {voter_id} voted for Candidate {candidate_id}.")
        else:
            messagebox.showerror("Voting Error", "Invalid voter or candidate ID.")

    def calculate_results(self):
        results = ""
        for candidate in self._candidates.values():
            results += f"{candidate.get_name()}: {candidate.get_vote_count()} votes\n"
        messagebox.showinfo("Election Results", results)

# GUI class for the voting system
class VotingGUI:
    def __init__(self, election):
        self.election = election
        self.root = tk.Tk()
        self.root.title("E-Voting System")

        # Voter Registration Section
        tk.Label(self.root, text="Voter Registration").grid(row=0, column=0, padx=10, pady=10)
        self.voter_name_entry = tk.Entry(self.root)
        self.voter_name_entry.grid(row=1, column=0)
        self.voter_id_entry = tk.Entry(self.root)
        self.voter_id_entry.grid(row=2, column=0)
        tk.Button(self.root, text="Register Voter", command=self.register_voter).grid(row=3, column=0)

        # Candidate Registration Section
        tk.Label(self.root, text="Candidate Registration").grid(row=0, column=1, padx=10, pady=10)
        self.candidate_name_entry = tk.Entry(self.root)
        self.candidate_name_entry.grid(row=1, column=1)
        self.candidate_id_entry = tk.Entry(self.root)
        self.candidate_id_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Add Candidate", command=self.add_candidate).grid(row=3, column=1)

        # Voting Section
        tk.Label(self.root, text="Voting").grid(row=4, column=0, columnspan=2, pady=10)
        self.voter_id_vote_entry = tk.Entry(self.root)
        self.voter_id_vote_entry.grid(row=5, column=0)
        self.candidate_id_vote_entry = tk.Entry(self.root)
        self.candidate_id_vote_entry.grid(row=5, column=1)
        tk.Button(self.root, text="Cast Vote", command=self.cast_vote).grid(row=6, column=0, columnspan=2)

        # Results Section
        tk.Button(self.root, text="Calculate Results", command=self.show_results).grid(row=7, column=0, columnspan=2, pady=10)

    def register_voter(self):
        name = self.voter_name_entry.get()
        voter_id = int(self.voter_id_entry.get())
        voter = Voter(name, voter_id)
        self.election.register_voter(voter)
        self.voter_name_entry.delete(0, tk.END)
        self.voter_id_entry.delete(0, tk.END)

    def add_candidate(self):
        name = self.candidate_name_entry.get()
        candidate_id = int(self.candidate_id_entry.get())
        candidate = Candidate(name, candidate_id)
        self.election.add_candidate(candidate)
        self.candidate_name_entry.delete(0, tk.END)
        self.candidate_id_entry.delete(0, tk.END)

    def cast_vote(self):
        voter_id = int(self.voter_id_vote_entry.get())
        candidate_id = int(self.candidate_id_vote_entry.get())
        self.election.cast_vote(voter_id, candidate_id)
        self.voter_id_vote_entry.delete(0, tk.END)
        self.candidate_id_vote_entry.delete(0, tk.END)

    def show_results(self):
        self.election.calculate_results()

    def run(self):
        self.root.mainloop()

# Example usage
if __name__ == "__main__":
    election = Election("Presidential Election")
    gui = VotingGUI(election)
    gui.run()
