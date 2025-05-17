# product name / version
# nuitka-project: --product-name="rusk"
# nuitka-project: --product-version=0.1.0

# output dir / filename
# nuitka-project: --output-dir="build"
# nuitka-project: --output-filename="rusk"


# nuitka-project: --remove-output

# nuitka-project: --macos-create-app-bundle

import webview

webview.create_window(title="Hello world", url="https://pywebview.flowrl.com/")
webview.start()
