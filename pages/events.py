import flet as ft
from config.config import supabase


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.all_events = ft.Column([])

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
                                                weight=ft.FontWeight.W_500,
                                                color="#0078D9"
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

    def fetch_all_events(self):
        """function will be used to fetch the records from the database here"""
        try:
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
                                    "#0078D9",
                                    "#009CDC"
                                ],
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_center
                            ),
                            border_radius=ft.border_radius.all(8),
                            content=ft.Column(
                                controls=[
                                    # ========= container for the icon will be here ==== //
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.CALENDAR_MONTH_ROUNDED
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
