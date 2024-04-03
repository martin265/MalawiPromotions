import flet as ft
from config.config import supabase
import time


class PaymentView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/payment")
        self.page = page
        self.all_artists = ft.Column([])
        self.artist_details = ft.Text()
        self.page.auto_scroll = True
        self.current_id = ft.Text()
        self.events_page = EventsPage(page=page)
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
                                    self.all_artists
                                ]
                            )
                        )
                    ]
                )
            )
        ]
        self.fetch_current_id()

    def view_pop(self, e):
        """the function to pop out the views will be here"""
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def fetch_current_id(self):
        self.current_id = self.events_page.current_id
        print(self.current_id)


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.all_events = ft.Column([])
        self.fetch_all_events()
        self.current_id = ft.Text()
        self.page.on_route_change = self.router
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
                                                                on_click=lambda e: self.page.go("/payment")
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
        print(f"{self.current_id}")

    def router(self, route):
        """the button"""
        if self.page.route == "/payment":
            payment_view = PaymentView(page=self.page)
            self.page.views.append(payment_view)

        self.page.update()
