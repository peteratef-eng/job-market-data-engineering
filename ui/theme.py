from __future__ import annotations



DESIGN_SYSTEM = {
    "mode": "light",
    "background": "#F6F8FC",
    "sidebar": "#EEF3F8",
    "surface": "#FFFFFF",
    "surface_secondary": "#F8FAFC",
    "surface_elevated": "#FFFFFF",
    "primary_text": "#0F172A",
    "secondary_text": "#475569",
    "muted_text": "#64748B",
    "border": "#D8E1EC",
    "accent": "#2563EB",
    "accent_hover": "#1D4ED8",
    "bright_accent": "#0284C7",
    "input_bg": "#FFFFFF",
    "input_text": "#0F172A",
    "on_accent": "#FFFFFF",
    "tag_bg": "#EAF2FF",
    "tag_text": "#1E3A8A",
    "chart_bg": "rgba(255,255,255,0)",
    "chart_grid": "#E2E8F0",
    "positive": "#0F9F6E",
    "warning": "#D97706",
    "negative": "#DC2626",
    "shadow": "0 12px 28px rgba(15, 23, 42, 0.07)",
    "shadow_accent": "0 10px 24px rgba(37, 99, 235, 0.18)",
    "hover": "#EAF2FF",
    "disabled": "#CBD5E1",
    "palette": ["#2563EB", "#0284C7", "#0F9F6E", "#64748B", "#D97706", "#DC2626"],
}


def current_theme() -> dict[str, str]:
    return DESIGN_SYSTEM
