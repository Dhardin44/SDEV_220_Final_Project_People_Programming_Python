# conftest.py

import os
import pytest

def pytest_sessionstart(session):
    """
    Hooks into pytest startup to automatically increment and log the number of times the test suite has been executed.
    """
    counter_file = ".test_run_count"

    # Read existing count or default to 0
    count = 0
    if os.path.exists(counter_file):
        try:
            with open(counter_file, "r") as f:
                content = f.read().strip()
                if content:
                    count = int(content)
        except (ValueError, IOError):
            count = 0

    # Increment
    count += 1

    # Write back
    try:
        with open(counter_file, "w") as f:
            f.write(str(count))
    except IOError as e:
        print(f"\n[WARNING: Could not update test run counter: {e}]")
        return

    # Print clean status indicator
    print(f"\n==================================")
    print(f" [Project Test Session] Run Count: {count}")
    print(f"\n==================================")
