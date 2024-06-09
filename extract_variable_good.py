def render_banner() -> None:
    is_mac = "MAC" in platform.upper()
    is_safari = "SAFARI" in browser
    was_resized = resize > 0
    if is_mac and is_safari and was_resized:
        do_something()
