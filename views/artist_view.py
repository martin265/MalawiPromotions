import flet as ft


class ArtistPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/artist")
        self.controls.append(
            ft.SafeArea(
                adaptive=True,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK_ROUNDED,
                                        on_click=self.view_pop
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        )

    def view_pop(self, e):
        """the function to pop out the views will be here"""
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)