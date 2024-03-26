import flet as ft
from cards.homepageCards.payment_card import PaymentCard
from cards.homepageCards.eventsCard import EventsCard
from cards.homepageCards.artist_card import ArtistCard


class HomePage(ft.Container):
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

        #  ==================== // importing the different page cards here ====== //
        self.payments_cards = PaymentCard(page=page)
        self.events_card = EventsCard(page=page)
        self.artist_card = ArtistCard(page=page)
        #  ========== // the content for the page will be here ========= //
        self.content = ft.SafeArea(
            adaptive=True,
            content=ft.Column(
                controls=[
                    # =========== the container for the landing page here ======= //
                    ft.Container(
                        margin=ft.margin.only(top=20),
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
                                #  ====container for the top text here =====//
                                ft.Container(
                                    margin=ft.margin.all(10),
                                    adaptive=True,
                                    content=ft.Image(
                                        expand=True,
                                        src="https://images.pexels.com/photos/1587927/pexels-photo-1587927.jpeg"
                                            "?auto=compress&cs=tinysrgb&w=600",
                                        border_radius=ft.border_radius.all(10),

                                    ),
                                ),
                                #  =========== container for the text
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            #  =========== // container for the text ==== //
                                            ft.Container(
                                                margin=ft.margin.only(top=20),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            "music entertainers".title(),
                                                            font_family="manrop-bold",
                                                            size=20,
                                                            weight=ft.FontWeight.BOLD,
                                                            color="#412728"
                                                        )
                                                    ]
                                                )
                                            ),

                                            ft.Container(
                                                margin=ft.margin.only(15),
                                                content=ft.Row(
                                                    wrap=True,
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.SafeArea(
                                                            maintain_bottom_view_padding=True,
                                                            content=ft.Text(
                                                                "malawi music entertainers promotions"
                                                                "is a malawian based entertainment group that"
                                                                "helps in promoting and improving the "
                                                                "entertainment industry in Malawi".capitalize(),
                                                                font_family="manrop-bold",
                                                                color="#412728",
                                                                size=16,
                                                                text_align=ft.TextAlign.CENTER
                                                            )
                                                        ),

                                                    ]
                                                )
                                            ),

                                            # ================= the divider for the cards ========= //
                                            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                                            # ================ container for the icons will be here ========= //
                                        ]
                                    )
                                )
                            ]
                        )
                    ),

                    ft.Divider(height=5, color=ft.colors.TRANSPARENT),

                    # ============ // container for the other cards will be here ======= //
                    ft.Container(
                        padding=ft.padding.only(left=10),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "features".title(),
                                    font_family="manrope-bold",
                                    color="#412728",
                                    style=ft.TextStyle(
                                        size=20,
                                    )
                                )
                            ]
                        )
                    ),

                    # =================== // =================== //
                    ft.SafeArea(
                        content=ft.Row(
                            scroll=ft.ScrollMode.HIDDEN,
                            controls=[
                                self.payments_cards,
                                self.events_card,
                                self.artist_card
                            ]
                        )
                    )

                ]
            )
        )
