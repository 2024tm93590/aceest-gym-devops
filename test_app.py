from app import ACEestApp
import tkinter as tk

def test_programs_exist():
    root = tk.Tk()
    root.withdraw()   # prevents window opening
    app = ACEestApp(root)

    assert "Fat Loss (FL)" in app.programs
    assert "Muscle Gain (MG)" in app.programs
    assert "Beginner (BG)" in app.programs