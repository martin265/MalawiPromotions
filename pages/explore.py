import flet as ft


class Explore(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.adaptive = True
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.fonts = {
            "manrope-bold": "fonts/Manrope/static/Manrope-Bold.ttf",
            "Manrope-Light": "assets/fonts/Manrope/static/Manrope-Light.ttf",
            "Manrope-SemiBold": "assets/fonts/Manrope/static/Manrope-SemiBold.ttf",
            "Manrope-Regular": "assets/fonts/Manrope/static/Manrope-Regular.ttf"
        }

        # ============= adding the page controls here ============= //
        self.content = ft.SafeArea(
            adaptive=True,
            content=ft.Column(
                controls=[
                    # =========== the container for all features ============ //
                    ft.ResponsiveRow(
                        adaptive=True,
                        controls=[
                            ft.Container(
                                bgcolor="blue",
                                content=ft.Text("Explore")
                            ),
                            ft.Container(
                                bgcolor="black",
                                content=ft.Text("Explore")
                            )
                        ]
                    )
                ]
            )
        )
