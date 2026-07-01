"""testarge CLI giriş noktası."""
from __future__ import annotations

import argparse

from . import __version__
from .core import greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="testarge",
        description="Basit bir selamlama aracı.",
    )
    parser.add_argument(
        "--name",
        "-n",
        default="Dünya",
        help="Selamlanacak isim (varsayılan: Dünya)",
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
