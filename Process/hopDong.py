import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox

class Create_HD:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới hợp đồng 123")
        self.root.geometry("1000x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        mahd = self.mahd_entry.get()
        tenhd = self.tenhd_entry.get()
        ngayhd = self.ngayhd_entry.get()
        ngaytailen = self.ngaytailen_entry.get()
        nguoitao = self.ngt_combobox.get()
        doituong = self.dt_combobox.get()
        tepdinhkem = self.tepdinhkem_entry.get()

        if not mahd or not tepdinhkem or not nguoitao or not doituong:
            tk.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
        else:
            print("Mã HĐ: ", mahd, "Tên HĐ: ", tenhd, "Ngày tải lên: ", ngaytailen, "ngày hợp đồng:", ngayhd)
            print("Nhân viên:  ", nguoitao, "tệp: ", tepdinhkem, "đối tượng:", doituong)
            print("------------------------------------------")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        self.tepdinhkem_entry.delete(0, tk.END)
        self.tepdinhkem_entry.insert(0, file_path)

    def create_ui(self, parent_frame):

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        mahd_label = tk.Label(user_info_frame, text="Mã HĐ")
        mahd_label.grid(row=0, column=0, padx=10)
        self.mahd_entry = tk.Entry(user_info_frame)
        self.mahd_entry.grid(row=1, column=0, padx=10)

        tenhd_label = tk.Label(user_info_frame, text="Tên HĐ")
        tenhd_label.grid(row=0, column=1)
        self.tenhd_entry = tk.Entry(user_info_frame)
        self.tenhd_entry.grid(row=1, column=1)

        ngt_label = tk.Label(user_info_frame, text="Nhân viên")
        ngt_label.grid(row=0, column=2, padx=10)
        self.ngt_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
        self.ngt_combobox.grid(row=1, column=2, padx=10)

        ngayhd_label = tk.Label(user_info_frame, text="Ngày hợp đồng")
        ngayhd_label.grid(row=2, column=0)
        self.ngayhd_entry = tk.Entry(user_info_frame)
        self.ngayhd_entry.grid(row=3, column=0)

        ngaytailen_label = tk.Label(user_info_frame, text="Ngày tải lên")
        ngaytailen_label.grid(row=2, column=1)
        self.ngaytailen_entry = tk.Entry(user_info_frame)
        self.ngaytailen_entry.grid(row=3, column=1)

        tepdinhkem_label = tk.Label(user_info_frame, text="Tệp")
        tepdinhkem_label.grid(row=2, column=2)
        # self.tepdinhkem_entry = tk.Entry(user_info_frame)
        # self.tepdinhkem_entry.grid(row=3, column=2)

        tepdinhkem_btn = tk.Button(user_info_frame, text="Chọn tệp", command=self.open_file, bg="#000")
        tepdinhkem_btn.grid(row=3, column=2, padx=10)

        dt_label = tk.Label(user_info_frame, text="Đối tượng")
        dt_label.grid(row=2, column=3, padx=10)
        self.dt_combobox = ttk.Combobox(user_info_frame, values=["KH0001", "KH0002", "KH0003", "NCC001", "NCC002", "NCC003"])
        self.dt_combobox.grid(row=3, column=3, padx=10)

        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
