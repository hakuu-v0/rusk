## 使い方

```
python.exe -m nuitka [--mode=compilation_mode] [--run] [options] main_module.py
```

## 注意

一般的なプラグインのヘルプ（多くの場合、独自のコマンドラインオプションもあります）については、'--help-plugins' の出力を参照してください。

## オプション

### 一般

```--help```
このヘルプメッセージを表示して終了します。

```--version```
バージョン情報とバグ報告用の重要な詳細を表示して終了します。デフォルトはオフです。

```--module```
プログラムの代わりにインポート可能なバイナリ拡張モジュールを作成します。デフォルトはオフです。

```--mode=COMPILATION_MODE```
コンパイルするモードを指定します。acceleratedは現在のPython環境で動作し、その環境に依存します。standaloneは実行可能ファイルを含むフォルダを作成し、他のマシンでも動作します。onefileは単一の実行ファイルを作成して配布できます。appはonefileと同様ですが、macOSでは使用しません。moduleはモジュールを作成し、packageはサブモジュールやサブパッケージも含めます。dllは現在開発中で、一般ユーザー向けではありません。デフォルトは'accelerated'です。

```--standalone```
スタンドアロンモードを有効にします。これにより、作成したバイナリを他のマシンに移しても、既存のPythonインストールを使用せずに実行できます。その分ファイルサイズは大きくなります。このオプションは "--follow-imports" および "--python-flag=no_site" を暗黙的に有効にします。デフォルトはオフです。

```--onefile```
スタンドアロンモードに加えて、onefileモードを有効にします。フォルダではなく、圧縮された単一の実行ファイルが作成されます。デフォルトはオフです。

```--python-flag=FLAG```
使用するPythonフラグを指定します。デフォルトは現在Nuitkaを実行している設定です。これにより特定のモードを強制できます。サポートされているオプション例: "-S"（"no_site"のエイリアス）、"static_hashes"（ハッシュのランダム化を無効化）、"no_warnings"（Python実行時の警告を表示しない）、"-O"（"no_asserts"のエイリアス）、"no_docstrings"（ドキュメント文字列を使用しない）、"-u"（"unbuffered"のエイリアス）、"isolated"（外部コードを読み込まない）、"-P"（"safe_path"のエイリアス、カレントディレクトリをモジュール検索に使わない）、"-m"（パッケージモード、"package.__main__"としてコンパイル）。デフォルトは空です。

```--python-debug```
デバッグバージョンを使用するかどうか。デフォルトは現在使用中のPythonに従います。主にデバッグやテスト用途です。

```--python-for-scons=PATH```
Python 3.4でコンパイルする場合、Scons用に使用するPythonバイナリのパスを指定します。それ以外の場合、Nuitkaは現在実行中のPythonやWindowsレジストリからPythonインストールを自動検出します。WindowsではPython 3.5以上、非WindowsではPython 2.6または2.7も利用可能です。

```--main=PATH```
1回だけ指定した場合、位置引数（コンパイルするファイル名）の代わりとなります。複数回指定した場合は「multidist」（ユーザーマニュアル参照）を有効にし、ファイル名や呼び出し名に応じて異なるバイナリを作成できます。

---

### モジュールやパッケージの含め方の制御

```--include-package=PACKAGE```
パッケージ全体を含めます。Pythonの名前空間（例: "some_package.sub_package"）を指定すると、Nuitkaがそのディスク上の場所を見つけて、配下のすべてのモジュールをバイナリや拡張モジュールに含め、コードからインポートできるようにします。不要なサブパッケージ（例: テスト用）を除外したい場合は、"--nofollow-import-to=*.tests" のように指定できます。デフォルトは空です。

```--include-module=MODULE```
単一のモジュールを含めます。Pythonの名前空間（例: "some_package.some_module"）を指定すると、Nuitkaがそのモジュールを見つけてバイナリや拡張モジュールに含め、コードからインポートできるようにします。デフォルトは空です。

