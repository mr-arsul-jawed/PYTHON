import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def copy_folders():
    main_path = entry_main.get().strip()
    dest_path = entry_dest.get().strip()
    year = entry_year.get().strip()
    folders_input = entry_folders.get().strip()

    if not all([main_path, dest_path, year, folders_input]):
        messagebox.showerror("Error", "All fields are required!")
        return

    folder_numbers = [f.strip() for f in folders_input.split(",")]

    destination_year_folder = os.path.join(dest_path, year)
    os.makedirs(destination_year_folder, exist_ok=True)

    success = []
    failed = []

    for folder in folder_numbers:
        source_folder = os.path.join(main_path, year, folder)
        destination_folder = os.path.join(destination_year_folder, folder)

        if not os.path.exists(source_folder):
            failed.append(folder)
            continue

        shutil.copytree(
            source_folder,
            destination_folder,
            dirs_exist_ok=True
        )
        success.append(folder)

    msg = ""
    if success:
        msg += "Copied folders:\n" + ", ".join(success) + "\n\n"
    if failed:
        msg += "Not found:\n" + ", ".join(failed)

    messagebox.showinfo("Result", msg if msg else "Done!")


def browse_main():
    path = filedialog.askdirectory()
    if path:
        entry_main.delete(0, tk.END)
        entry_main.insert(0, path)


def browse_dest():
    path = filedialog.askdirectory()
    if path:
        entry_dest.delete(0, tk.END)
        entry_dest.insert(0, path)


# ---------------- GUI WINDOW ----------------

root = tk.Tk()
root.title("Folder Copy Tool")
root.geometry("500x320")
root.resizable(False, False)

tk.Label(root, text="Main Folder Path").pack(pady=(10, 0))
entry_main = tk.Entry(root, width=55)
entry_main.pack()
tk.Button(root, text="Browse", command=browse_main).pack(pady=3)

tk.Label(root, text="Destination Path").pack(pady=(10, 0))
entry_dest = tk.Entry(root, width=55)
entry_dest.pack()
tk.Button(root, text="Browse", command=browse_dest).pack(pady=3)

tk.Label(root, text="Year").pack(pady=(10, 0))
entry_year = tk.Entry(root, width=20)
entry_year.pack()

tk.Label(root, text="Folder Numbers (comma-separated)").pack(pady=(10, 0))
entry_folders = tk.Entry(root, width=40)
entry_folders.pack()

tk.Button(
    root,
    text="COPY FOLDERS",
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    command=copy_folders
).pack(pady=20)

root.mainloop()
