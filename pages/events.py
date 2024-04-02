import flet as ft


class EventsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        # ============ the controls for the page will be here ========== //
        self.content = ft.SafeArea(
            content=ft.Column(
                controls=[
                    # =========== the top container for the tabs will be here
                    ft.Container(
                        content=ft.Row(

                        )
                    )
                ]
            )
        )
