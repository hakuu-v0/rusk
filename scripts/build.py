import subprocess
import tomllib
from pathlib import Path


def main() -> None:
    main_path = str(object=Path("main.py").resolve())

    toml: dict[str, Any] = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf8"))
    product_name: str = toml["project"]["name"]
    product_version: str = toml["project"]["version"]

    args: list[str] = [
        "uv",
        "run",
        "nuitka",
        main_path,
        f"--product-name={product_name}",
        f"--product-version={product_version}",
        "--output-dir=build",
        f"--output-filename={product_name}",
        "--mode=onefile",
        "--onefile-tempdir-spec={CACHE_DIR}/{PRODUCT}/{VERSION}",
        "--include-data-files=.venv/Scripts/uv.exe=uv.exe",
        "--include-data-files=.venv/Scripts/uvx.exe=uvx.exe",
        "--remove-output",
        "--mingw64",
        "--windows-console-mode=disable",
        "--onefile-windows-splash-screen-image=images/splash.png",
        "--noinclude-default-mode=error",
        "--include-package-data=nicegui",
        "--nofollow-import-to=doctest",
        "--include-module=pygments.formatters.html",
    ]

    subprocess.run(args=args, check=True)


if __name__ == "__main__":
    main()
