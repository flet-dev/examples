import flet
from flet import Container, GestureDetector, Page, TapEvent, colors


def main(page: Page):

    gd = GestureDetector(
        Container(bgcolor=colors.GREEN, width=200, height=200),
        hover_interval=50,
        on_tap=lambda e: print("TAP"),
        on_tap_down=lambda e: print(
            f"TAP DOWN - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_tap_up=lambda e: print(
            f"TAP UP - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_secondary_tap=lambda e: print("SECONDARY TAP"),
        on_secondary_tap_down=lambda e: print(
            f"SECONDARY TAP DOWN - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_secondary_tap_up=lambda e: print(
            f"SECONDARY TAP UP - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_long_press_start=lambda e: print(
            f"LONG PRESS START - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}"
        ),
        on_long_press_end=lambda e: print(
            f"LONG PRESS END - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, vx: {e.velocity_x}, vy: {e.velocity_y}"
        ),
        on_secondary_long_press_start=lambda e: print(
            f"SECONDARY LONG PRESS START - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}"
        ),
        on_secondary_long_press_end=lambda e: print(
            f"SECONDARY LONG PRESS END - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, vx: {e.velocity_x}, vy: {e.velocity_y}"
        ),
        on_double_tap=lambda e: print("DOUBLE TAP"),
        on_double_tap_down=lambda e: print(
            f"DOUBLE TAP DOWN - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_pan_start=lambda e: print(
            f"PAN START - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_pan_update=lambda e: print(
            f"PAN UPDATE - dx: {e.delta_x}, dy: {e.delta_y}, gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}"
        ),
        on_pan_end=lambda e: print(
            f"PAN END - pv: {e.primary_velocity}, vx: {e.velocity_x}, vy: {e.velocity_y}"
        ),
        on_hover=lambda e: print(
            f"HOVER - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_enter=lambda e: print(
            f"ENTER - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_exit=lambda e: print(
            f"EXIT - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
    )

    page.add(gd)


flet.app(target=main)
