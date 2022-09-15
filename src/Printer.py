class Color:

    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    PURPLE = "\033[0;35m"
    BOLD = "\033[;1m"
    RESET = "\033[0;0m"


class Printer:

    def colorPrint(text: str, color: Color) -> None:
        """Prints a colored string."""
        print(color + text + Color.RESET)

    def coloredText(text: str, color: Color) -> str:
        """Returns a colored string."""
        return color + text + Color.RESET

    def boldText(text: str) -> str:
        """Returns bold text."""
        return Color.BOLD + text + Color.RESET

    def printError(text: str) -> None:
        """Prints an error."""
        print(Color.RED + "[ERROR] " + text + Color.RESET)

    def printTitle(text: str) -> None:
        """Prints a title."""
        Printer.printSeparator(20, Color.PURPLE)
        print(Color.PURPLE + text.upper() + Color.RESET)
        Printer.printSeparator(20, Color.PURPLE)

    def printSeparator(n: int, color: Color) -> None:
        """Prints a colored separator of length n"""
        print(color + n * "-" + Color.RESET)
