import flet as ft
from config.config import supabase
import time
import asyncio
import json


class FetchingEventsRecords(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  =========== the list for the records here ======== //

    def fetch_events_record(self):
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
                    print(element["last_name"])



        except Exception as ex:
            print("something wrong at {}".format(ex))


class Events(ft.Container):
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
        #  ============ all the functions will be called here ========== //
        self.fetch_records = FetchingEventsRecords(page=page)
        self.fetch_records.fetch_events_record()
        # ============== // passing the controls to the page here ======== //
        self.content = ft.SafeArea(
            content=ft.Column(
                controls=[
                    # ======= container for the landing text will be here ======= //
                    ft.Container(
                        margin=ft.margin.only(top=30),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                "latest events".title(),
                                                size=30,
                                                weight=ft.FontWeight.BOLD,
                                                color="#2A272A"
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
