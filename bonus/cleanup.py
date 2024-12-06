"""Clean up Python code copied verbatim from the interpreter."""

import sys
from pathlib import Path

def main(filename):
    path = Path(filename)
    contents = path.read_text()

    PROMPT = '>>> '
    CONTINUE_PROMPT = '... '

    raw_lines = contents.splitlines()
    lines = []
    for raw_line in raw_lines:
        start_at = 0
        if raw_line.startswith(PROMPT): # statement entered in REPL
            start_at = len(PROMPT)
        elif raw_line.startswith(CONTINUE_PROMPT): # statement that continues
            start_at = len(CONTINUE_PROMPT)
        else: # output from code that was run in the REPL
            continue
        line = raw_line[start_at:]
        lines.append(line)

    for line in lines:
        print(line)

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Usage: python3 cleanup.py filename')
        sys.exit(-1)

    main(sys.argv[1])
