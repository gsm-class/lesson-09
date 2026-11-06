import subprocess
import sys
from pathlib import Path


MEETING_ROOM_SCRIPT = Path(__file__).with_name("meeting_room_assign.py")


def test_meeting_room_sample_case():
    stdin_data = (
        "11\n"
        "1 4\n"
        "3 5\n"
        "0 6\n"
        "5 7\n"
        "3 8\n"
        "5 9\n"
        "6 10\n"
        "8 11\n"
        "8 12\n"
        "2 13\n"
        "12 14\n"
    )

    result = subprocess.run(
        [sys.executable, str(MEETING_ROOM_SCRIPT)],
        input=stdin_data,
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == "4"