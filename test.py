from formal_system import ProofEngine


def run_godel_test() -> None:
    """
    Runs tests on the ProofEngine for both a provable and an unprovable statement.
    """
    provable_statement = "0 is a number"
    unprovable_statement = "This statement is not provable"

    print("Testing provable statement:")
    engine1 = ProofEngine(provable_statement, 10)
    if engine1.proof:
        print("\n")
        print(f"SUCCESS: The statement '{provable_statement}' is provable.")
    else:
        print("\n")
        print(f"FAIL: The statement '{provable_statement}' should be provable but was not.")

    print("\nTesting unprovable (Gödel) statement:")
    engine2 = ProofEngine(unprovable_statement, 10)
    if engine2.proof:
        print("\n")
        print(f"FAIL: The statement '{unprovable_statement}' should not be provable but was.")
    else:
        print("\n")
        print(f"SUCCESS: The statement '{unprovable_statement}' is true but cannot be proved within the system.")


if __name__ == "__main__":
    run_godel_test()