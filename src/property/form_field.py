from typing import Optional
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from . import _utils
from .form_options import form_options


class FormField:
    @staticmethod
    def _input(pos: Optional[DeltaGenerator], widget_name: str, *args, **kwargs) -> None:
        widget = getattr(st if pos is None else pos, widget_name)
        widget(*args, **kwargs)

    @staticmethod
    def AREA(label: str = "Area (in sq.ft.)", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(pos, "number_input", label, min_value=1, format="%d", key="AREA")

    @staticmethod
    def FACING(label: str = "Facing of the Property", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(pos, "selectbox", label, options=form_options.FACING, format_func=str.title, key="FACING")

    @staticmethod
    def AGE(label: str = "Age of Property", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(pos, "selectbox", label, options=form_options.AGE, format_func=str.title, key="AGE")

    @staticmethod
    def FURNISH(label: str = "Furnishing Status", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(pos, "selectbox", label, options=form_options.FURNISH, format_func=str.title, key="FURNISH")

    @staticmethod
    def BEDROOM_NUM(label: str = "Select number of Bedroom", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(
            pos,
            "selectbox",
            label,
            options=form_options.BEDROOM_NUM,  # 🛠️ Corrected: no str(x) conversion
            format_func=_utils.format_99_option,
            key="BEDROOM_NUM",
        )

    @staticmethod
    def BALCONY_NUM(label: str = "Select number of Balcony", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(
            pos,
            "selectbox",
            label,
            options=form_options.BALCONY_NUM,  # 🛠️ Corrected: no str(x) conversion
            format_func=_utils.format_99_option,
            key="BALCONY_NUM",
        )

    @staticmethod
    def FLOOR_NUM(label: str = "Select Floor type", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(pos, "selectbox", label, options=form_options.FLOOR_NUM, format_func=str.title, key="FLOOR_NUM")

    @staticmethod
    def LUXURY_CATEGORY(label: str = "Select Luxury Category", pos: Optional[DeltaGenerator] = None) -> None:
        FormField._input(
            pos,
            "selectbox",
            label,
            options=list(form_options.LUXURY_CATEGORY.keys()),
            format_func=lambda x: form_options.LUXURY_CATEGORY[x],
            key="LUXURY_CATEGORY",
        )
