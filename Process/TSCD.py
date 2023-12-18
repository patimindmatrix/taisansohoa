from datetime import datetime
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import requests


class Create_TSCD:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới tài sản cố định")
        self.root.geometry("790x500")  # Kích thước cửa sổ

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
            purchase_date = datetime.strptime(ngaymua, '%d/%m/%Y')
            current_date = datetime.now()
            years_difference = current_date.year - purchase_date.year
            new_giatri = int(giatri)
            new_thsd = int(thsd)
            khauhao = str((years_difference * new_giatri) / new_thsd)
            data = {
                "MATSCD": matscd,
                "TenTSCD": tentscd,
                "TT": tt,
                "GiaTri": giatri,
                "THSD": thsd,
                "NgayMua": ngaymua,
                "KhauHao": khauhao
            }
            try:
                response = requests.post("http://127.0.0.1:8000/tscd", json=data)  # Replace with your actual API endpoint
                response.raise_for_status()
                data = response.json()

            except requests.RequestException as e:
                print(f"An error occurred: {e}")

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
        self.tt_combobox = ttk.Combobox(user_info_frame, values=["Đang sử dụng", "Chưa sử dụng"])
        self.tt_combobox.grid(row=1, column=2, padx = 10)

        gt_label = tk.Label(user_info_frame, text="Giá trị")
        gt_label.grid(row=2, column=0)
        self.gt_entry = tk.Entry(user_info_frame)
        self.gt_entry.grid(row=3, column=0)

        thsd_label = tk.Label(user_info_frame, text="THSD")
        thsd_label.grid(row=2, column=1)
        self.thsd_entry = tk.Entry(user_info_frame)
        self.thsd_entry.grid(row=3, column=1)

        ngaymua_label = tk.Label(user_info_frame, text="Ngày mua")
        ngaymua_label.grid(row=2, column=2)
        self.ngaymua_entry = tk.Entry(user_info_frame)
        self.ngaymua_entry.grid(row=3, column=2)

        khauhao_label = tk.Label(user_info_frame, text="Khấu hao")
        khauhao_label.grid(row=4, column=0)
        self.kh_entry = tk.Entry(user_info_frame)
        self.kh_entry.grid(row=5, column=0)

        pb_label = tk.Label(user_info_frame, text="Phòng ban")
        pb_label.grid(row=4, column=1, padx = 10)
        pb_data = []
        try:
            response = requests.get("http://127.0.0.1:8000/pb")  # Replace with your actual API endpoint
            response.raise_for_status()
            data = response.json()
            pb_data = data

        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        self.pb_combobox = ttk.Combobox(user_info_frame)
        self.pb_combobox["values"] = [item["TenPB"] for item in pb_data]
        self.pb_combobox.grid(row=5, column=1, padx = 10)

        nv_label = tk.Label(user_info_frame, text="Nhân viên")
        nv_label.grid(row=4, column=2, padx = 10)
        nv_data = []
        try:
            response = requests.get("http://127.0.0.1:8000/nv")  # Replace with your actual API endpoint
            response.raise_for_status()
            data = response.json()
            nv_data = data

        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        self.nv_combobox = ttk.Combobox(user_info_frame)
        self.nv_combobox["values"] = [item["TenNV"] for item in nv_data]
        self.nv_combobox.grid(row=5, column=2, padx = 10)
        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=6, column=0, sticky="news", padx=20, pady=10)
