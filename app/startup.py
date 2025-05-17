import os
import tempfile
from pathlib import Path

import yaml
from nicegui import app, ui
from nicegui.elements.expansion import Expansion


# Nuitka
async def remove_splash_feedback() -> None:
    if "NUITKA_ONEFILE_PARENT" in os.environ:
        splash_filename: Path = Path(tempfile.gettempdir()).joinpath(
            f"onefile_{int(os.environ['NUITKA_ONEFILE_PARENT'])!s}_splash_feedback.tmp",
        )

        if Path(splash_filename).exists():
            Path(splash_filename).unlink()


class Startup:
    def __init__(self) -> None:
        # add ttf
        app.add_static_file(
            local_file=Path("fonts/NotoSansJP-VariableFont_wght.ttf"),
            url_path="/NotoSansJP-VariableFont_wght.ttf",
        )
        # CSS
        ui.add_css(content=Path("css/style.css"), shared=True)

        # app.on_disconnect(handler=lambda: app.shutdown())

        ui.colors(
            primary="#1a1a1a",
            secondary="#1a1a1a",
            accent="#1a1a1a",
            dark="#1a1a1a",
            dark_page="#1a1a1a",
            positive="#1a1a1a",
            negative="#1a1a1a",
            info="#1a1a1a",
            warning="#1a1a1a",
        )

        self.current_page: str = ""

    async def startup(self) -> None:
        ui.query(selector=".nicegui-content").classes(add="w-screen h-screen p-0 gap-0")
        ui.query(selector=".nicegui-expansion .q-expansion-item__content").style("gap: 0;")

        with ui.row().classes(add="border-b w-full h-[38px] p-0 gap-0"):
            # with ui.header(bordered=True).classes(add="p-0 gap-0 bg-white").classes(add="pywebview-drag-region"):
            ui.button(text="らすく", on_click=lambda: self.show_info(), icon="sym_o_pets").props(add="flat")
            ui.space()
            ui.button(on_click=lambda: self.minimize(), icon="sym_o_minimize").props(add="flat")
            ui.button(on_click=lambda: self.toggle_fullscreen(), icon="sym_o_maximize").props(add="flat")
            ui.button(on_click=lambda: self.shutdown(), icon="sym_o_close").props(add="flat")

        with ui.row().classes(add="w-full h-[calc(100vh-38px)] p-0 gap-0 overflow-hidden"):
            with ui.column().classes(add="border-r w-[300px] h-full p-4 gap-0"):

                def link_button(text: str, icon: str, target: str) -> Expansion:
                    return (
                        ui.expansion(
                            text=text,
                            icon=icon,
                            on_value_change=lambda: self.navigate_to(target=target),
                        )
                        .props("hide-expand-icon")
                        .classes("w-full gap-0 select-none")
                    )

                def expansion(text: str, icon: str, target: str) -> Expansion:
                    return ui.expansion(
                        text=text,
                        icon=icon,
                        on_value_change=lambda: self.navigate_to(target=target),
                    ).classes("w-full select-none")

                link_button(text="ホーム", icon="sym_o_home", target="home")
                ui.separator()

                with expansion(text="お気に入り", icon="sym_o_star", target="list-"):
                    link_button(text="コード 01", icon="sym_o_code", target="/1")
                    link_button(text="コード 02", icon="sym_o_code", target="/2")

                ui.separator()

                with (
                    ui.column()
                    .classes("w-full flex-1 overflow-auto gap-0")
                    .style("scrollbar-width: none; overscroll-behavior: none;")
                ):
                    for category01 in yaml.safe_load(Path("data/yaml/projects.yaml").read_text(encoding="utf-8")):
                        ui.label(text=category01["text"]).classes("w-full p-4 text-sm text-gray-600 select-none")
                        for category02 in category01["children"]:
                            with expansion(text=category02["text"], icon="sym_o_folder", target="list-"):
                                for item in category02["children"]:
                                    link_button(text=item["text"], icon="sym_o_code", target=item["target"])

                ui.separator()
                link_button(text="開発者向け", icon="sym_o_construction", target="dev")
                link_button(text="設定", icon="sym_o_settings", target="settings")

            # content
            with ui.column() as self.content:
                self.content.classes(add="w-[calc(100vw-300px)] h-full p-4 overflow-y-auto")
                self.content.style(add="scrollbar-width: none; overscroll-behavior: none;")

        # dialog
        # info
        with ui.dialog() as self.dialog_info, ui.card():
            with ui.row(align_items="baseline"):
                ui.icon(name="sym_o_pets").classes(add="text-xl")
                ui.label(text="らすく").classes(add="text-xl")
            ui.label(text="Are you sure?")
            with ui.row():
                ui.button(text="Yes", on_click=lambda: self.dialog_info.submit(result="Yes"))
                ui.button(text="No", on_click=lambda: self.dialog_info.submit(result="No"))

        await self.navigate_to(target="home")

        await remove_splash_feedback()

    async def shutdown(self) -> None:
        if app.native.main_window is not None:
            app.shutdown()
        else:
            ui.notify(message="disabled")

    async def minimize(self) -> None:
        if app.native.main_window is not None:
            app.native.main_window.minimize()
        else:
            ui.notify(message="disabled")

    async def toggle_fullscreen(self) -> None:
        if app.native.main_window is not None:
            app.native.main_window.toggle_fullscreen()
        else:
            ui.notify(message="disabled")

    async def show_info(self) -> None:
        _ = await self.dialog_info

    async def navigate_to(self, target: str) -> None:
        if self.current_page == target:
            return

        self.content.clear()

        match target:
            case "home":
                with self.content:
                    ui.markdown(
                        content=Path("data/md/home.md").read_text(encoding="utf-8"),
                    ).classes("w-full")
                    for _ in range(100):
                        ui.label(text="Hello world!")

            case "dev":
                with self.content:
                    ui.label(text="開発者向け")

            case "settings":
                with self.content:
                    ui.label(text="設定")

            case text if text.startswith("list-"):
                with self.content:
                    ui.label(text=target).classes(add="text-2xl")
                    await self.list_codes()

            case _:
                with self.content:
                    ui.label(text=target).classes(add="text-2xl")

        self.current_page = target

    async def list_codes(self) -> None:
        # with ui.dialog().props(add="full-width full-height") as dialog, ui.card():
        #     with ui.page_sticky(position="top-right", x_offset=30, y_offset=30):
        #         ui.button(icon="close", on_click=lambda: dialog.close()).props(add="flat")

        #     ui.label(text="Hello world!")
        #     ui.input(label="Input")

        #     async def compute() -> None:
        #         n = ui.notification(timeout=None)
        #         for i in range(10):
        #             n.message = f"Computing {i / 10:.0%}"
        #             n.spinner = True
        #             await asyncio.sleep(delay=0.2)
        #         n.message = "Done!"
        #         n.spinner = False
        #         await asyncio.sleep(delay=0.1)
        #         n.dismiss()

        #     ui.button(text="compute", on_click=compute)

        for _ in range(100):
            ui.label(text="Hello world!")

        # with ui.row().classes(add="gap-4").classes(add="w-full h-full gap-0 overflow-auto"):
        #     for _ in range(10):
        #         with ui.card().classes(add="w-3xs w-3xs").on(type="click", handler=dialog.open):
        #             ui.image(source="https://picsum.photos/id/684/640/360")
        #             with ui.card_section():
        #                 ui.label(text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...")