```--include-plugin-directory=MODULE/PACKAGE```
指定したディレクトリ内のコードも含めます。それぞれをメインファイルとして扱います。他の含め方のオプションよりも優先されます。通常は名前で指定する他のオプションを推奨しますが、特殊な用途でのみ使用してください。複数回指定可能。デフォルトは空です。

```--include-plugin-files=PATTERN```
PATTERNに一致するファイルを含めます。他のすべてのフォローオプションよりも優先されます。複数回指定可能。デフォルトは空です。

```--prefer-source-code```
すでにコンパイル済みの拡張モジュールがあり、ソースファイルも存在する場合、通常は拡張モジュールが使われますが、ソースコードからコンパイルした方がパフォーマンスが良くなります。これを有効にするとソースコードからのコンパイルを優先します。無効にしたい場合は --no-prefer-source-code を使います。デフォルトはオフです。

---

### インポートされたモジュールのフォロー制御

```--follow-imports```
すべてのインポートされたモジュールに降りていきます。スタンドアロンモードではデフォルトでオン、それ以外ではオフです。

```--follow-import-to=MODULE/PACKAGE```
指定したモジュールやパッケージにインポートがあればフォローします。複数回指定可能。デフォルトは空です。

```--nofollow-import-to=MODULE/PACKAGE```
指定したモジュール名やパッケージ名には、たとえ使われていても絶対にフォローしません。他のすべてのオプションよりも優先されます。パターン（例: "*.tests"）も指定可能。複数回指定可能。デフォルトは空です。

```--nofollow-imports```
インポートされたモジュールには一切降りていきません。他のすべての含め方のオプションよりも優先され、スタンドアロンモードでは使用できません。デフォルトはオフです。

```--follow-stdlib```
標準ライブラリからインポートされたモジュールにも降りていきます。コンパイル時間が大幅に増加し、十分にテストされていない場合があります。デフォルトはオフです。

---
### Onefile オプション

```--onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC```
onefile モードで展開先のフォルダを指定します。デフォルトは '{TEMP}/onefile_{PID}_{TIME}' で、ユーザーの一時ディレクトリが使われ、実行後に削除されます。例: '{CACHE_DIR}/{COMPANY}/{PRODUCT}/{VERSION}' のような静的なキャッシュパスを指定すると、そのフォルダは削除されません。

```--onefile-cache-mode=ONEFILE_CACHED_MODE```
spec の内容から自動的にモードが決まります。ランタイム依存のパスを含む場合は "temporary" となり、実行後に展開ファイルが削除されます。静的なパスの場合は "cached" となり、次回以降の実行で再利用され起動が速くなります。

```--onefile-child-grace-time=GRACE_TIME_MS```
子プロセス終了時（CTRL-C やシャットダウン等）に、Python コードへ "KeyboardInterrupt" を送ってから強制終了するまでの猶予時間（ミリ秒単位）を指定します。デフォルトは 5000ms です。

```--onefile-no-compression```
onefile 作成時にペイロードの圧縮を無効化します。主にデバッグや高速化用途です。デフォルトはオフです。

```--onefile-as-archive```
onefile 作成時に、専用の "nuitka-onefile-unpack" で展開できるアーカイブ形式を使用します。デフォルトはオフです。

```--onefile-no-dll```
onefile 作成時、一部プラットフォーム（現在は Windows でキャッシュを使わない場合）で Python コードを DLL ではなく実行ファイルとして展開します。デフォルトはオフです。

---

### データファイル

```--include-package-data=PACKAGE```
指定したパッケージ名のデータファイルを含めます。DLL や拡張モジュールは含まれません。ファイル名パターンも指定可能です。例: "--include-package-data=package_name"（全ファイル）、"--include-package-data=package_name:*.txt"（特定拡張子のみ）、"--include-package-data=package_name:some_filename.dat"（特定ファイルのみ）。デフォルトは空です。

