import flet as ft


async def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(title=ft.Text("Geolocator Tests"))

    def handle_position_change(e):
        page.add(ft.Text(f"New position: {e.latitude} {e.longitude}"))

    gl = ft.Geolocator(
        location_settings=ft.GeolocatorSettings(
            accuracy=ft.GeolocatorPositionAccuracy.LOW
        ),
        on_position_change=handle_position_change,
        on_error=lambda e: page.add(ft.Text(f"Error: {e.data}")),
    )
    page.overlay.append(gl)

    settings_dlg = lambda handler: ft.AlertDialog(
        adaptive=True,
        title=ft.Text("Opening Location Settings..."),
        content=ft.Text(
            "You are about to be redirected to the location/app settings. "
            "Please locate this app and grant it location permissions."
        ),
        actions=[ft.TextButton(text="Take me there", on_click=handler)],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    async def handle_permission_request(e):
        p = await gl.request_permission_async(wait_timeout=60)
        page.add(ft.Text(f"request_permission: {p}"))

    async def handle_get_permission_status(e):
        p = await gl.get_permission_status_async()
        page.add(ft.Text(f"get_permission_status: {p}"))

    async def handle_get_current_position(e):
        p = await gl.get_current_position_async()
        page.add(ft.Text(f"get_current_position: ({p.latitude}, {p.longitude})"))

    async def handle_get_last_known_position(e):
        p = await gl.get_last_known_position_async()
        page.add(ft.Text(f"get_last_known_position: ({p.latitude}, {p.longitude})"))

    async def handle_location_service_enabled(e):
        p = await gl.is_location_service_enabled_async()
        page.add(ft.Text(f"is_location_service_enabled: {p}"))

    async def handle_open_location_settings(e):
        p = await gl.open_location_settings_async()
        page.close(location_settings_dlg)
        page.add(ft.Text(f"open_location_settings: {p}"))

    async def handle_open_app_settings(e):
        p = await gl.open_app_settings_async()
        page.close(app_settings_dlg)
        page.add(ft.Text(f"open_app_settings: {p}"))

    location_settings_dlg = settings_dlg(handle_open_location_settings)
    app_settings_dlg = settings_dlg(handle_open_app_settings)

    page.add(
        ft.Row(
            wrap=True,
            controls=[
                ft.OutlinedButton(
                    "Request Permission",
                    on_click=handle_permission_request,
                ),
                ft.OutlinedButton(
                    "Get Permission Status",
                    on_click=handle_get_permission_status,
                ),
                ft.OutlinedButton(
                    "Get Current Position",
                    on_click=handle_get_current_position,
                ),
                ft.OutlinedButton(
                    "Get Last Known Position",
                    visible=False if page.web else True,
                    on_click=handle_get_last_known_position,
                ),
                ft.OutlinedButton(
                    "Is Location Service Enabled",
                    on_click=handle_location_service_enabled,
                ),
                ft.OutlinedButton(
                    "Open Location Settings",
                    visible=False if page.web else True,
                    on_click=lambda e: page.open(location_settings_dlg),
                ),
                ft.OutlinedButton(
                    "Open App Settings",
                    visible=False if page.web else True,
                    on_click=lambda e: page.open(app_settings_dlg),
                ),
            ],
        )
    )


ft.app(main)
