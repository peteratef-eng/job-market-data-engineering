from __future__ import annotations



DESIGN_SYSTEM = {
    "mode": "light",
    "background": "#F7F5F1",
    "sidebar": "#F1EEE8",
    "surface": "#FFFFFF",
    "surface_secondary": "#F5F2EC",
    "surface_elevated": "#FFFFFF",
    "primary_text": "#16212E",
    "secondary_text": "#4B5A6B",
    "muted_text": "#6B7A8B",
    "border": "#DCD5C9",
    "accent": "#B45309",
    "accent_hover": "#92400E",
    "bright_accent": "#1E3A5F",
    "input_bg": "#FFFFFF",
    "input_text": "#16212E",
    "on_accent": "#FFFFFF",
    "tag_bg": "#F3E7D4",
    "tag_text": "#7C4A03",
    "chart_bg": "rgba(255,255,255,0)",
    "chart_grid": "#E4DFD3",
    "positive": "#0F9F6E",
    "warning": "#C2410C",
    "negative": "#B91C1C",
    "shadow": "0 12px 28px rgba(22, 33, 46, 0.08)",
    "shadow_accent": "0 10px 24px rgba(180, 83, 9, 0.18)",
    "hover": "#F3E7D4",
    "disabled": "#D4CDC0",
    "palette": ["#B45309", "#1E3A5F", "#0F9F6E", "#6B7A8B", "#92400E", "#334155"],
}


def current_theme() -> dict[str, str]:
    return DESIGN_SYSTEM