```--include-data-files=DESC```
配布物にファイルを含めます。様々な形式が利用可能です。例: '--include-data-files=/path/to/file/*.txt=folder_name/some.txt'（単一ファイル）、'--include-data-files=/path/to/files/*.txt=folder_name/'（複数ファイル）、'--include-data-files=/path/to/scan=folder_name/=**/*.txt'（ディレクトリ構造を保持して再帰的にコピー）。デフォルトは空です。

```--include-data-dir=DIRECTORY```
指定ディレクトリ内のデータファイルを配布物に含めます（再帰的）。例: '--include-data-dir=/path/some_dir=data/some_dir'。コード以外の全ファイルがコピーされます。不要な場合は '--noinclude-data-files' で除外可能です。デフォルトは空です。

```--noinclude-data-files=PATTERN```
指定したパターンに一致するデータファイルを含めません。パッケージ 'package_name' のファイルを除外する場合は 'package_name/*.txt' のように指定します。ディレクトリ全体を除外する場合は 'package_name' を指定します。デフォルトは空です。

```--include-onefile-external-data=PATTERN```
onefile バイナリの外部にデータファイルを含めます（内部ではなく）。'--onefile' コンパイル時のみ有効です。まず他の `--include-*data*` オプションでファイルを含め、その後に配布物内のターゲットパスを指定します。デフォルトは空です。

```--list-package-data=LIST_PACKAGE_DATA```
指定したパッケージ名のデータファイル一覧を出力します。デフォルトは出力しません。

```--include-raw-dir=DIRECTORY```
指定ディレクトリをそのまま配布物に含めます（再帰的）。通常は '--include-data-dir' の利用を推奨します。デフォルトは空です。

---

### メタデータサポート

```--include-distribution-metadata=DISTRIBUTION```
指定したディストリビューション名のメタデータ情報を含めます。一部のパッケージはメタデータの有無やバージョン、エントリポイントなどをチェックしますが、このオプションを指定しないとコンパイル時に認識された場合のみ有効となり、常に動作するとは限りません。このオプションはコンパイルに含めるパッケージに対してのみ意味があります。デフォルトは空です。

```--list-distribution-metadata```
すべてのパッケージについてディストリビューションとその詳細の一覧を出力します。デフォルトは出力しません。

---

### DLLファイル

```--noinclude-dlls=PATTERN```
指定したファイル名パターンに一致するDLLファイルを含めません。これはターゲットファイル名に対して適用され、ソースパスには適用されません。たとえば、パッケージ 'package_name' に含まれる 'someDLL' を除外したい場合は 'package_name/someDLL.*' のように指定します。デフォルトは空です。

```--list-package-dlls=LIST_PACKAGE_DLLS```
指定したパッケージ名に対して見つかったDLLの一覧を出力します。デフォルトは出力しません。

```--list-package-exe=LIST_PACKAGE_EXE```
指定したパッケージ名に対して見つかったEXEファイルの一覧を出力します。デフォルトは出力しません。

---

### Nuitkaによる警告制御

```--warn-implicit-exceptions```
コンパイル時に検出された暗黙的な例外について警告を有効にします。

```--warn-unusual-code```
コンパイル時に検出された異常なコードについて警告を有効にします。

```--assume-yes-for-downloads```
必要に応じてNuitkaが外部コード（例: dependency walker, ccache, Windowsではgccなど）をダウンロードすることを許可します。無効にするには、入力をnulデバイスからリダイレクトしてください（例: "</dev/null" または "<NUL:"）。デフォルトはプロンプト表示です。

```--nowarn-mnemonic=MNEMONIC```
指定したニーモニックの警告を無効にします。これらは特定のトピックに注意を促すために表示され、通常はNuitkaのWebサイトへのリンクとなっています。ニーモニックはURLの末尾部分（.htmlを除く）です。複数回指定可能で、シェルパターンも受け付けます。デフォルトは空です。

---

### コンパイル後の即時実行

```--run```
作成したバイナリ（またはコンパイル済みモジュール）を直ちに実行します。デフォルトはオフです。

