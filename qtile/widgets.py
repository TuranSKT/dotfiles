from libqtile import widget
from color import colors
from utils import monitor_adapt

def get_widgets(primary=False):
    widgets = [
            widget.Spacer(
                length=monitor_adapt(primary, 3, "width"),
                background=colors["clouds"],
                ),
            widget.GroupBox(
                highlight_method="line",
                background=colors["midnight"],
                highlight_color=colors["asbestos"],
                inactive="#00000000",
                fontsize=20 if primary else 10,
                ),
            widget.Spacer(
                length=monitor_adapt(primary, 12, "width"),
                background=colors["midnight"],
                ),
            widget.Volume(
                fmt="墳 {}",
                mute_command="amixer -D pulse set Master toogle",
                fontsize=20 if primary else 10,
                background=colors["midnight"],
                ),
            widget.TextBox(
                text="  ",
                fontsize=20 if primary else 10,
                padding=0,
                background=colors["midnight"],
                foreground=colors["clouds"],
            ),
            widget.CPU(
                format = "CPU {load_percent:04}%",
                fontsize=20 if primary else 10,
                background=colors["midnight"],
                ),
            widget.TextBox(
                text="  ",
                fontsize=20 if primary else 10,
                padding=0,
                background=colors["midnight"],
                foreground=colors["clouds"],
             ),
            widget.TextBox(
                text=" ",
                fontsize=20 if primary else 10,
                padding=0,
                background=colors["midnight"],
                foreground=colors["clouds"],
            ),
            widget.Battery(
                energy_now_file="charge_now",
                energy_full_file="charge_full",
                power_now_file="current_now",
                background=colors["midnight"].,
                foreground=colors["clouds"],
                update_interval = 5,
                ),
            widget.Clock(
                format = "%I:%M %p",
                fontsize=20 if primary else 10,
                background=colors["midnight"],
                ),
            widget.Spacer(
                length=monitor_adapt(primary, 2, "width"),
                background=colors["clouds"],
                ),
            ]
    if primary:
        widgets.insert(10, widget.Systray())
    return widgets
