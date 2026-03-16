from app import ACEestApp
import tkinter as tk

def test_program_templates_exist():
    root = tk.Tk()
    root.withdraw()   # prevents window opening

    app = ACEestApp(root)

    assert "Fat Loss" in app.program_templates
    assert "Muscle Gain" in app.program_templates
    assert "Beginner" in app.program_templates

    root.destroy()