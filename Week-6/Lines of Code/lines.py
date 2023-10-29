import sys

def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            code_lines = 0
            in_multiline_comment = False
            in_docstring = False

            for line in file:
                line = line.strip()

                # Check if the line is a docstring
                if line.startswith('"""') or line.startswith("'''"):
                    in_docstring = not in_docstring

                # Skip comments and docstrings
                if not in_multiline_comment and not in_docstring:
                    if line.startswith('#'):
                        continue

                # Check for multiline comments
                if '"""' in line or "'''" in line:
                    in_multiline_comment = not in_multiline_comment

                # Count non-blank, non-comment lines
                if line and not line.startswith('#'):
                    code_lines += 1

            return code_lines
    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found.")
    except Exception as e:
        sys.exit(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Error: Please specify a Python file ending with .py.")

    line_count = count_lines(filename)
    print(f"Total lines of code in '{filename}': {line_count}")

if __name__ == "__main__":
    main()
