import flet as ft
from config.config import supabase
import time
from views.payment_view import PaymentView


# class PaymentView(ft.View):
#     def __init__(self, page: ft.Page):
#         super().__init__(route="/payment")
#         self.page = page


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.all_events = ft.Column([])
        self.fetch_all_events()
        self.page.on_route_change = self.router
        self.current_id = ft.Text()
        # ============ the controls for the page will be here ========== //
        self.content = ft.SafeArea(
            content=ft.Column(
                controls=[
                    # =========== the top container for the tabs will be here
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                # ============ // container for the
                                ft.Container(
                                    padding=ft.padding.only(top=20),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                "available events".title(),
                                                size=24,
                                                weight=ft.FontWeight.BOLD,
                                                color="#212121"
                                            )
                                        ]
                                    )
                                ),

                                # ================= the container for the events here ======== //
                                ft.Container(
                                    margin=ft.margin.only(top=20),
                                    content=ft.Column(
                                        controls=[
                                            self.all_events
                                        ]
                                    )
                                )

                            ]
                        )
                    )
                ]
            )
        )

        # ============= the input fields will be here =============== //
        self.event_name = ft.Text(
            size=20,
            color="#7F4D3E",
            weight=ft.FontWeight.BOLD
        )

        self.first_name = ft.TextField(
            width=500,
        )

        self.payment_modal = ft.AlertDialog(
            adaptive=True,
            content=ft.Container(
                expand=True,

                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "make your payment here".capitalize(),
                                        color="#412728",
                                        weight=ft.FontWeight.BOLD,
                                        size=20
                                    )
                                ]
                            )
                        ),
                        # ============== // for the icon // ================ //
                        ft.Container(
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(ft.icons.PAYMENT_ROUNDED, size=30, color="#412728")
                                ]
                            )
                        ),

                        ft.Container(
                            padding=ft.padding.only(top=30),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    self.event_name
                                ]
                            )
                        ),

                        # =============== // container for the textfield // ========== //
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    self.first_name,
                                ]
                            )
                        )
                    ]
                )
            )
        )

    def fetch_all_events(self):
        """function will be used to fetch the records from the database here"""
        try:
            time.sleep(2)
            data, count = supabase.table("Events").select("*").execute()
            # =========== checking if the data is available here ======== //
            if not data:
                print("no available records")
            else:
                data_tuple = data
                data_list = data_tuple[1]
                # first_names = [artist['first_name'] for artist in data_list]

                for element in data_list:
                    self.all_events.controls.append(
                        ft.Container(
                            adaptive=True,

                            gradient=ft.LinearGradient(
                                colors=[
                                    "#282828",
                                    "#353535"
                                ],
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_center
                            ),
                            border_radius=ft.border_radius.all(10),
                            content=ft.Column(
                                controls=[
                                    # ========= container for the icon will be here ==== //
                                    ft.Container(
                                        bgcolor="#424242",
                                        padding=ft.padding.only(top=40),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Image(
                                                    src="https://cdn-icons-png.flaticon.com/256/9292/9292417.png"
                                                )
                                            ]
                                        )
                                    ),

                                    ft.Container(
                                        padding=ft.padding.all(20),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        ft.Icon(
                                                            ft.icons.AIRPLANE_TICKET_ROUNDED,
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(
                                                            "ticket type: ".capitalize(),
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(f"{element["ticket_type"]}", color="white", size=20)
                                                    ]
                                                ),

                                                ft.Row(
                                                    controls=[
                                                        ft.Icon(
                                                            ft.icons.EVENT_AVAILABLE_ROUNDED,
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(
                                                            "event name : ".capitalize(),
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(f"{element["event_name"]}", color="white", size=20)
                                                    ]
                                                ),

                                                ft.Row(
                                                    controls=[
                                                        ft.Icon(
                                                            ft.icons.PRICE_CHECK_ROUNDED,
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(
                                                            "ticket  price: ".capitalize(),
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(f"{element["ticket_price"]}", color="white", size=20)
                                                    ]
                                                ),

                                                ft.Row(
                                                    controls=[
                                                        ft.Icon(
                                                            ft.icons.PAYMENT_ROUNDED,
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(
                                                            "payment method: ".capitalize(),
                                                            size=20,
                                                            color="white"
                                                        ),

                                                        ft.Text(f"{element["payment_method"]}", color="white", size=20)
                                                    ]
                                                ),

                                                ft.Container(
                                                    adaptive=True,
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.ElevatedButton(
                                                                data=element,
                                                                text="purchase ticket".capitalize(),
                                                                icon=ft.icons.SHOPPING_CART_ROUNDED,
                                                                on_click=self.page.go("/payment")
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
                    )
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            'something went wrong at {}'.format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    def current_id_func(self, e):
        self.current_id = e.control.data["id"]
        self.event_name.value = e.control.data["event_name"]
        print(self.event_name.value)
        # =========== the payment modal will be shown here
        self.page.dialog = self.payment_modal
        self.payment_modal.open = True
        self.page.update()

    def router(self, route):
        """the button"""
        if self.page.route == "/payment":
            payment_view = PaymentView(page=self.page)
            self.page.views.append(payment_view)

        self.page.update()
