import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Create_BB:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới bài báo")
        self.root.geometry("500x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        mabb = self.mabb_entry.get()
        tenbb = self.tenbb_entry.get()
        ngayviet =  self.ngayviet_entry.get()
        nb =  self.nb_entry.get()
        nvql =  self.nvql_combobox.get()
        if not mabb or not tenbb or not ngayviet or not nb or not nvql:
            tk.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
        else:
            print("Mã HĐ: ", "Tên HĐ: ",  "Ngày tải lên: ",  "ngày hợp đồng:")
            print("Nhân viên:  ",  "tệp: ", "đối tượng:")
            print("------------------------------------------")

    def create_ui(self, parent_frame):

        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        mabb_label = tk.Label(user_info_frame, text="Mã bài báo")
        mabb_label.grid(row=0, column=0, padx = 10)
        self.mabb_entry = tk.Entry(user_info_frame)
        self.mabb_entry.grid(row=1, column=0, padx = 10)

        tenbb_label = tk.Label(user_info_frame, text="Tên bài báo")
        tenbb_label.grid(row=0, column=1)
        self.tenbb_entry = tk.Entry(user_info_frame)
        self.tenbb_entry.grid(row=1, column=1)

        nviet_label = tk.Label(user_info_frame, text="Ngày viết")
        nviet_label.grid(row=0, column=2)
        self.ngayviet_entry = tk.Entry(user_info_frame)
        self.ngayviet_entry.grid(row=1, column=2)

        nb_label = tk.Label(user_info_frame, text="Nhà báo")
        nb_label.grid(row=2, column=0)
        self.nb_entry = tk.Entry(user_info_frame)
        self.nb_entry.grid(row=3, column=0)

        nvql_label = tk.Label(user_info_frame, text="Nhân viên QL")
        nvql_label.grid(row=2, column=1)
        self.nvql_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002","NVNS003",])
        self.nvql_combobox.grid(row=3, column=1)

        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
