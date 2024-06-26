import flet as ft
from config.config import supabase


class PaymentView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/payment")
        self.page = page
        self.page.auto_scroll = True
        self.events_page = EventsPage(page=page)
        print(self.events_page.get_current_id)
        # ============ calling the other class here ========== //
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
                                                    "buy ticket".capitalize(),
                                                    size=30,
                                                    weight=ft.FontWeight.BOLD,
                                                    color="#412728",

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


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.all_events = ft.Column([])
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

        self.fetch_all_events()

        self.main_content = ft.Column([])

        # =============== the input fields for the client ========== //
        self.first_name = ft.TextField(
            label="first name".capitalize(),
            hint_text="enter first name",
            keyboard_type=ft.KeyboardType.TEXT,
            border_radius=ft.border_radius.all(20)
        )

        self.last_name = ft.TextField(
            label="last name".capitalize(),
            hint_text="enter last name",
            keyboard_type=ft.KeyboardType.TEXT
        )

        self.age = ft.TextField(
            label="age".capitalize(),
            hint_text="enter your age",
            keyboard_type=ft.KeyboardType.NUMBER
        )

        self.username = ft.TextField(
            label="first name".capitalize(),
            hint_text="enter first name",
            keyboard_type=ft.KeyboardType.TEXT
        )

        self.email = ft.TextField(
            label="email".capitalize(),
            hint_text="enter your email",
            keyboard_type=ft.KeyboardType.EMAIL
        )

    def fetch_all_events(self):
        """function will be used to fetch the records from the database here"""
        try:
            data, count = supabase.table("Events").select("*").execute()
            # =========== checking if the data is available here ======== //
            if not data:
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "No available events"
                            )
                        ]
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()
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
                                                                on_click=self.get_current_id
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
            payment_dialog = ft.AlertDialog(
                content=ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "no internet connection".capitalize(),
                                weight=ft.FontWeight.BOLD,
                                size=20,
                            ),

                            ft.Icon(
                                ft.icons.ERROR_ROUNDED,
                                color="red"
                            )
                        ]
                    )
                )
            )
            self.page.dialog = payment_dialog
            payment_dialog.open = True
            self.page.update()

    def router(self, e):
        if self.page.route == "/payment":
            payment = PaymentView(page=self.page)
            self.page.views.append(payment)

        self.page.update()

    def get_current_id(self, e):
        self.current_id = e.control.data["id"]
        if self.current_id:
            self.page.go("/payment")
            return self.current_id







