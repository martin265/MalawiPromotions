import flet as ft


class ArtistView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.content = ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("artist page")
                ]
            )
        )


class Explore(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.adaptive = True
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.artists_page = ArtistView(page=page)
        self.main_content = ft.Column([self.artists_page])
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
                    ft.Container(
                        margin=ft.margin.only(top=40),
                        gradient=ft.LinearGradient(
                            colors=[
                                ft.colors.SURFACE_VARIANT,
                                ft.colors.SURFACE_VARIANT
                            ],
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_center
                        ),
                        padding=ft.padding.all(10),
                        border_radius=ft.border_radius.all(10),
                        content=ft.Column(
                            controls=[
                                # =========== the top container for the top title ========= //
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Container(
                                                padding=ft.padding.only(bottom=20, top=20),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            "explore".capitalize(),
                                                            size=50,
                                                            color="#212121",
                                                            weight=ft.FontWeight.BOLD
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            data=1,
                                            expand=True,
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#412728",
                                                    "#7F4D3E"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_left
                                            ),
                                            border_radius=ft.border_radius.all(9),
                                            content=ft.Column(
                                                controls=[
                                                    # -========== container for the top icon
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.MUSIC_NOTE_ROUNDED,
                                                                    size=50,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    ft.Container(
                                                        margin=ft.margin.only(top=6),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "artist".capitalize(),
                                                                    size=30,
                                                                    weight=ft.FontWeight.BOLD,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            on_click=self.get_current_container

                                        ),
                                        # ================ // the other card will be here ========= //
                                        ft.Container(
                                            expand=True,
                                            data=2,
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#4B4A54",
                                                    "#2A272A"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_left
                                            ),
                                            border_radius=ft.border_radius.all(9),
                                            content=ft.Column(
                                                controls=[
                                                    # -========== container for the top icon
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.AIRPLANE_TICKET_ROUNDED,
                                                                    size=50,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    ft.Container(
                                                        margin=ft.margin.only(top=6),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "tickets".capitalize(),
                                                                    size=30,
                                                                    weight=ft.FontWeight.BOLD,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            on_click=self.get_current_container
                                        ),

                                    ]
                                ),

                                ft.Row(
                                    controls=[
                                        # ================ // the other card will be here ========= //
                                        ft.Container(
                                            margin=ft.margin.only(bottom=30),
                                            expand=True,
                                            data=3,
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#009DCE",
                                                    "#00A4F8"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_left
                                            ),
                                            border_radius=ft.border_radius.all(9),
                                            content=ft.Column(
                                                controls=[
                                                    # -========== container for the top icon
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.PAYMENT_ROUNDED,
                                                                    size=50,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    ft.Container(
                                                        margin=ft.margin.only(top=6),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "payments".capitalize(),
                                                                    size=30,
                                                                    weight=ft.FontWeight.BOLD,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            on_click=self.get_current_container
                                        ),

                                        # ============== // the other card will be here =========== //
                                        # ================ // the other card will be here ========= //
                                        ft.Container(
                                            expand=True,
                                            data=4,
                                            margin=ft.margin.only(bottom=30),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#007842",
                                                    "#00876D"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_left
                                            ),
                                            border_radius=ft.border_radius.all(9),
                                            content=ft.Column(
                                                controls=[
                                                    # -========== container for the top icon
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.CONTACT_MAIL_ROUNDED,
                                                                    size=50,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    ft.Container(
                                                        margin=ft.margin.only(top=6),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "contact".capitalize(),
                                                                    size=30,
                                                                    weight=ft.FontWeight.BOLD,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            on_click=self.get_current_container
                                        ),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

    def get_current_container(self, e):
        if e.control.data == 1:
            self.main_content.controls.append(
                ft.Text("hello")
            )
            self.main_content.update()
        elif e.control.data == 2:
            print("second container clicked")
        elif e.control.data == 3:
            print("third container clicked")
        elif e.control.data == 4:
            print("last container clicked")
