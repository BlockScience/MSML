from ..Classes import MathSpec


def write_glossary_report(ms: MathSpec, directory: str) -> None:
    """Function to write a report of each component and its description in MSML

    Args:
        ms (MathSpec): The mathematical specification object
        directory (str): Directory to put reports into
    """
    out = "# Glossary\n\n"

    path = directory + "/Glossary.md"
    with open(path, "w") as f:
        f.write(out)
