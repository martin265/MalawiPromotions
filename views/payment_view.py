import flet as ft
from config.config import supabase


class PaymentView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/payment")
        self.page = page
        self.all_artists = ft.Column([])
        self.artist_details = ft.Text()
        self.page.auto_scroll = True
        self.controls = [
            ft.SafeArea(
                maintain_bottom_view_padding=True,
                adaptive=True,
                content=ft.Column(
                    height=self.page.height,
                    scroll=ft.ScrollMode.ADAPTIVE,

                    controls=[
                        ft.Container(
                            adaptive=True,
                            gradient=ft.LinearGradient(
                                colors=[
                                    ft.colors.SURFACE_VARIANT,
                                    ft.colors.SURFACE_VARIANT
                                ],
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_center
                            ),
                            border_radius=ft.border_radius.all(10),
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        adaptive=True,
                                        margin=ft.margin.all(10),
                                        content=ft.Row(
                                            controls=[
                                                ft.IconButton(
                                                    bgcolor="#212121",
                                                    icon_size=30,
                                                    icon=ft.icons.ARROW_BACK_ROUNDED,
                                                    on_click=self.view_pop,
                                                    icon_color="white"
                                                )
                                            ]
                                        )
                                    ),

                                    # ============ container for the page header will be here ======= //
                                    ft.Container(
                                        padding=ft.padding.only(top=30, bottom=20),
                                        adaptive=True,
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text(
                                                    "check out artists".capitalize(),
                                                    size=30,
                                                    weight=ft.FontWeight.BOLD,
                                                    color="#212121",

                                                )
                                            ]
                                        )
                                    ),

                                ]
                            )
                        ),

                        # ================ // container for the details here ===== //
                        ft.Container(
                            margin=ft.margin.only(top=10, bottom=10),
                            content=ft.Column(
                                controls=[
                                    self.all_artists
                                ]
                            )
                        )
                    ]
                )
            )
        ]


    def view_pop(self, e):
        """the function to pop out the views will be here"""
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