```--debugger```
デバッガ（例: "gdb" や "lldb"）内で実行し、自動的にスタックトレースを取得します。デバッガは自動的に選択されますが、NUITKA_DEBUGGER_CHOICE環境変数で名前を指定することもできます。デフォルトはオフです。

---

### コンパイル設定

```--user-package-configuration-file=YAML_FILENAME```
ユーザーが提供するパッケージ設定用のYAMLファイルを指定します。DLLの追加、不要コードの除去、隠れた依存関係の追加などが可能です。書式の詳細はNuitkaパッケージ設定マニュアルを参照してください。複数回指定可能。デフォルトは空です。

```--full-compat```
CPythonとの完全な互換性を強制します。CPythonの動作とわずかでも異なる（例: より良いトレースバックや例外メッセージなど）場合でも許容しません。主にテスト用途であり、通常は使用しないでください。

```--file-reference-choice=FILE_MODE```
"__file__" の値をどのようにするか選択します。"runtime"（スタンドアロンバイナリモードやモジュールモードのデフォルト）では、作成されたバイナリやモジュール自身の場所を基準に "__file__" の値を決定します。パッケージを含める場合は、その配下のディレクトリにあるかのように振る舞います。データファイルを含める場合に便利です。単なる高速化目的の場合は "original"（ソースファイルの場所を使用）を推奨します。"frozen" を選ぶと "<frozen module_name>" という表記になります。互換性のため "__file__" の値には常に ".py" 拡張子が付きます。

```--module-name-choice=MODULE_NAME_MODE```
"__name__" および "__package__" の値をどのようにするか選択します。"runtime"（モジュールモードのデフォルト）では、作成されたモジュールが親パッケージから "__package__" の値を推測し、完全な互換性を保ちます。"original"（他のモードのデフォルト）では、より静的な最適化が可能ですが、通常どのパッケージにもロードできるモジュールには非互換となります。

---

### 出力設定

```--output-filename=FILENAME```
実行ファイルの名前を指定します。拡張モジュールやスタンドアロンモードでは指定できません。パス情報を含める場合は、そのディレクトリが存在している必要があります。デフォルトはこのプラットフォームでは '<program_name>.exe' です。

```--output-dir=DIRECTORY```
中間ファイルや最終出力ファイルを配置するディレクトリを指定します。指定したディレクトリにビルドフォルダ、distフォルダ、バイナリなどが作成されます。デフォルトはカレントディレクトリです。

```--remove-output```
モジュールやexeファイルの作成後にビルドディレクトリを削除します。デフォルトはオフです。

```--no-pyi-file```
Nuitkaが作成する拡張モジュール用の '.pyi' ファイルを生成しません。これは暗黙的なインポートの検出に使われます。デフォルトはオフです。

```--no-pyi-stubs```
拡張モジュール用の '.pyi' ファイル作成時にstubgenを使用しません。APIが公開されますが、stubgenが問題を引き起こす場合に有効です。デフォルトはオフです。

---

### デプロイ制御

```--deployment```
互換性問題の発見を容易にするためのコードを無効化します。例えば "-c" 引数での実行（モジュールを再帰的に起動し続ける場合がある）を防ぎます。エンドユーザー向けに配布する際に有効化してください。開発中は典型的な問題発見のため無効のままが便利です。デフォルトはオフです。

```--no-deployment-flag=FLAG```
デプロイメントモードを維持しつつ、特定の機能のみ無効化します。デプロイメントモードによるエラー時にこれらの識別子が出力されます。デフォルトは空です。

---

### 環境変数制御

```--force-runtime-environment-variable=VARIABLE_SPEC```
指定した環境変数に値を強制的に設定します。デフォルトは空です。

---

### デバッグ機能

```--debug```
Nuitkaの自己診断チェックをすべて実行します。運用環境では使用しないでください。デフォルトはオフです。

```--no-debug-immortal-assumptions```
通常 "--debug" で行われるチェックを無効化します。Python3.12以降では、既知のイミュータブルオブジェクトの仮定をチェックしません。一部のCライブラリがこれらを破壊する場合があります。デフォルトは "--debug" 有効時にチェックします。

