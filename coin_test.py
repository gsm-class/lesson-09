import subprocess
import sys
from pathlib import Path

import pytest


COIN_SCRIPT = Path(__file__).with_name("coin.py")


@pytest.mark.parametrize(
    ("stdin_data", "expected_output"),
    [
        (
            "10 4200\n1\n5\n10\n50\n100\n500\n1000\n5000\n10000\n50000\n",
            "6",
        ),
        (
            "10 4790\n1\n5\n10\n50\n100\n500\n1000\n5000\n10000\n50000\n",
            "12",
        ),
    ],
)
def test_coin_sample_cases(stdin_data, expected_output):
    result = subprocess.run(
        [sys.executable, str(COIN_SCRIPT)],
        input=stdin_data,
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == expected_output