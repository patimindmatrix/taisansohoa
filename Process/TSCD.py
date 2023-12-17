import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Create_TSCD:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới tài sản cố định")
        self.root.geometry("490x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        matscd = self.matscd_entry.get()
        tentscd = self.tentscd_entry.get()
        tt = self.tt_combobox.get()
        giatri = self.gt_entry.get()
        thsd = self.thsd_entry.get()
        ngaymua = self.ngaymua_entry.get()
        khauhao = self.kh_entry.get()
        pb = self.pb_combobox.get()
        nv = self.nv_combobox.get()
        if not matscd or not tentscd or not tt or not giatri or not thsd or not ngaymua or not pb or not nv :
            tk.messagebox.showwarning(title="Error", message="Lỗi nhập liệu!!")
        else:
            print("Mã NV: ", "Tên NV: ",  "Phòng ban: ")
            print("SDT:  ", "Email: ",  "STK:")
            print("Địa chỉ: ")
            print("------------------------------------------")

    def create_ui(self, parent_frame):

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)
        matscd_label = tk.Label(user_info_frame, text="Mã TSCĐ")
        matscd_label.grid(row=0, column=0, padx = 10)
        self.matscd_entry = tk.Entry(user_info_frame)
        self.matscd_entry.grid(row=1, column=0, padx = 10)

        tentscd_label = tk.Label(user_info_frame, text="Tên TSCĐ")
        tentscd_label.grid(row=0, column=1)
        self.tentscd_entry = tk.Entry(user_info_frame)
        self.tentscd_entry.grid(row=1, column=1)

        tt_label = tk.Label(user_info_frame, text="Tình trạng")
        tt_label.grid(row=0, column=2, padx = 10)
        self.tt_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
        self.tt_combobox.grid(row=1, column=2, padx = 10)

        gt_label = tk.Label(user_info_frame, text="Giá trị")
        gt_label.grid(row=2, column=0)
        self.gt_entry = tk.Entry(user_info_frame)
        self.gt_entry.grid(row=3, column=0)

        thsd_label = tk.Label(user_info_frame, text="THSD")
        thsd_label.grid(row=2, column=2)
        self.thsd_entry = tk.Entry(user_info_frame)
        self.thsd_entry.grid(row=3, column=2)

        ngaymua_label = tk.Label(user_info_frame, text="Ngày mua")
        ngaymua_label.grid(row=2, column=1)
        self.ngaymua_entry = tk.Entry(user_info_frame)
        self.ngaymua_entry.grid(row=3, column=1)

        khauhao_label = tk.Label(user_info_frame, text="Khấu hao", status = "readonly")
        khauhao_label.grid(row=4, column=0)
        self.kh_entry = tk.Entry(user_info_frame)
        self.kh_entry.grid(row=5, column=0)

        pb_label = tk.Label(user_info_frame, text="Phòng ban")
        pb_label.grid(row=4, column=1, padx = 10)
        self.pb_combobox = ttk.Combobox(user_info_frame, values=["KH0001", "KH0002", "KH0003", "NCC001", "NCC002", "NCC003"])
        self.pb_combobox.grid(row=5, column=1, padx = 10)

        nv_label = tk.Label(user_info_frame, text="Nhân viên")
        nv_label.grid(row=4, column=2, padx = 10)
        self.nv_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
        self.nv_combobox.grid(row=5, column=2, padx = 10)
        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