```--no-debug-c-warnings```
通常 "--debug" で行われるCコンパイル時の警告チェックを無効化します。多くのパッケージで未使用値などの警告が出る場合があります。

```--unstripped```
デバッグ用に生成物のオブジェクトファイルにデバッグ情報を保持します。デフォルトはオフです。

```--profile```
vmprofによる実行時間プロファイリングを有効化します（現在は未対応）。デフォルトはオフです。

```--trace-execution```
実行前に各行のコードを出力します。デフォルトはオフです。

```--xml=XML_FILENAME```
最適化結果などの内部プログラム構造をXML形式で指定ファイルに出力します。

```--experimental=FLAG```
「実験的」な機能を有効化します。該当する機能がコード内に存在する場合のみ効果があります。詳細はソース内のタグを参照してください。

```--low-memory```
Cコンパイルの並列数を減らすなどしてメモリ使用量を抑えます。組み込み機器やメモリ不足時に使用してください。デフォルトはオフです。

```--create-environment-from-report=CREATE_ENVIRONMENT_FROM_REPORT```
'--report=compilation-report.xml' などで生成したレポートファイルから新しい仮想環境を指定パスに作成します。デフォルトは実行しません。

```--generate-c-only```
Cソースコードのみ生成し、バイナリやモジュールへのコンパイルは行いません。デバッグやカバレッジ解析用です。デフォルトはオフです。

---

### Nuitka開発用機能

```--devel-missing-code-helpers```
型情報を活用できるコードヘルパーが存在しない場合に警告を出します。最適化改善の機会を特定するのに役立ちます。デフォルトはFalseです。

```--devel-missing-trust```
信頼できるインポートが未対応の場合に警告を出します。静的最適化の改善機会を特定するのに役立ちます。デフォルトはFalseです。

```--devel-recompile-c-only```
Nuitka開発用。既存のCファイルを再コンパイルします。Pythonソースの解析結果から対象ファイルを決定します。

```--devel-internal-graph```
最適化処理の内部グラフを生成します。小規模なテストケースでのみ使用してください。デフォルトはオフです。

---

### バックエンドCコンパイラ選択

```--clang```
clangの使用を強制します。WindowsではVisual Studioが必要です。デフォルトはオフです。

```--mingw64```
WindowsでMinGW64の使用を強制します。MSYS2+MinGW Python利用時以外はデフォルトはオフです。

```--msvc=MSVC_VERSION```
Windowsで特定バージョンのMSVCを強制使用します。例: "14.3"（MSVC 2022）、"list"でインストール済み一覧、"latest"で最新版。デフォルトは最新版MSVC、なければMinGW64。

```--jobs=N```
Cコンパイラの並列ジョブ数を指定します。負の値はCPU数から減算。デフォルトは全CPU数（low-memory時は1）。

```--lto=choice```
リンク時最適化（LTO）を有効化します（MSVC, gcc, clang対応）。"yes"、"no"、"auto"（既知の場合のみ有効）から選択。デフォルトは"auto"。

```--static-libpython=choice```
Pythonの静的リンクライブラリを使用します。"yes"、"no"、"auto"から選択。デフォルトは"auto"。

```--cf-protection=PROTECTION_MODE```
gcc専用。gccの "cf-protection" モードを選択します。デフォルト"auto"はgccの既定値。詳細はgccの"-fcf-protection"ドキュメント参照。

---

### キャッシュ制御

```--disable-cache=DISABLED_CACHES```
指定したキャッシュを無効化します。"all"指定で全キャッシュ無効。利用可能: "all","ccache","bytecode","compression","dll-dependencies"。複数指定可。デフォルトはなし。

```--clean-cache=CLEAN_CACHES```
指定したキャッシュを実行前にクリアします。"all"指定で全キャッシュクリア。利用可能: "all","ccache","bytecode","compression","dll-dependencies"。複数指定可。デフォルトはなし。

