import tkinter as tk

# --- CONFIGURATION ---
# REMINDER_INTERVAL = 1800000  # 30 minutes in milliseconds
REMINDER_INTERVAL = 300000   # 5 minutes in milliseconds
PLANE_SPEED = 10             
PLANE_TEXT = "✈️  TIME TO STRETCH! 🧘"
# ---------------------


def launch_plane():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
  
    # Handle platform-specific transparency
    ws = root.tk.call('tk', 'windowingsystem')
    if ws == 'aqua':  # macOS
        root.config(bg="systemTransparent")
        bg_color = "systemTransparent"
    elif ws == 'x11':  # Linux
        # Enable RGBA alpha channel for true Linux transparency
        root.wait_visibility(root)
        root.wm_attributes("-alpha", 1.0)
        # Use an empty string or clear background for the canvas
        bg_color = None 
    else:  # Windows
        root.config(bg="white")
        root.wm_attributes("-transparentcolor", "white")
        bg_color = "white"

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # On Linux, we configure the window to have a transparent visual structure
    if ws == 'x11':
        try:
            root.attributes('-type', 'splash')  # Better than overrideredirect on Linux
        except tk.TclError:
            pass

    canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0)
    if bg_color:
        canvas.config(bg=bg_color)
    canvas.pack()

    start_x = -500  
    start_y = screen_height // 2
    
    plane = canvas.create_text(
        start_x, start_y, 
        text=PLANE_TEXT, 
        font=("Helvetica", 28, "bold"), 
        fill="red", 
        anchor="w"
    )

    def animate():
        nonlocal start_x
        start_x += PLANE_SPEED
        canvas.coords(plane, start_x, start_y)
        
        if start_x > screen_width:
            root.destroy()
            schedule_next_break()
        else:
            root.after(20, animate)

    animate()
    root.mainloop()

def schedule_next_break():
    dummy_root = tk.Tk()
    dummy_root.withdraw() 
    dummy_root.after(REMINDER_INTERVAL, lambda: [dummy_root.destroy(), launch_plane()])
    dummy_root.mainloop()

if __name__ == "__main__":
    print("Stretch reminder active. Close the terminal to exit.")
    schedule_next_break()
