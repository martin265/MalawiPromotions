import flet as ft


class ArtistCard(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.adaptive = True
        # ============ the content for the cards =========== //
        self.content = ft.Container(
            adaptive=True,
            width=self.page.width,
            border_radius=ft.border_radius.all(8),
            gradient=ft.LinearGradient(
                colors=[
                    "#4B4A54",
                    "#2A272A"
                ],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_left
            ),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(left=30, top=30),
                                content=ft.Icon(
                                    ft.icons.MY_LIBRARY_MUSIC_ROUNDED,
                                    size=50,
                                    color="#eceff1"
                                )
                            ),

                            ft.Container(
                                padding=ft.padding.only(top=30),
                                content=ft.Text(
                                    "artist review".capitalize(),
                                    style=ft.TextStyle(
                                        size=30,
                                        color="#eceff1"
                                    )
                                )
                            )
                        ]
                    ),

                    #  ================= // the container for the text will be here ========= //
                    ft.Container(
                        adaptive=True,
                        margin=ft.margin.only(left=30, right=30, bottom=30, top=10),
                        content=ft.Row(
                            wrap=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "Your feedback matters! Share your thoughts about your experience"
                                    "and let us know how our artists have inspired, entertained, or moved you. Your "
                                    "reviews help us improve and empower our talented creators to continue delivering "
                                    "exceptional content. Thank you for being part of our community!",
                                    color="#eceff1",
                                    style=ft.TextStyle(
                                        size=18
                                    )
                                )
                            ]
                        )
                    ),

                    # ============== container for the read more here ====== //

                ]
            ),
            # ============== // the on click function ========== //
            on_click=lambda _e: print("hello world")

        )