```--force-dll-dependency-cache-update```
DLL依存関係キャッシュを強制更新します。配布フォルダ作成に時間がかかりますが、キャッシュが原因のエラー時などに使用します。

---

### PGO（プロファイルガイド最適化）関連

```--pgo-c```
Cレベルのプロファイルガイド最適化（PGO）を有効化します。専用ビルドでプロファイリング実行後、その結果をCコンパイルに反映します。実験的機能で、スタンドアロンモードでは未対応。デフォルトはオフです。

```--pgo-args=PGO_ARGS```
PGOプロファイリング実行時に渡す引数。デフォルトは空です。

```--pgo-executable=PGO_EXECUTABLE```
プロファイル情報収集時に実行するコマンド。スクリプト経由で起動する場合のみ指定。デフォルトは生成されたプログラムを使用。

---

### トレース機能

```--report=REPORT_FILENAME```
モジュール、データファイル、コンパイル、プラグインなどの詳細をXML形式でレポート出力します。問題報告時にも非常に便利です。このレポートを使って `--create-environment-from-report` で環境を再現することもできますが、多くの情報が含まれます。デフォルトはオフです。

```--report-diffable```
レポートを差分比較しやすい形式で出力します（実行ごとに変わるタイミングやメモリ使用量などを除外）。デフォルトはオフです。

```--report-user-provided=KEY_VALUE```
任意のデータを 'key=value' 形式でレポートに含めます。複数回指定可能です。例: `--report-user-provided=pipenv-lock-hash=64a5e4` など。デフォルトは空です。

```--report-template=REPORT_DESC```
テンプレートを使ってレポートを出力します。'template.rst.j2:output.rst' のようにテンプレートと出力ファイルを指定します。組み込みテンプレートについてはユーザーマニュアルを参照してください。複数回指定可能。デフォルトは空です。

```--quiet```
すべての情報出力を無効化し、警告のみ表示します。デフォルトはオフです。

```--show-scons```
CビルドバックエンドのSconsを詳細表示で実行し、コマンドや検出されたコンパイラを表示します。デフォルトはオフです。

```--no-progressbar```
進捗バーを無効化します。デフォルトはオフです。

```--show-progress```
進捗情報や統計を表示します（進捗バーを無効化）。非推奨。デフォルトはオフです。

```--show-memory```
メモリ情報や統計を表示します。デフォルトはオフです。

```--show-modules```
含まれるモジュールやDLLの情報を表示します（非推奨: 代わりに `--report` を推奨）。デフォルトはオフです。

```--show-modules-output=PATH```
`--show-modules` の出力先ファイル名を指定します。デフォルトは標準出力です。

```--verbose```
最適化などの詳細な処理内容を出力します。大量になる場合があります。デフォルトはオフです。

```--verbose-output=PATH```
`--verbose` の出力先ファイル名を指定します。デフォルトは標準出力です。

---

### 一般的なOS制御

```--force-stdout-spec=FORCE_STDOUT_SPEC```
プログラムの標準出力を指定した場所に強制的に出力します。コンソールが無効なプログラムやWindows Services Plugin利用時に便利です。デフォルトは無効。例: `{PROGRAM_BASE}.out.txt`（プログラムと同じ場所に出力）。詳細はユーザーマニュアル参照。

```--force-stderr-spec=FORCE_STDERR_SPEC```
プログラムの標準エラー出力を指定した場所に強制的に出力します。用途や指定方法は上記と同様です。

---

### Windows固有の制御

```--windows-console-mode=CONSOLE_MODE```
コンソールモードを選択します。デフォルトは 'force'（新しいコンソールウィンドウを作成）。'disable' でコンソールを作成・使用せず、'attach' で既存のコンソールを利用、'hide' で新規コンソールを非表示にします。デフォルトは 'force' です。

```--windows-icon-from-ico=ICON_PATH```
実行ファイルにアイコンを追加します。複数回指定可能。複数アイコンが含まれる場合は `#<n>` でインデックス指定も可能です。

