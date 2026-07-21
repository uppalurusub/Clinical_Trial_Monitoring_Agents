def format_percent(value, decimals: int = 2) -> str:
    try:
        return f"{float(value):.{decimals}f}%"
    except (TypeError, ValueError):
        return "-"


def format_value(value, default: str = "-"):
    return default if value is None or value == "" else value


def yes_no(value) -> str:
    return "Yes" if bool(value) else "No"
