import flet as ft


class ArtistPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/artist")
        self.controls.append(
            ft.SafeArea(
                adaptive=True,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK_ROUNDED,
                                        on_click={}
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        )


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
        self.artist_page = ArtistPage(page=page)
        self.page.on_route_change = self.router
        # ============= adding the page controls here ============= //
        self.content = ft.SafeArea(
            adaptive=True,
            content=ft.Column(
                controls=[
                    # =========== the container for all features ============ //
                    ft.Container(
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
                                            on_click=lambda e: self.page.go("/artist")
                                        ),
                                        # ================ // the other card will be here ========= //
                                        ft.Container(
                                            expand=True,
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
                                            )
                                        ),
                                    ]
                                ),

                                ft.Row(
                                    controls=[
                                        # ================ // the other card will be here ========= //
                                        ft.Container(
                                            expand=True,
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
                                            )
                                        ),

                                        # ============== // the other card will be here =========== //
                                        # ================ // the other card will be here ========= //
                                        ft.Container(
                                            expand=True,
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
                                            )
                                        ),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

    def router(self, route):
        """the function to loop through the page here"""
        self.page.views.clear()
        if self.page.route == "/artist":
            self.page.views.append(self.artist_page)

        self.page.update()