```--windows-icon-from-exe=ICON_EXE_PATH```
既存の実行ファイルからアイコンをコピーします（Windowsのみ）。

```--onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE```
Windowsのonefileモードで、アプリ起動時にスプラッシュ画像を表示します。デフォルトはオフです。

```--windows-uac-admin```
実行時に管理者権限を要求します（Windowsのみ）。デフォルトはオフです。

```--windows-uac-uiaccess```
リモートデスクトップアクセスや特定フォルダからの実行を強制します（Windowsのみ）。デフォルトはオフです。

---

### macOS固有の制御

```--macos-create-app-bundle```
macOS用にバンドル（.app）を作成します。これによりコンソール無効化や高DPIグラフィックなどが利用可能になります（スタンドアロンモードを暗黙的に有効化）。デフォルトはオフです。

```--macos-target-arch=MACOS_TARGET_ARCH```
ターゲットとするアーキテクチャを指定します。デフォルトは実行中のPythonのアーキテクチャ（"native"）。

```--macos-app-icon=ICON_PATH```
アプリバンドル用のアイコンを追加します。1回のみ指定可能。デフォルトはPythonアイコン。

```--macos-signed-app-name=MACOS_SIGNED_APP_NAME```
macOS署名用のアプリ名を指定します。例: "com.YourCompany.AppName" のようにグローバルで一意な名前を推奨。

```--macos-app-name=MACOS_APP_NAME```
macOSバンドル情報で使用する製品名を指定します。デフォルトはバイナリのファイル名。

```--macos-app-mode=APP_MODE```
アプリバンドルのモードを指定します。デフォルトの "gui" はウィンドウ表示とDock表示を行います。"background" はウィンドウなし、"ui-element" はDock非表示で後からウィンドウ表示可能。

```--macos-sign-identity=MACOS_APP_VERSION```
署名時に使用するIDを指定します。デフォルトは "ad-hoc"。インストール済みIDが1つだけなら "auto" で自動検出。署名はmacOSで必須です。

```--macos-sign-notarization```
AppleのTeamID署名IDでノータリゼーション用署名を行う場合に使用します。

```--macos-app-version=MACOS_APP_VERSION```
macOSバンドル情報で使用する製品バージョンを指定します。デフォルトは "1.0"。

```--macos-app-protected-resource=RESOURCE_DESC```
macOSの保護リソース（例: マイク、カメラ等）へのアクセス権を要求します。書式は "NSMicrophoneUsageDescription:マイク録音のためのアクセス" のように、コロン区切りで説明文を付与します。複数回指定可能。詳細は https://developer.apple.com/documentation/bundleresources/information_property_list/protected_resources を参照。デフォルトは空です。

---

### Linux固有の制御

```--linux-icon=ICON_PATH```
onefileバイナリで使用する実行ファイルのアイコンを追加します。1回のみ指定可能です。デフォルトはPythonアイコン（利用可能な場合）です。

---

### バイナリのバージョン情報

```--company-name=COMPANY_NAME```
バージョン情報で使用する会社名を指定します。デフォルトは未使用です。

```--product-name=PRODUCT_NAME```
バージョン情報で使用する製品名を指定します。デフォルトはバイナリのファイル名です。

```--file-version=FILE_VERSION```
バージョン情報で使用するファイルバージョンを指定します。最大4つの数字（例: 1.0 または 1.0.0.0）で構成してください。文字列は使用できません。デフォルトは未使用です。

```--product-version=PRODUCT_VERSION```
バージョン情報で使用する製品バージョンを指定します。ファイルバージョンと同じルールです。デフォルトは未使用です。

```--file-description=FILE_DESCRIPTION```
バージョン情報で使用するファイルの説明を指定します。現在はWindowsのみ対応。デフォルトはバイナリのファイル名です。

```--copyright=COPYRIGHT_TEXT```
バージョン情報で使用する著作権表記を指定します。現在はWindows/macOSのみ対応。デフォルトは表示されません。

```--trademarks=TRADEMARK_TEXT```
バージョン情報で使用する商標を指定します。現在はWindows/macOSのみ対応。デフォルトは表示されません。

