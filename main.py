import flet as ft
from pages.home import HomePage
from pages.events import EventsPage
from pages.explore import Explore


def main(page: ft.Page):
    page.theme_mode = "light"
    page.adaptive = True
    page.platform = ft.PagePlatform.ANDROID
    page.scroll = ft.ScrollMode.AUTO,
    page.fonts = {
        "Manrope-Bold": "fonts/Manrope/static/Manrope-Bold.ttf",
        "Manrope-Light": "fonts/Manrope/static/Manrope-Light.ttf",
        "Manrope-SemiBold": "fonts/Manrope/static/Manrope-SemiBold.ttf",
        "Manrope-Regular": "fonts/Manrope/static/Manrope-Regular.ttf"
    }
    # ======== adding the default font for the pages here ===== //
    page.theme = ft.Theme(font_family="Manrope-Bold")
    # ============= the top app bar for the app will be here ======== //
    page.appbar = ft.AppBar(
        adaptive=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        #  ============= the actions for the app bar ========= //
        actions=[
            ft.IconButton(ft.icons.SUNNY_SNOWING)
        ]
    )

    # ============= passing all the pages here ================ //
    home_page = HomePage(page=page)
    events_page = EventsPage(page=page)
    explore_page = Explore(page=page)
    main_content = ft.Column([events_page])

    # ============ transitioning the pages here ============= //
    async def selected_page_destination(e):
        """the function will navigate to the selected page"""
        try:
            if e.control.selected_index == 0:
                main_content.controls.clear()
                main_content.controls.append(
                    home_page
                )
                main_content.update()

            elif e.control.selected_index == 1:
                main_content.controls.clear()
                main_content.controls.append(events_page)
                main_content.update()

            elif e.control.selected_index == 2:
                main_content.controls.clear()
                main_content.controls.append(explore_page)
                main_content.update()

        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True

    #  =========== the bottom navigation bar for the app ======== //
    page.navigation_bar = ft.NavigationBar(
        bgcolor=ft.colors.SURFACE_VARIANT,
        label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_SHOW,
        adaptive=True,
        destinations=[
            # ========== the bottom navigation destinations =========== //
            ft.NavigationDestination(
                label="home",
                icon_content=ft.Icon(ft.icons.HOME_OUTLINED, size=30),
                selected_icon_content=ft.Icon(ft.icons.HOME_ROUNDED, size=30)
            ),
            # ========== the bottom navigation destinations =========== //
            ft.NavigationDestination(
                label="events".capitalize(),
                tooltip="events".capitalize(),
                icon_content=ft.Icon(ft.icons.CALENDAR_TODAY, size=30),
                selected_icon_content=ft.Icon(ft.icons.CALENDAR_MONTH_ROUNDED, size=30)
            ),
            # ========== the bottom navigation destinations =========== //
            ft.NavigationDestination(
                label="explore".capitalize(),
                tooltip="explore",
                icon_content=ft.Icon(ft.icons.EXPLORE_OUTLINED, size=30),
                selected_icon_content=ft.Icon(ft.icons.EXPLORE_ROUNDED, size=30)
            ),
        ],
        on_change=selected_page_destination
    )

    # ============ // updating the page controls here ====== //
    page.add(main_content, page.appbar, page.navigation_bar)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets/")
