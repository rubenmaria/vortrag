def print_owing(name: str) -> None:
    print_banner()
    print_details(get_outstanding(name))


def print_details(outstanding: float) -> None:
    print(f"name: {name}")
    print(f"amount: {outstanding}")
