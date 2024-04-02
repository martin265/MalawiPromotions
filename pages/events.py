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

                                # =============== // the container for the icon will be here ===== //
                                ft.Container(
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Icon(
                                                ft.icons.EVENT_AVAILABLE_ROUNDED,
                                                size=30
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


    def fetch_all_events(self):
        try:
            data, count = supabase.table("Artists").select("*").execute()
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
                            content=ft.Column(
                                controls=[

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
