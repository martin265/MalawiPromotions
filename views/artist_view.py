import flet as ft
from config.config import supabase


class ArtistPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/artist")
        self.all_artists = ft.Column([])
        self.artist_details = ft.Text()
        self.controls.append(
            ft.SafeArea(
                adaptive=True,
                content=ft.Column(
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
                                                    "check out artists".capitalize(),
                                                    size=30,
                                                    weight=ft.FontWeight.BOLD,
                                                    color="#212121",

                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),


                    ]
                )
            )
        )

        self.fetching_all_artists()

    def view_pop(self, e):
        """the function to pop out the views will be here"""
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def fetching_all_artists(self):
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


        except Exception as ex:
            print("something wrong at {}".format(ex))
