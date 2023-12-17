import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Create_CCDC:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới công cụ dụng cụ")
        self.root.geometry("490x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        maccdc = self.maccdc_entry.get()
        tenccdc = self.tenccdc_entry.get()
        tt = self.tt_combobox.get()
        giatri = self.gt_entry.get()
        pb = self.pb_combobox.get()
        nv = self.nv_combobox.get()
        if not maccdc or not tenccdc or not tt or not giatri or not pb or not nv:
            tk.messagebox.showwarning(title="Error", message="Lỗi nhập liệu!!")
        else:
            print("Mã NV: ", "Tên NV: ",  "Phòng ban: ")
            print("SDT:  ",  "Email: ", "STK:")
            print("Địa chỉ: ")
            print("------------------------------------------")

    def create_ui(self, parent_frame):

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)
        maccdc_label = tk.Label(user_info_frame, text="Mã CCDC")
        maccdc_label.grid(row=0, column=0, padx = 10)
        self.maccdc_entry = tk.Entry(user_info_frame)
        self.maccdc_entry.grid(row=1, column=0, padx = 10)

        tenccdc_label = tk.Label(user_info_frame, text="Tên CCDC")
        tenccdc_label.grid(row=0, column=1)
        self.tenccdc_entry = tk.Entry(user_info_frame)
        self.tenccdc_entry.grid(row=1, column=1)

        tt_label = tk.Label(user_info_frame, text="Tình trạng")
        tt_label.grid(row=0, column=2, padx = 10)
        self.tt_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
        self.tt_combobox.grid(row=1, column=2, padx = 10)

        gt_label = tk.Label(user_info_frame, text="Giá trị")
        gt_label.grid(row=2, column=0)
        self.gt_entry = tk.Entry(user_info_frame)
        self.gt_entry.grid(row=3, column=0)

        pb_label = tk.Label(user_info_frame, text="Phòng ban")
        pb_label.grid(row=2, column=1, padx = 10)
        self.pb_combobox = ttk.Combobox(user_info_frame, values=["KH0001", "KH0002", "KH0003", "NCC001", "NCC002", "NCC003"])
        self.pb_combobox.grid(row=3, column=1, padx = 10)

        nv_label = tk.Label(user_info_frame, text="Nhân viên")
        nv_label.grid(row=2, column=2, padx = 10)
        self.nv_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
        self.nv_combobox.grid(row=3, column=2, padx = 10)
        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
