import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Create_VBPQ:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới văn bản pháp quy")
        self.root.geometry("500x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        mavbpq = self.mavbpq_entry.get()
        tenvbpq = self.tenvbpq_entry.get()
        ngaybh = self.ngaybh_entry.get()
        nvbh =self.nvbh_combobox.get()
        nvql = self.nvql_combobox.get()
        if not mavbpq or not tenvbpq or not ngaybh or not nvbh or not nvql:
            tk.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
        else:
            print("Mã HĐ: ", "Tên HĐ: ",  "Ngày tải lên: ",  "ngày hợp đồng:")
            print("Nhân viên:  ",  "tệp: ", "đối tượng:")
            print("------------------------------------------")

    def create_ui(self, parent_frame):

        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        mavbpq_label = tk.Label(user_info_frame, text="Mã VBPQ")
        mavbpq_label.grid(row=0, column=0, padx = 10)
        self.mavbpq_entry = tk.Entry(user_info_frame)
        self.mavbpq_entry.grid(row=1, column=0, padx = 10)

        tenvbpq_label = tk.Label(user_info_frame, text="Tên VBPQ")
        tenvbpq_label.grid(row=0, column=1)
        self.tenvbpq_entry = tk.Entry(user_info_frame)
        self.tenvbpq_entry.grid(row=1, column=1)

        ngaybh_label = tk.Label(user_info_frame, text="Ngày ban hành")
        ngaybh_label.grid(row=0, column=2)
        self.ngaybh_entry = tk.Entry(user_info_frame)
        self.ngaybh_entry.grid(row=1, column=2)

        nvbh_label = tk.Label(user_info_frame, text="Nhân viên BH")
        nvbh_label.grid(row=2, column=0)
        self.nvbh_combobox = ttk.Combobox(user_info_frame, values=["NVDH001", "NVDH002","NVDH003",])
        self.nvbh_combobox.grid(row=3, column=0)

        nvql_label = tk.Label(user_info_frame, text="Nhân viên QL")
        nvql_label.grid(row=2, column=1)
        self.nvql_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002","NVNS003",])
        self.nvql_combobox.grid(row=3, column=1)

        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
