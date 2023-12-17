import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Create_KH:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới khách hàng")
        self.root.geometry("500x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        makh = self.makh_entry.get()
        tenkh = self.tenkh_entry.get()
        sdt = self.sdt_entry.get()
        email = self.email_entry.get()
        mst = self.mst_entry.get()
        dc = self.dc_entry.get()
        hd = self.hd_combobox.get()
        if not makh or not tenkh or not sdt or not email or not mst or not dc:
            tk.messagebox.showwarning(title="Error", message="Lỗi nhập liệu!!")
        else:
            print("Mã NV: ", "Tên NV: ",  "Phòng ban: ")
            print("SDT:  ", sdt, "Email: ", email, "STK:")
            print("Địa chỉ: ", dc)
            print("------------------------------------------")

    def create_ui(self, parent_frame):

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        makh_label = tk.Label(user_info_frame, text="Mã KH")
        makh_label.grid(row=0, column=0, padx = 10)
        self.makh_entry = tk.Entry(user_info_frame)
        self.makh_entry.grid(row=1, column=0, padx = 10)
        tenkh_label = tk.Label(user_info_frame, text="Tên KH")
        tenkh_label.grid(row=0, column=1)
        self.tenkh_entry = tk.Entry(user_info_frame)
        self.tenkh_entry.grid(row=1, column=1)

        hd_label = tk.Label(user_info_frame, text="Hợp đồng")
        hd_label.grid(row=0, column=2, padx = 10)
        self.hd_combobox = ttk.Combobox(user_info_frame, values=["223S001", "23P002", "23P003", "23S002", "23S003"])
        self.hd_combobox.grid(row=1, column=2, padx = 10)

        sdt_label = tk.Label(user_info_frame, text="SĐT")
        sdt_label.grid(row=2, column=0)
        self.sdt_entry = tk.Entry(user_info_frame)
        self.sdt_entry.grid(row=3, column=0)

        email_label = tk.Label(user_info_frame, text="Email")
        email_label.grid(row=2, column=1)
        self.email_entry = tk.Entry(user_info_frame)
        self.email_entry.grid(row=3, column=1)

        mst_label = tk.Label(user_info_frame, text="MST")
        mst_label.grid(row=2, column=2)
        self.mst_entry = tk.Entry(user_info_frame)
        self.mst_entry.grid(row=3, column=2)

        dc_label = tk.Label(user_info_frame, text="Địa chỉ")
        dc_label.grid(row=4, column=0)
        self.dc_entry = tk.Entry(user_info_frame)
        self.dc_entry.grid(row=5, column=0)
        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
