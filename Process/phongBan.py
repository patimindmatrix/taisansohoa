import tkinter as tk
from tkinter import ttk, messagebox

class Create_PB:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới phòng ban")
        self.root.geometry("250x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_ui(frame)

    # Saving User Info
    def create_ui(self, parent_frame):
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        tenpb_label = tk.Label(user_info_frame, text="Tên phòng ban")
        tenpb_label.grid(row=2, column=0, padx=10)
        self.tenpb_entry = tk.Entry(user_info_frame)  # Make it an instance variable
        self.tenpb_entry.grid(row=3, column=0, padx=10)

        mapb_label = tk.Label(user_info_frame, text="Mã phòng ban")
        mapb_label.grid(row=0, column=0, padx=10)
        self.mapb_entry = tk.Entry(user_info_frame)  # Make it an instance variable
        self.mapb_entry.grid(row=1, column=0, padx=10)

        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def create(self):
        mapb = self.mapb_entry.get()
        tenpb = self.tenpb_entry.get()
        if not mapb or not tenpb:
            messagebox.showwarning(title="Error", message="Thông tin không được bỏ trống")
        else:
            print("Tên phòng ban:", tenpb)
