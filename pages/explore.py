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
                                            )
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
                                )
                            ]
                        )
                    )
                ]
            )
        )
