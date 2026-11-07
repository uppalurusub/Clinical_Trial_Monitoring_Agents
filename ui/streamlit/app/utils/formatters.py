def format_currency(value):
    try:
        return f"${float(value or 0):,.2f}"
    except (TypeError, ValueError):
        return "$0.00"


def format_score(value, decimals=2):
    try:
        return f"{float(value or 0):.{decimals}f}"
    except (TypeError, ValueError):
        return f"{0:.{decimals}f}"


def format_seconds(value):
    return f"{format_score(value)} sec"


def yes_no(value):
    return "Yes" if value else "No"


def value_or_na(value):
    return value if value not in (None, "") else "N/A"
