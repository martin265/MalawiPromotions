import flet as ft


class Events(ft.Container):
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
        # ============== // passing the controls to the page here ======== //
        self.content = ft.SafeArea(
            content=ft.Column(
                controls=[
                    # ======= container for the landing text will be here ======= //
                    ft.Container(
                        margin=ft.margin.only(top=30),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                "latest events".title(),
                                                size=30,
                                                weight=ft.FontWeight.BOLD,
                                                color="#2A272A"
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )