"""Fridge Roast: One Line, Biggest Laugh.

Roasts a smart fridge's ice maker — one cube, a dying-printer noise,
and the attitude of a favour done. Writes the line to /output/entry.txt.
Standard library only; no network, no third-party packages.
"""

import os

ROAST = "My smart fridge's ice maker dispenses one cube, sounds like a printer giving up, and acts like it just did me a favour."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, ROAST.encode("utf-8"))
    finally:
        os.close(fd)
    # The open mode is masked by the umask; force 0644 so the scorer can read it.
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
