import flet as ft


class PaymentCard(ft.Container):
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
                    "#353535",
                    "#353535"
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
                                    ft.icons.PAYMENT_ROUNDED,
                                    size=50,
                                    color="#eceff1"
                                )
                            ),

                            ft.Container(
                                padding=ft.padding.only(top=30),
                                content=ft.Text(
                                    "payment".capitalize(),
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
                                    "Welcome to our secure and seamless payments section! We understand the "
                                    "importance of convenience and security when it comes to "
                                    "handling"
                                    "transactions. Rest assured, your financial information "
                                    "is protected with"
                                    "state-of-the-art encryption technology",
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
