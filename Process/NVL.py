import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Create_NVL:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới nguyên vật liệu")
        self.root.geometry("500x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        manvl = self.manvl_entry.get()
        tennvl =self.tennvl_entry.get()
        ncc = self.ncc_combobox.get()
        dvt = self.dvt_entry.get()
        dongia = self.dg_entry.get()
        nvql = self.nvql_combobox.get()
        if not manvl or not tennvl or not ncc or not dongia or not dvt or not nvql :
            tk.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
        else:
            print("Mã HĐ: ", "Tên HĐ: ",  "Ngày tải lên: ",  "ngày hợp đồng:")
            print("Nhân viên:  ",  "tệp: ", "đối tượng:")
            print("------------------------------------------")

    def create_ui(self, parent_frame):

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        manvl_label = tk.Label(user_info_frame, text="Mã NVL")
        manvl_label.grid(row=0, column=0, padx = 10)
        self.manvl_entry = tk.Entry(user_info_frame)
        self.manvl_entry.grid(row=1, column=0, padx = 10)

        tennvl_label = tk.Label(user_info_frame, text="Tên NVL")
        tennvl_label.grid(row=0, column=1)
        self.tennvl_entry = tk.Entry(user_info_frame)
        self.tennvl_entry.grid(row=1, column=1)

        ncc_label = tk.Label(user_info_frame, text="Nhà cung cấp")
        ncc_label.grid(row=0, column=2, padx = 10)
        self.ncc_combobox = ttk.Combobox(user_info_frame, values=["NCC001", "NCC002","NCC003", "NCC004"])
        self.ncc_combobox.grid(row=1, column=2, padx = 10)

        dvt_label = tk.Label(user_info_frame, text="ĐVT")
        dvt_label.grid(row=2, column=0)
        self.dvt_entry = tk.Entry(user_info_frame)
        self.dvt_entry.grid(row=3, column=0)

        dg_label = tk.Label(user_info_frame, text="Đơn giá")
        dg_label.grid(row=2, column=1)
        self.dg_entry = tk.Entry(user_info_frame)
        self.dg_entry.grid(row=3, column=1)

        nvql_label = tk.Label(user_info_frame, text="Nhân viên QL")
        nvql_label.grid(row=2, column=2, padx = 10)
        self.nvql_combobox = ttk.Combobox(user_info_frame, values=["NVK0001", "NVK0002"])
        self.nvql_combobox.grid(row=3, column=2, padx = 10)

        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

