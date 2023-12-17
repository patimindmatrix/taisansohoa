import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Create_NV:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới nhân viên")
        self.root.geometry("700x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_ui(frame)
    def create(self):
        manv = self.manv_entry.get()
        tennv = self.tennv_entry.get()
        pb = self.pb_combobox.get()
        sdt = self.sdt_entry.get()
        email = self.email_entry.get()
        stknh = self.stknh_entry.get()
        dc = self.dc_entry.get()
        if not manv or not tennv:
            tk.messagebox.showwarning(title="Error", message="Mã NV bắt buộc nhập")
        else:
            print("Mã NV: ", manv, "Tên NV: ", tennv, "Phòng ban: ", pb)
            print("SDT:  ", sdt, "Email: ", email, "STK:", stknh)
            print("Địa chỉ: ", dc)
            print("------------------------------------------")

    def create_ui(self, parent_frame): 

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        manv_label = tk.Label(user_info_frame, text="Mã NV")
        manv_label.grid(row=0, column=0, padx = 10)
        self.manv_entry = tk.Entry(user_info_frame)
        self.manv_entry.grid(row=1, column=0, padx = 10)

        tennv_label = tk.Label(user_info_frame, text="Tên NV")
        tennv_label.grid(row=0, column=1)
        self.tennv_entry = tk.Entry(user_info_frame)
        self.tennv_entry.grid(row=1, column=1)

        pb_label = tk.Label(user_info_frame, text="Phòng ban")
        pb_label.grid(row=0, column=2, padx = 10)
        self.pb_combobox = ttk.Combobox(user_info_frame, values=["Điều hành", "Nhân sự", "QC", "Kho", "Sản xuất"])
        self.pb_combobox.grid(row=1, column=2, padx = 10)

        sdt_label = tk.Label(user_info_frame, text="SĐT")
        sdt_label.grid(row=2, column=0)
        self.sdt_entry = tk.Entry(user_info_frame)
        self.sdt_entry.grid(row=3, column=0)

        email_label = tk.Label(user_info_frame, text="Email")
        email_label.grid(row=2, column=1)
        self.email_entry = tk.Entry(user_info_frame)
        self.email_entry.grid(row=3, column=1)

        stknh_label = tk.Label(user_info_frame, text="STK")
        stknh_label.grid(row=2, column=2)
        self.stknh_entry = tk.Entry(user_info_frame)
        self.stknh_entry.grid(row=3, column=2)

        mk_label = tk.Label(user_info_frame, text="Mật khẩu")
        mk_label.grid(row=4, column=0)
        self.mk_entry = tk.Entry(user_info_frame, show="*")
        self.mk_entry.grid(row=5, column=0)

        mkl_label = tk.Label(user_info_frame, text="Nhập lại MK")
        mkl_label.grid(row=4, column=1)
        self.mkl_entry = tk.Entry(user_info_frame, show="*")
        self.mkl_entry.grid(row=5, column=1)

        dc_label = tk.Label(user_info_frame, text="Địa chỉ")
        dc_label.grid(row=6, column=0)
        self.dc_entry = tk.Entry(user_info_frame)
        self.dc_entry.grid(row=7, column=0)
        # Button
        save_button= tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
