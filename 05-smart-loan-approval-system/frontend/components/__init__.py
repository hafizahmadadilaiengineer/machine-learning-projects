"""
Reusable UI components for the Smart Loan Approval frontend.

This package re-exports every component so callers can write::

    from components import render_sidebar, render_result_card
"""

from components.sidebar import render_sidebar
from components.dashboard import (
    render_hero,
    render_summary_cards,
    render_result_card,
    render_about,
)
from components.footer import render_footer

__all__ = [
    "render_sidebar",
    "render_hero",
    "render_summary_cards",
    "render_result_card",
    "render_about",
    "render_footer",
]
