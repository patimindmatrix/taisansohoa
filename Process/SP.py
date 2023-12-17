import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Create_SP:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới sản phẩm")
        self.root.geometry("500x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        masp = self.masp_entry.get()
        tensp = self.tensp_entry.get()
        dvt = self.dvt_entry.get()
        dongia = self.dg_entry.get()
        nvl = self.nvl_combobox.get()
        nvql = self.nvql_combobox.get()
        nvcr = self.nvcr_combobox.get()
        if not masp or not tensp or not dvt or not dongia or not nvql or not nvcr or not nvl:
            tk.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
        else:
            print("Mã HĐ: ", "Tên HĐ: ",  "Ngày tải lên: ",  "ngày hợp đồng:")
            print("Nhân viên:  ",  "tệp: ", "đối tượng:")
            print("------------------------------------------")

    def create_ui(self, parent_frame):

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        masp_label = tk.Label(user_info_frame, text="Mã SP")
        masp_label.grid(row=0, column=0, padx = 10)
        self.masp_entry = tk.Entry(user_info_frame)
        self.masp_entry.grid(row=1, column=0, padx = 10)

        tensp_label = tk.Label(user_info_frame, text="Tên SP")
        tensp_label.grid(row=0, column=1)
        self.tensp_entry = tk.Entry(user_info_frame)
        self.tensp_entry.grid(row=1, column=1)

        nvql_label = tk.Label(user_info_frame, text="Nhân viên QL")
        nvql_label.grid(row=0, column=2, padx = 10)
        self.nvql_combobox = ttk.Combobox(user_info_frame, values=["NVK0001", "NVK0002"])
        self.nvql_combobox.grid(row=1, column=2, padx = 10)

        dvt_label = tk.Label(user_info_frame, text="ĐVT")
        dvt_label.grid(row=2, column=0)
        self.dvt_entry = tk.Entry(user_info_frame)
        self.dvt_entry.grid(row=3, column=0)

        dg_label = tk.Label(user_info_frame, text="Đơn giá")
        dg_label.grid(row=2, column=1)
        self.dg_entry = tk.Entry(user_info_frame)
        self.dg_entry.grid(row=3, column=1)

        nvcr_label = tk.Label(user_info_frame, text="Nhân viên tạo")
        nvcr_label.grid(row=2, column=2, padx = 10)
        self.nvcr_combobox = ttk.Combobox(user_info_frame, values=["NVSX001", "NVSX002","NVSX003", "NVSX004","NVSX005"])
        self.nvcr_combobox.grid(row=3, column=2, padx = 10)

        nvl_label = tk.Label(user_info_frame, text="Nguyên vật liệu")
        nvl_label.grid(row=4, column=0, padx = 10)
        self.nvl_combobox = ttk.Combobox(user_info_frame, values=["YX-QB026", "YX-DZ006","YS-DM011", "YS-ZY014","YW-XG039","YS-FH001"])
        self.nvl_combobox.grid(row=5, column=0, padx = 10)

        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

