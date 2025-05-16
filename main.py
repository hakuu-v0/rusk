# product name / version
# nuitka-project: --product-name="rusk"
# nuitka-project: --product-version=0.1.0

# output dir / filename
# nuitka-project: --output-dir="build"
# nuitka-project: --output-filename="rusk"

# nuitka-project: --mode=onefile
# nuitka-project: --onefile-tempdir-spec={CACHE_DIR}\{PRODUCT}\{VERSION}
# nuitka-project: --include-data-files=.venv\Scripts\uv.exe=uv.exe
# nuitka-project: --include-data-files=.venv\Scripts\uvx.exe=uvx.exe
# nuitka-project: --remove-output
# nuitka-project: --mingw64
# nuitka-project: --windows-console-mode=disable
# nuitka-project: --onefile-windows-splash-screen-image=images\splash.png
# nuitka-project: --noinclude-default-mode=error
# nuitka-project: --include-package-data=nicegui
# nuitka-project: --nofollow-import-to=doctest
# nuitka-project: --include-module=pygments.formatters.html


from nicegui import app, native, ui

from app.startup import Startup

app.on_startup(handler=Startup().startup())

# True or False
debug = False

if debug:
    ui.run(uvicorn_reload_includes="*.css")
else:
    app.native.window_args["frameless"] = True
    ui.run(native=True, reload=False, port=native.find_open_port(), title="")
