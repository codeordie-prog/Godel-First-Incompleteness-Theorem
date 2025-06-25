from typing import Set, List
from axioms import AXIOMS
from godel_code import GodelEncoder

class ProofEngine:
    """
    Attempts to prove a statement from a set of axioms using simple inference rules and Gödel encoding.
    """
    def __init__(self, statement: str, max_steps: int) -> None:
        """
        Initializes the proof engine and attempts to prove the statement.
        """
        self.proof: bool = self.proof_engine(statement, max_steps)

    def encode_axioms(self, axioms: Set[str]) -> Set[int]:
        """
        Encodes a set of axioms as Gödel numbers.
        """
        encoder = GodelEncoder()
        return {encoder.encode(axiom) for axiom in axioms}

    def encode_statement(self, statement: str) -> int:
        """
        Encodes a statement as a Gödel number.
        """
        encoder = GodelEncoder()
        return encoder.encode(statement)

    def apply_inference(self, facts: Set[str]) -> Set[str]:
        """
        Applies inference rules to generate new facts from existing ones.
        """
        new_facts: Set[str] = set()
        for fact in facts:
            if fact.endswith("is a number"):
                x = fact[:-len(" is a number")]
                new_fact = f"{x} + 1 is a number"
                if new_fact not in facts:
                    new_facts.add(new_fact)
        return new_facts

    def proof_engine(self, statement: str, max_steps: int) -> bool:
        """
        Attempts to prove the statement within a maximum number of inference steps.
        Returns True if the statement is provable, False otherwise.
        """
        facts: Set[str] = set(AXIOMS)
        encoded_statement = self.encode_statement(statement)
        print("\n")
        print("Statement's Gödel code is:", encoded_statement)
        print("\n")
        for _ in range(max_steps):
            new_facts = self.apply_inference(facts)
            encoded_new_facts = self.encode_axioms(new_facts)
            if encoded_statement in encoded_new_facts:
                return True
            facts.update(new_facts)
            print("Axioms in use:", encoded_new_facts)
        return encoded_statement in self.encode_axioms(facts)
    

