"""
Custom bsp layout
"""

from color import colors
from libqtile import layout

bsp_layout= [
        layout.Bsp(
            margin=20,
            border_focus=colors["clouds"],
            border_normal=colors["midnight"],
            border_width=7,
        )
    ]

