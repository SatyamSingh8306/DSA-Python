class StringMethods:
    
    def __init__(self, string: str):
        self.string = string

    def find(self, substring: str, start: int = 0, end: int = None) -> int:
        """
        Parameters:
        - substring (str): The substring to search for.
        - start (int, optional): The index to start searching from. Default is 0.
        - end (int, optional): The index to end searching at. Default is None.
        
        Returns:
        - int: The lowest index of the substring if found, else -1.
        """
        pass

    def upper(self) -> str:
        """
        Parameters: None
        
        Returns:
        - str: A copy of the string converted to uppercase.
        """
        pass

    def lower(self) -> str:
        """
        Parameters: None
        
        Returns:
        - str: A copy of the string converted to lowercase.
        """
        pass

    def strip(self, chars: str = None) -> str:
        """
        Parameters:
        - chars (str, optional): The characters to remove from both ends. Default is None.
        
        Returns:
        - str: A copy of the string with specified characters removed from both ends.
        """
        pass

    def replace(self, old: str, new: str, count: int = -1) -> str:
        """
        Parameters:
        - old (str): The substring to be replaced.
        - new (str): The substring to replace with.
        - count (int, optional): The number of occurrences to replace. Default is -1 (all occurrences).
        
        Returns:
        - str: A new string with specified replacements.
        """
        pass

    def split(self, separator: str = None, maxsplit: int = -1) -> list:
        """
        Parameters:
        - separator (str, optional): The delimiter to split by. Default is None (whitespace).
        - maxsplit (int, optional): The maximum number of splits. Default is -1 (no limit).
        
        Returns:
        - list: A list of substrings resulting from the split operation.
        """
        pass

    def join(self, iterable: list) -> str:
        """
        Parameters:
        - iterable (list): The list of strings to join together.
        
        Returns:
        - str: A string formed by concatenating the elements of the iterable, separated by the original string.
        """
        pass

    def isdigit(self) -> bool:
        """
        Parameters: None
        
        Returns:
        - bool: True if all characters in the string are digits, otherwise False.
        """
        pass

    def isalpha(self) -> bool:
        """
        Parameters: None
        
        Returns:
        - bool: True if all characters in the string are alphabetic, otherwise False.
        """
        pass

    def startswith(self, prefix: str) -> bool:
        """
        Parameters:
        - prefix (str): The substring to check for at the beginning of the string.
        
        Returns:
        - bool: True if the string starts with the specified prefix, otherwise False.
        """
        pass

    def endswith(self, suffix: str) -> bool:
        """
        Parameters:
        - suffix (str): The substring to check for at the end of the string.
        
        Returns:
        - bool: True if the string ends with the specified suffix, otherwise False.
        """
        pass
