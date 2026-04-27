"""Tkinter desktop app for Tailo Typer GUI.

This GUI intentionally stays small and beginner-friendly. The conversion
itself is handled by tailo_converter.convert so the command-line and GUI paths
share the same core logic.
"""

from __future__ import annotations

from pathlib import Path
import re
import tkinter as tk
from tkinter import messagebox, ttk

try:
    from tailo_converter import convert
except ImportError:
    from src.tailo_converter import convert


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TONE_CHART_PATH = PROJECT_ROOT / "Basic-Tones_v2.png"
TONE_4_8_PATTERN = re.compile(r"\b([A-Za-z]+)([48])\b")
TONE_4_8_FINALS = ("p", "t", "k", "h")


class TaiLoTyperApp(tk.Tk):
    """Simple Windows desktop GUI for converting Tai-lo tone numbers."""

    def __init__(self) -> None:
        super().__init__()

        self.title("Tailo Typer GUI")
        self.minsize(1180, 700)
        self.tone_chart_image: tk.PhotoImage | None = None
        self.status_message = tk.StringVar(
            value="Tone 4/8 warnings will appear here after conversion."
        )

        self._build_layout()

    def _build_layout(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(5, weight=1)

        header = ttk.Label(
            self,
            text="Tailo Typer GUI",
            font=("Segoe UI", 18, "bold"),
        )
        header.grid(row=0, column=0, sticky="w", padx=16, pady=(16, 8))

        chart_frame = ttk.Frame(self, padding=(16, 0, 16, 12))
        chart_frame.grid(row=1, column=0, sticky="ew")
        chart_frame.columnconfigure(0, weight=0)
        chart_frame.columnconfigure(1, weight=1)
        self._add_tone_chart(chart_frame)
        self._add_example_panel(chart_frame)

        input_frame = ttk.Frame(self, padding=(16, 0, 16, 8))
        input_frame.grid(row=2, column=0, sticky="nsew")
        input_frame.columnconfigure(0, weight=1)
        input_frame.rowconfigure(1, weight=1)

        input_label = ttk.Label(input_frame, text="Tone-number Tai-lo")
        input_label.grid(row=0, column=0, sticky="w", pady=(0, 4))

        self.input_text = tk.Text(input_frame, wrap="word", height=8, undo=True)
        self.input_text.grid(row=1, column=0, sticky="nsew")
        self.input_text.focus_set()

        button_frame = ttk.Frame(self, padding=(16, 4, 16, 12))
        button_frame.grid(row=3, column=0, sticky="ew")
        button_frame.columnconfigure(3, weight=1)

        convert_button = ttk.Button(
            button_frame,
            text="Convert",
            command=self.convert_text,
        )
        convert_button.grid(row=0, column=0, sticky="w", padx=(0, 8))

        copy_button = ttk.Button(
            button_frame,
            text="Copy Output",
            command=self.copy_output,
        )
        copy_button.grid(row=0, column=1, sticky="w", padx=(0, 8))

        clear_button = ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_text,
        )
        clear_button.grid(row=0, column=2, sticky="w")

        output_frame = ttk.Frame(self, padding=(16, 0, 16, 16))
        output_frame.grid(row=5, column=0, sticky="nsew")
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(1, weight=1)

        output_label = ttk.Label(output_frame, text="Tone-marked Tai-lo")
        output_label.grid(row=0, column=0, sticky="w", pady=(0, 4))

        self.output_text = tk.Text(output_frame, wrap="word", height=8)
        self.output_text.grid(row=1, column=0, sticky="nsew")

        status_label = ttk.Label(
            output_frame,
            textvariable=self.status_message,
            foreground="#7a4b00",
            wraplength=900,
            justify="left",
        )
        status_label.grid(row=2, column=0, sticky="ew", pady=(8, 0))

        self.bind("<Control-Return>", lambda _event: self.convert_text())

    def _add_tone_chart(self, parent: ttk.Frame) -> None:
        if not TONE_CHART_PATH.exists():
            ttk.Label(parent, text="Basic tones chart image not found.").grid(
                row=0,
                column=0,
                sticky="w",
            )
            return

        try:
            source_image = tk.PhotoImage(file=str(TONE_CHART_PATH))
        except tk.TclError:
            ttk.Label(parent, text="Basic tones chart could not be loaded.").grid(
                row=0,
                column=0,
                sticky="w",
            )
            return

        self.tone_chart_image = source_image

        chart_label = ttk.Label(parent, image=self.tone_chart_image)
        chart_label.grid(row=0, column=0, sticky="w")

    def _add_example_panel(self, parent: ttk.Frame) -> None:
        example_input = "ta2 si7 kap4 sih8 ta4 a8"
        example_output = convert(example_input)

        example_frame = ttk.LabelFrame(parent, text="Example", padding=12)
        example_frame.grid(row=0, column=1, sticky="nw", padx=(16, 0))
        example_frame.columnconfigure(0, weight=1)

        input_heading = ttk.Label(example_frame, text="Type numbers to indicate tones:")
        input_heading.grid(row=0, column=0, sticky="w")

        input_value = ttk.Label(
            example_frame,
            text=example_input,
            font=("Segoe UI", 13, "bold"),
        )
        input_value.grid(row=1, column=0, sticky="w", pady=(2, 12))

        output_heading = ttk.Label(example_frame, text="Output:")
        output_heading.grid(row=2, column=0, sticky="w")

        output_value = ttk.Label(
            example_frame,
            text=example_output,
            font=("Segoe UI", 13, "bold"),
        )
        output_value.grid(row=3, column=0, sticky="w", pady=(2, 12))

        warning_note = ttk.Label(
            example_frame,
            text=(
                "Tone 4 and tone 8 usually need a syllable ending in "
                "p, t, k, or h. The app warns about forms like ta4 or a8."
            ),
            wraplength=250,
            justify="left",
        )
        warning_note.grid(row=4, column=0, sticky="w")

    def convert_text(self) -> None:
        input_value = self.input_text.get("1.0", "end-1c")
        converted_value = convert(input_value)

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", converted_value)
        self._update_validation_status(input_value)

    def _update_validation_status(self, input_value: str) -> None:
        warnings = self._find_tone_4_8_warnings(input_value)

        if not warnings:
            self.status_message.set("No tone 4/8 warnings.")
            return

        warning_text = "Tone 4/8 check: " + "; ".join(warnings)
        self.status_message.set(warning_text)

    def _find_tone_4_8_warnings(self, input_value: str) -> list[str]:
        warnings: list[str] = []

        for match in TONE_4_8_PATTERN.finditer(input_value):
            syllable = match.group(1)
            tone_number = match.group(2)

            if syllable.lower().endswith(TONE_4_8_FINALS):
                continue

            warnings.append(
                f"'{syllable}{tone_number}' uses tone {tone_number} "
                "but does not end in p, t, k, or h"
            )

        if len(warnings) > 5:
            extra_count = len(warnings) - 5
            warnings = warnings[:5]
            warnings.append(f"and {extra_count} more")

        return warnings

    def copy_output(self) -> None:
        output_value = self.output_text.get("1.0", "end-1c")

        if not output_value:
            messagebox.showinfo("Tailo Typer GUI", "There is no output to copy yet.")
            return

        self.clipboard_clear()
        self.clipboard_append(output_value)
        self.update()
        messagebox.showinfo("Tailo Typer GUI", "Output copied to the clipboard.")

    def clear_text(self) -> None:
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.status_message.set(
            "Tone 4/8 warnings will appear here after conversion."
        )
        self.input_text.focus_set()


def main() -> None:
    app = TaiLoTyperApp()
    app.mainloop()


if __name__ == "__main__":
    main()