---

### プラグイン制御

```--enable-plugins=PLUGIN_NAME```
有効化するプラグイン名を指定します。'--plugin-list' で利用可能なプラグイン一覧を表示できます。デフォルトは空です。

```--disable-plugins=PLUGIN_NAME```
無効化するプラグイン名を指定します。'--plugin-list' で利用可能なプラグイン一覧を表示できます。標準プラグインの多くは無効化しないことを推奨します。デフォルトは空です。

```--user-plugin=PATH```
ユーザープラグインのファイル名を指定します。複数回指定可能です。デフォルトは空です。

```--plugin-list```
利用可能なすべてのプラグイン一覧を表示して終了します。デフォルトはオフです。

```--plugin-no-detection```
プラグインの自動検出機能を無効化します。どのプラグインを使うか確定している場合に、検出処理を省略してコンパイルを高速化できます。デフォルトはオフです。

```--module-parameter=MODULE_PARAMETERS```
モジュールパラメータを指定します。一部のパッケージで追加の指定が必要な場合に使用します。書式例: --module-parameter=module.name-option-name=value デフォルトは空です。

```--show-source-changes=SHOW_SOURCE_CHANGES```
コンパイル前にPythonファイルへ加えられたソース変更を表示します。主にプラグインやNuitkaパッケージ設定の開発用途です。例: '--show-source-changes=numpy.**' で特定名前空間以下、'*' で全て（大量になる場合あり）。デフォルトは空です。

---

### クロスコンパイル

```--target=TARGET_DESC```
クロスコンパイルのターゲットを指定します。実験的機能で現在開発中です。現時点では '--target=wasi' のみ対応予定です。

---

### 'anti-bloat' プラグインオプション（カテゴリ: core）

```--show-anti-bloat-changes```
このプラグインによる変更内容を注釈付きで表示します。

```--noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE```
'setuptools'（および 'setuptools_scm'）のインポート時の動作を指定します。依存関係が多いため、配布物には含めないことを推奨します。

```--noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE```
'pytest'（および 'nose'）のインポート時の動作を指定します。依存関係が多いため、配布物には含めないことを推奨します。

```--noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE```
'unittest'のインポート時の動作を指定します。依存関係が多いため、配布物には含めないことを推奨します。

```--noinclude-pydoc-mode=NOINCLUDE_PYDOC_MODE```
'pydoc'のインポート時の動作を指定します。デプロイ用途では不要なコードのため、含めないことを推奨します。

```--noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE```
'IPython'のインポート時の動作を指定します。依存関係が多いため、配布物には含めないことを推奨します。

```--noinclude-dask-mode=NOINCLUDE_DASK_MODE```
'dask'のインポート時の動作を指定します。依存関係が多いため、配布物には含めないことを推奨します。

```--noinclude-numba-mode=NOINCLUDE_NUMBA_MODE```
'numba'のインポート時の動作を指定します。依存関係が多く、スタンドアロンでは現在動作しません。配布物には含めないことを推奨します。

```--noinclude-default-mode=NOINCLUDE_DEFAULT_MODE```
上記各オプションのデフォルト値（"warning"）を一括で指定できます。

```--noinclude-custom-mode=CUSTOM_CHOICES```
特定のインポート時の動作を指定します。書式は「モジュール名:動作」で、動作は "error"、"warning"、"nofollow" のいずれか。例: PyQt5:error

---

### 'playwright' プラグインオプション（カテゴリ: package-support）

```--playwright-include-browser=INCLUDE_BROWSERS```
含めるPlaywrightブラウザ名を指定します。複数回指定可能です。"all"で全てのインストール済みブラウザ、"none"で全て除外。

---

### 'spacy' プラグインオプション（カテゴリ: package-support）

```--spacy-language-model=INCLUDE_LANGUAGE_MODELS```
含めるSpacy言語モデルを指定します。複数回指定可能です。"all"で全てのダウンロード済みモデルを含めます。
