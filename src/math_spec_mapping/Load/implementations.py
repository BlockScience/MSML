import os


def load_implementations(ms):
    implementations = {}
    python_path = "src/Implementations/Python/__init__.py"
    if os.path.exists(python_path):
        implementations["python"] = load_python_implementations()

    ms["Implementations"] = implementations


def load_python_implementations():
    from src.Implementations.Python import implementation

    return implementation
