import asyncio
import sys
from pathlib import Path

import uv


class UVCli:
    def __init__(self, target_dir: Path):
        self.target_dir = Path(target_dir)

    async def uv_bin(self) -> Optional[Path]:
        try:
            return Path(uv.find_uv_bin())
        except FileNotFoundError:
            main_file = getattr(sys.modules["__main__"], "__file__", None)
            if main_file is not None:
                return Path(main_file).parent / "uv.exe"
            return None

    async def sync(self) -> int:
        uv_path = await self.uv_bin()
        if uv_path is None or not uv_path.exists():
            print("uv.exeが見つかりませんでした。")
            return 1
        cmd = [str(uv_path), "sync"]
        proc = await asyncio.create_subprocess_exec(*cmd, cwd=self.target_dir)
        await proc.communicate()
        return proc.returncode

    async def run_main(self) -> int:
        uv_path = await self.uv_bin()
        if uv_path is None or not uv_path.exists():
            print("uv.exeが見つかりませんでした。")
            return 1
        cmd = [str(uv_path), "run", "main.py"]
        proc = await asyncio.create_subprocess_exec(*cmd, cwd=self.target_dir)
        await proc.communicate()
        return proc.returncode

    async def all(self) -> int:
        ret = await self.sync()
        if ret != 0:
            print("uv sync でエラーが発生しました。")
            return ret
        ret = await self.run_main()
        if ret != 0:
            print("uv run でエラーが発生しました。")
        return ret


# 例：利用方法
async def main():
    cli = UVCli(Path("your/target/dir"))
    await cli.all()


# 実行
# asyncio.run(main())
