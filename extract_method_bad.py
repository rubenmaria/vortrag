def print_owing(name: str) -> None:
    print_banner()

    # Print details
    print(f"name: {name}")
    print(f"amount: {get_outstanding(name)}")
