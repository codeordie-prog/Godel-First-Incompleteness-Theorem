from sympy import isprime
from typing import Dict, List

class SymbolMap:
    """
    Maintains a mapping between symbols and their Gödel codes for encoding and decoding statements.
    """
    def __init__(self) -> None:
        self.symbol_map: Dict[str, int] = {
            "0": 1,
            "+": 2,
            "1": 3,
            "2": 4,
            "3": 5,
            "4": 6,
            "5": 7,
            "is": 8,
            "a": 9,
            "number": 10,
            "This": 11,
            "statement": 12,
            "not": 13,
            "provable": 14
        }

    def reverse_map(self) -> Dict[int, str]:
        """
        Returns the reverse mapping from code to symbol.
        """
        return {v: k for k, v in self.symbol_map.items()}


class GodelEncoder:
    """
    Encodes and decodes statements using Gödel numbering.
    """
    def get_primes(self, n: int) -> List[int]:
        """
        Returns the first n prime numbers.
        """
        primes: List[int] = []
        i: int = 2
        while len(primes) < n:
            if isprime(i):
                primes.append(i)
            i += 1
        return primes

    def encode(self, statement: str) -> int:
        """
        Encodes a statement as a Gödel number.
        """
        symbol_map = SymbolMap().symbol_map
        tokens = statement.split()
        codes = [symbol_map[token] for token in tokens]
        primes = self.get_primes(len(codes))
        result = 1
        for p, c in zip(primes, codes):
            result *= p ** c
        return result


class GodelDecoder:
    
    def decode(self, number: int) -> str:
        """
        Decodes a Gödel number back into a statement.
        """
        reverse_map = SymbolMap().reverse_map()
        primes = self.get_primes(500)
        decoded: List[str] = []
        for p in primes:
            count = 0
            while number % p == 0:
                number //= p
                count += 1
            if count > 0:
                decoded.append(reverse_map[count])
            if number == 1:
                break
        return " ".join(decoded)
    



