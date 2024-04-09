import tkinter as tk
import subprocess
import os
import time
import shutil
import webbrowser

def play_game():
    file_path = os.path.expanduser("~/AppData/Local/Bloxstrap/Modifications/ClientSettings/ClientAppSettings.json")

    # Check if the ClientAppSettings.json file exists
    if not os.path.exists(file_path):
        # Run the Bloxstrap installer
        subprocess.run(r".\CodeStuff/bloxstrapinstall.exe")

    # Wait for the file to exist
    while not os.path.exists(file_path):
        print("File does not exist yet. Waiting...")
        time.sleep(1)

    # Copy the local file to the correct directory
    local_file_path = os.path.join(os.getcwd(), "CodeStuff/ClientAppSettings.json")
    if os.path.exists(local_file_path):
        shutil.copy(local_file_path, file_path)
        print(f"File '{local_file_path}' copied to '{file_path}'.")
    else:
        print(f"Local file '{local_file_path}' does not exist.")

    # Open the Roblox place using the roblox:// URL scheme
    url = "roblox://placeid=7390193918"
    webbrowser.open(url)

    # Run the udp-reverse-proxy executable
    udp_reverse_proxy_path = os.path.join(os.getcwd(), "CodeStuff/udp-reverse-proxy.exe")
    if os.path.exists(udp_reverse_proxy_path):
        args = [udp_reverse_proxy_path, "localhost:53640", "147.185.221.16:40033"]
        subprocess.run(args, shell=True)
    else:
        print(f"Executable '{udp_reverse_proxy_path}' does not exist.")

root = tk.Tk()
root.geometry("634x487")
root.config(bg="#2f2f2f")
root.overrideredirect(True)

# Calculate the x and y coordinates for the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (634 // 2)
y = (screen_height // 2) - (487 // 2)

# Move the window to the center of the screen
root.geometry(f"+{x}+{y}")

# Create a semi-transparent color
color = "#992f99" # RGB color with alpha value of 50% (transparent)

# Create a semi-transparent image
image = tk.PhotoImage(width=1, height=1)
image.put(color, to=(0, 0, 1, 1))

# Create a canvas with the semi-transparent rectangle
canvas = tk.Canvas(root, width=634, height=487, bg="#2f2f2f", highlightthickness=0)
canvas.pack_propagate(0)
canvas.pack()
canvas.create_rectangle(0, 0, 634, 487, fill="#2f2f2f", stipple="gray50")

# Create an image object with the semi-transparent color
image_obj = canvas.create_image(0, 0, image=image, anchor="nw")

# Create a text object with the semi-transparent color
text = "ROCE X"
font_size = 62
x = 317
y = 100

text_layer = canvas.create_text(x, y, text=text, font=("Arial", font_size, "bold"), fill=color, anchor="center")

container = tk.Frame(root, bg="#2f2f2f", borderwidth=0, relief="flat", width=634, height=487)
container.pack_propagate(0)
container.place(x=0, y=0)

text_1 = tk.Label(container, text="ROCE X", font=("Arial", 72, "bold"), fg="#383838", bg="#2f2f2f", anchor="center")
text_1.place(relx=0.5, rely=0.3, anchor="center")

discord_link = tk.Label(container, text="https://discord.gg/rosex", font=("Arial", 7, "bold"), fg="#5A5A5A", bg="#2f2f2f", anchor="center")
discord_link.place(relx=0.5, rely=0.4, anchor="center")

button_area = tk.Frame(container, bg="#444444", width=221, height=70, borderwidth=0, relief="flat")
button_area.place(relx=0.5, rely=0.6, anchor="center")

button = tk.Button(button_area, text="P L A Y", font=("Arial", 31, "bold"), fg="#ffffff", bg="#2f2f2f", activebackground="#ffffff", borderwidth=0, cursor="hand2", command=play_game)
button.pack(fill="both", expand=True)

details_area = tk.Label(container, text="1.0", font=("Arial", 7, "bold"), fg="#999999", bg="#2f2f2f", anchor="center")
details_area.place(relx=1.0, rely=1.0, x=-1, y=-1, anchor="se")

warnings_area = tk.Label(container, text="Roce X condolauncher | mature contrent ahead",font=("Arial", 9, "bold"),fg="#5A5A5A", bg="#2f2f2f", anchor="center")
warnings_area.place(relx=0.5, rely=0.8, anchor="center")

close_program_area = tk.Frame(container, bg="#2f2f2f", width=17, height=17)
close_program_area.place(relx=1.0, rely=0.0, anchor="ne")

close_button = tk.Button(close_program_area, text="X", font=("Courier", 21, "bold"), fg="#ff0000", bg="#2f2f2f", borderwidth=0, highlightthickness=0, cursor="hand2", command=lambda: root.destroy())
close_button.pack()

root.mainloop()