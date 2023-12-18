import tkinter as tk
from tkinter import ttk, messagebox
from Process.NV import Create_NV
from Process.hopDong import Create_HD

from Process.phongBan import Create_PB
from Process.KH import Create_KH
from Process.NCC import Create_NCC
from Process.taiLieu import Create_TL
from Process.SP import Create_SP
from Process.NVL import Create_NVL
from Process.BB import Create_BB
from Process.VBPQ import Create_VBPQ
from Process.TSCD import Create_TSCD
from Process.CCDC import Create_CCDC
import requests

root = tk.Tk()
root.geometry('1500x500')
root.title('Tài sản số hóa')
options_fm = tk.Frame(root)

def switch(indicator_lb, page):
    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child['bg'] = 'SystemButtonFace'
    indicator_lb['bg'] = '#0097e8'
    
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()
    page()
phongban_btn = tk.Button(options_fm, text='Phòng ban', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=phongban_indicator_lb, page=phongban_page))
phongban_btn.place(x=0, y=0, width=125, height=35)

phongban_indicator_lb = tk.Label(options_fm, bg='#0097e8')
phongban_indicator_lb.place(x=22, y=30, width=80, height=2)

nhanvien_btn = tk.Button(options_fm, text='Nhân viên', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=nhanvien_indicator_lb, page=nhanvien_page))
nhanvien_btn.place(x=125, y=0, width=125, height=35)

nhanvien_indicator_lb = tk.Label(options_fm, bg='#fff')
nhanvien_indicator_lb.place(x=147, y=30, width=80, height=2)

khachhang_btn = tk.Button(options_fm, text='Khách hàng', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=khachhang_indicator_lb, page=khachhang_page))
khachhang_btn.place(x=250, y=0, width=125, height=35)

khachhang_indicator_lb = tk.Label(options_fm, bg='#fff')
khachhang_indicator_lb.place(x=272, y=30, width=80, height=2)

nhacc_btn = tk.Button(options_fm, text='Nhà CC', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=nhacc_indicator_lb, page=nhacc_page))
nhacc_btn.place(x=375, y=0, width=125, height=35)

nhacc_indicator_lb = tk.Label(options_fm, bg='#fff')
nhacc_indicator_lb.place(x=397, y=30, width=80, height=2)

donhang_btn = tk.Button(options_fm, text='Đơn hàng', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=donhang_indicator_lb, page=donhang_page))
donhang_btn.place(x=500, y=0, width=125, height=35)

donhang_indicator_lb = tk.Label(options_fm, bg='#fff')
donhang_indicator_lb.place(x=522, y=30, width=80, height=2)

hopdong_btn = tk.Button(options_fm, text='Hợp đồng', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=hopdong_indicator_lb, page=hopdong_page))
hopdong_btn.place(x=625, y=0, width=125, height=35)

hopdong_indicator_lb = tk.Label(options_fm, bg='#fff')
hopdong_indicator_lb.place(x=647, y=30, width=80, height=2)

tailieu_btn = tk.Button(options_fm, text='Tài liệu', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=tailieu_indicator_lb, page=tailieu_page))
tailieu_btn.place(x=750, y=0, width=125, height=35)

tailieu_indicator_lb = tk.Label(options_fm, bg='#fff')
tailieu_indicator_lb.place(x=772, y=30, width=80, height=2)

nvl_btn = tk.Button(options_fm, text='Vật liệu', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=nvl_indicator_lb, page=nvl_page))
nvl_btn.place(x=875, y=0, width=125, height=35)

nvl_indicator_lb = tk.Label(options_fm, bg='#fff')
nvl_indicator_lb.place(x=897, y=30, width=80, height=2)

sp_btn = tk.Button(options_fm, text='Sản phẩm', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=sp_indicator_lb, page=sanpham_page))
sp_btn.place(x=1000, y=0, width=125, height=35)

sp_indicator_lb = tk.Label(options_fm, bg='#fff')
sp_indicator_lb.place(x=1022, y=30, width=80, height=2)

bb_btn = tk.Button(options_fm, text='Sản phẩm', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=bb_indicator_lb, page=baibao_page))
bb_btn.place(x=1125, y=0, width=125, height=35)

bb_indicator_lb = tk.Label(options_fm, bg='#fff')
bb_indicator_lb.place(x=1147, y=30, width=80, height=2)

tscd_btn = tk.Button(options_fm, text='Tài sản CD', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=tscd_indicator_lb, page=tscd_page))
tscd_btn.place(x=1250, y=0, width=125, height=35)
tscd_indicator_lb = tk.Label(options_fm, bg='#fff')
tscd_indicator_lb.place(x=1272, y=30, width=80, height=2)

# vbpq_btn = tk.Button(options_fm, text='Sản phẩm', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=vbpq_indicator_lb, page=vbpq_page))
# vbpq_btn.place(x=1228, y=0, width=125, height=35)

# vbpq_indicator_lb = tk.Label(options_fm, bg='#fff')
# vbpq_indicator_lb.place(x=1250, y=30, width=80, height=2)





# ccdc_btn = tk.Button(options_fm, text='Sản phẩm', font=('Arial', 13), bd=0, fg='#0097e8', activeforeground='#0097e8', command=lambda: switch(indicator_lb=ccdc_indicator_lb, page=ccdc_page))
# ccdc_btn.place(x=1478, y=0, width=125, height=35)

# ccdc_indicator_lb = tk.Label(options_fm, bg='#fff')
# ccdc_indicator_lb.place(x=1500, y=30, width=80, height=2)
# button_logout = tk.Button(options_fm, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79",
#                                   fg="black")
# button_logout.place(x=1250, y=30, width=80, height=2)
options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=1500, height=35, background='#0097e8')



def phongban_page(): 
    phongban_page_fm = tk.Frame(main_fm)
    phongban_page_lb = tk.Label(phongban_page_fm, text='Phòng ban', font=('Arial', 25), fg='#0097e8')
    phongban_page_lb.pack(pady=30)
    phongban_page_fm.pack(fill=tk.BOTH, expand=True)
    
    def create_info_table(parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MAPB", "Tên phòng ban"), show="headings", style="Treeview")
        tree.heading("MAPB", text="Mã phòng ban", anchor=tk.CENTER)
        tree.heading("Tên phòng ban", text="Tên phòng ban", anchor=tk.CENTER)

        for i in range(2):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        try:
            response = requests.get("http://127.0.0.1:8000/pb")  # Replace with your actual API endpoint
            response.raise_for_status()
            data = response.json()

            # Clear existing data in the Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insert data into the Treeview
            for item in data:
                values = (item["MAPB"], item["TenPB"])  # Add more values as needed
                tree.insert("", "end", values=values)

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    
    def open_new_window():
        create_phongban_root = tk.Tk()
        home_page = Create_PB(create_phongban_root)
        create_phongban_root.mainloop()
        
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm", command=open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(phongban_page_fm)
    create_function_buttons(phongban_page_fm)
    
    

        # Tạo nút và chức năng
    
def nhanvien_page(): 
    nhanvien_page_fm = tk.Frame(main_fm)
    nhanvien_page_lb = tk.Label(nhanvien_page_fm, text='Nhân viên', font=('Arial', 25), fg='#0097e8')
    nhanvien_page_lb.pack(pady=30)
    nhanvien_page_fm.pack(fill=tk.BOTH, expand=True)
    def create_info_table(parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MANV", "Tên", "Phòng ban", "SDT","Email","STKNH","ĐC"), show="headings", style="Treeview")
        tree.heading("MANV", text="MANV", anchor=tk.CENTER)
        tree.heading("Tên", text="Tên", anchor=tk.CENTER)
        tree.heading("Phòng ban", text="Phòng ban", anchor=tk.CENTER)
        tree.heading("SDT", text="SDT", anchor=tk.CENTER)
        tree.heading("Email", text="Email", anchor=tk.CENTER)
        tree.heading("STKNH", text="STKNH", anchor=tk.CENTER)
        tree.heading("ĐC", text="ĐC", anchor=tk.CENTER)

        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        try:
            response = requests.get("http://127.0.0.1:8000/nv")  # Replace with your actual API endpoint
            response.raise_for_status()
            data = response.json()

            # Clear existing data in the Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insert data into the Treeview
            for item in data:
                values = (item["MANV"], item["TenNV"], item["TenNV"], item["SDT"], item["EMAIL"], item["STKNH"], item["DC"])  # Add more values as needed
                tree.insert("", "end", values=values)

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
        
    def open_new_window():
        create_nhanvien_root = tk.Tk()
        home_page = Create_NV(create_nhanvien_root)
        create_nhanvien_root.mainloop()
        
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm", font=("Arial", 14), command=open_new_window, bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(nhanvien_page_fm)
    create_function_buttons(nhanvien_page_fm)
def khachhang_page(): 
    khachhang_page_fm = tk.Frame(main_fm)
    khachhang_page_lb = tk.Label(khachhang_page_fm, text='Khách hàng', font=('Arial', 25), fg='#0097e8')
    khachhang_page_lb.pack(pady=30)
    khachhang_page_fm.pack(fill=tk.BOTH, expand=True)
    def create_info_table(parent_frame):
        
        
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MAKH", "Tên", "SDT", "Email","MST","ĐC","HĐ"), show="headings", style="Treeview")
        tree.heading("MAKH", text="MAKH", anchor=tk.CENTER)
        tree.heading("Tên", text="Tên", anchor=tk.CENTER)
        tree.heading("SDT", text="SDT", anchor=tk.CENTER)
        tree.heading("Email", text="Email", anchor=tk.CENTER)
        tree.heading("MST", text="MST", anchor=tk.CENTER)
        tree.heading("ĐC", text="ĐC", anchor=tk.CENTER)
        tree.heading("HĐ", text="HĐ", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)
        
        
            # Handle error, e.g., show a message box
        # kh_data = 
        # Sample data for the table
        data = [
            ("1", "Người 1", "Quản lý", "$5000","","",""),
            ("2", "Người 2", "Nhân viên", "$3000","","",""),
            ("3", "Người 3", "Nhân viên", "$3500","","",""),
            ("4", "Người 4", "Quản lý", "$4800","","",""),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_khachhang_root = tk.Tk()
        home_page = Create_KH(create_khachhang_root)
        create_khachhang_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(khachhang_page_fm)
    create_function_buttons(khachhang_page_fm)
def nhacc_page(): 
    nhacc_page_fm = tk.Frame(main_fm)
    nhacc_page_lb = tk.Label(nhacc_page_fm, text='Nhà cung cấp', font=('Arial', 25), fg='#0097e8')
    nhacc_page_lb.pack(pady=30)
    nhacc_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MANCC", "Tên", "SDT", "Email","MST","ĐC","HĐ"), show="headings", style="Treeview")
        tree.heading("MANCC", text="MANCC", anchor=tk.CENTER)
        tree.heading("Tên", text="Tên", anchor=tk.CENTER)
        tree.heading("SDT", text="SDT", anchor=tk.CENTER)
        tree.heading("Email", text="Email", anchor=tk.CENTER)
        tree.heading("MST", text="MST", anchor=tk.CENTER)
        tree.heading("ĐC", text="ĐC", anchor=tk.CENTER)
        tree.heading("HĐ", text="HĐ", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)



        # Make API request
        try:
            response = requests.get("http://127.0.0.1:8000/ncc")  # Replace with your actual API endpoint
            response.raise_for_status()
            data = response.json()

            # Clear existing data in the Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insert data into the Treeview
            for item in data:
                values = (item["MANCC"], item["TenNCC"], item["SDT"], item["EMAIL"], item["MST"], item["DC"], item["MST"])  # Add more values as needed
                tree.insert("", "end", values=values)

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_nhacc_root = tk.Tk()
        home_page = Create_NCC(create_nhacc_root)
        create_nhacc_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(nhacc_page_fm)
    create_function_buttons(nhacc_page_fm)
def donhang_page(): 
    donhang_page_fm = tk.Frame(main_fm)
    donhang_page_lb = tk.Label(donhang_page_fm, text='Đơn hàng', font=('Arial', 25), fg='#0097e8')
    donhang_page_lb.pack(pady=30)
    donhang_page_fm.pack(fill=tk.BOTH, expand=True)
def hopdong_page(): 
    hopdong_page_fm = tk.Frame(main_fm)
    hopdong_page_lb = tk.Label(hopdong_page_fm, text='Hợp đồng', font=('Arial', 25), fg='#0097e8')
    hopdong_page_lb.pack(pady=30)
    hopdong_page_fm.pack(fill=tk.BOTH, expand=True)
    
    def create_info_table(parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MAHD", "Tên hợp đồng", "Ngày hợp đồng", "Ngày tải lên", "Tệp đính kèm"), show="headings", style="Treeview")
        tree.heading("MAHD", text="MAHD", anchor=tk.CENTER)
        tree.heading("Tên hợp đồng", text="Tên hợp đồng", anchor=tk.CENTER)
        tree.heading("Ngày hợp đồng", text="Ngày hợp đồng", anchor=tk.CENTER)
        tree.heading("Ngày tải lên", text="Ngày tải lên", anchor=tk.CENTER)
        tree.heading("Tệp đính kèm", text="Tệp đính kèm", anchor=tk.CENTER)
        for i in range(2):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        try:
            response = requests.get("http://127.0.0.1:8000/hd")  # Replace with your actual API endpoint
            response.raise_for_status()
            data = response.json()

            # Clear existing data in the Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insert data into the Treeview
            for item in data:
                values = (item["MAHD"], item["TenHD"], item["NgayTao"], item["NgayTaiLen"], item["TepDinhKem"])  # Add more values as needed
                tree.insert("", "end", values=values)

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    
    def open_new_window():
        create_phongban_root = tk.Tk()
        home_page = Create_HD(create_phongban_root)
        create_phongban_root.mainloop()
        
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm", command=open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(hopdong_page_fm)
    create_function_buttons(hopdong_page_fm)
    
def tailieu_page():
    tailieu_page_fm = tk.Frame(main_fm)
    tailieu_page_lb = tk.Label(tailieu_page_fm, text='Tài liệu', font=('Arial', 25), fg='#0097e8')
    tailieu_page_lb.pack(pady=30)
    tailieu_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        tree = ttk.Treeview(parent_frame, columns=("MATL", "Tên tài liệu", "Ngày tải lên","Người tạo","Tệp đính kèm"), show="headings", style="Treeview")
        tree.heading("MATL", text="MATL", anchor=tk.CENTER)
        tree.heading("Tên tài liệu", text="Tên tài liệu", anchor=tk.CENTER)
        tree.heading("Ngày tải lên", text="Ngày tải lên", anchor=tk.CENTER)
        tree.heading("Người tạo", text="Người tạo", anchor=tk.CENTER)
        tree.heading("Tệp đính kèm", text="Tệp đính kèm", anchor=tk.CENTER)

        for i in range(2):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "TL1", "","",""),
            ("1", "TL1", "","",""),
            ("3", "TL1", "","",""),
            ("3", "TL1", "","",""),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)

    def open_new_window():
        create_tailieu_root = tk.Tk()
        home_page = Create_TL(create_tailieu_root)
        create_tailieu_root.mainloop()

    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm", command=open_new_window, font=("Arial", 14),
                               bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        

    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin

    create_info_table(tailieu_page_fm)
    create_function_buttons(tailieu_page_fm)
def tscd_page():
    tscd_page_fm = tk.Frame(main_fm)
    tscd_page_lb = tk.Label(tscd_page_fm, text='Tài sản cố định', font=('Arial', 25), fg='#0097e8')
    tscd_page_lb.pack(pady=30)
    tscd_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MATSCD", "Tên TSCĐ", "Trạng thái", "Giá trị","Thời hạn SD","Ngày mua","Khấu hao"), show="headings", style="Treeview")
        tree.heading("MATSCD", text="MATSCD", anchor=tk.CENTER)
        tree.heading("Tên TSCĐ", text="Tên TSCĐ", anchor=tk.CENTER)
        tree.heading("Trạng thái", text="Trạng thái", anchor=tk.CENTER)
        tree.heading("Giá trị", text="Giá trị", anchor=tk.CENTER)
        tree.heading("Thời hạn SD", text="Thời hạn SD", anchor=tk.CENTER)
        tree.heading("Ngày mua", text="Ngày mua", anchor=tk.CENTER)
        tree.heading("Khấu hao", text="Khấu hao", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)
        # Sample data for the table
        try:
            response = requests.get("http://127.0.0.1:8000/tscd")  # Replace with your actual API endpoint
            response.raise_for_status()
            data = response.json()

            # Clear existing data in the Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insert data into the Treeview
            for item in data:
                values = (item["MATSCD"], item["TenTSCD"], item["TT"], item["GiaTri"], item["THSD"], item["NgayMua"], item["KhauHao"])  # Add more values as needed
                tree.insert("", "end", values=values)
        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_tscd_root = tk.Tk()
        home_page = Create_TSCD(create_tscd_root)
        create_tscd_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(tscd_page_fm)
    create_function_buttons(tscd_page_fm)
def ccdc_page():
    ccdc_page_fm = tk.Frame(main_fm)
    ccdc_page_lb = tk.Label(ccdc_page_fm, text='Công cụ dụng cụ', font=('Arial', 25), fg='#0097e8')
    ccdc_page_lb.pack(pady=30)
    ccdc_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        tree = ttk.Treeview(parent_frame, columns=("MACCDC", "Tên CCDC", "Trạng thái", "Giá trị", "Phòng ban", "Nhân viên SD"), show="headings", style="Treeview")
        tree.heading("MACCDC", text="MACCDC", anchor=tk.CENTER)
        tree.heading("Tên CCDC", text="Tên CCDC", anchor=tk.CENTER)
        tree.heading("Trạng thái", text="Trạng thái", anchor=tk.CENTER)
        tree.heading("Giá trị", text="Giá trị", anchor=tk.CENTER)
        tree.heading("Phòng ban", text="Phòng ban", anchor=tk.CENTER)
        tree.heading("Nhân viên SD", text="Nhân viên SD", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)

        
        # Sample data for the table
        data = [
            ("1", "Người 1", "Quản lý", "$5000","",""),
            ("2", "Người 2", "Nhân viên", "$3000","",""),
            ("3", "Người 3", "Nhân viên", "$3500","",""),
            ("4", "Người 4", "Quản lý", "$4800","",""),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_ccdc_root = tk.Tk()
        home_page = Create_CCDC(create_ccdc_root)
        create_ccdc_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(ccdc_page_fm)
    create_function_buttons(ccdc_page_fm)
def sanpham_page():
    sanpham_page_fm = tk.Frame(main_fm)
    sanpham_page_lb = tk.Label(sanpham_page_fm, text='Sản phẩm', font=('Arial', 25), fg='#0097e8')
    sanpham_page_lb.pack(pady=30)
    sanpham_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MASP", "Tên sản phẩm", "Đơn vị tính", "Đơn giá","NVL","Người quản lý","Người tạo"), show="headings", style="Treeview")
        tree.heading("MASP", text="MASP", anchor=tk.CENTER)
        tree.heading("Tên sản phẩm", text="Tên sản phẩm", anchor=tk.CENTER)
        tree.heading("Đơn vị tính", text="Đơn vị tính", anchor=tk.CENTER)
        tree.heading("Đơn giá", text="Đơn giá", anchor=tk.CENTER)
        tree.heading("NVL", text="NVL", anchor=tk.CENTER)
        tree.heading("Người quản lý", text="Người quản lý", anchor=tk.CENTER)
        tree.heading("Người tạo", text="Người tạo", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "Người 1", "Quản lý", "$5000","","",""),
            ("2", "Người 2", "Nhân viên", "$3000","","",""),
            ("3", "Người 3", "Nhân viên", "$3500","","",""),
            ("4", "Người 4", "Quản lý", "$4800","","",""),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_sanpham_root = tk.Tk()
        home_page = Create_SP(create_sanpham_root)
        create_sanpham_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(sanpham_page_fm)
    create_function_buttons(sanpham_page_fm)
def nvl_page():
    nvl_page_fm = tk.Frame(main_fm)
    nvl_page_lb = tk.Label(nvl_page_fm, text='Nguyên vật liệu', font=('Arial', 25), fg='#0097e8')
    nvl_page_lb.pack(pady=30)
    nvl_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        tree = ttk.Treeview(parent_frame, columns=("MANVL", "Tên NVL", "Nhà cung cấp", "Đơn giá","Đơn vị tính","Người quản lý"), show="headings", style="Treeview")
        tree.heading("MANVL", text="MANVL", anchor=tk.CENTER)
        tree.heading("Tên NVL", text="Tên NVL", anchor=tk.CENTER)
        tree.heading("Đơn vị tính", text="Đơn vị tính", anchor=tk.CENTER)
        tree.heading("Đơn giá", text="Đơn giá", anchor=tk.CENTER)
        tree.heading("Nhà cung cấp", text="Nhà cung cấp", anchor=tk.CENTER)
        tree.heading("Người quản lý", text="Người quản lý", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "Người 1", "Quản lý", "$5000","",""),
            ("2", "Người 2", "Nhân viên", "$3000","",""),
            ("3", "Người 3", "Nhân viên", "$3500","",""),
            ("4", "Người 4", "Quản lý", "$4800","",""),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_nvl_root = tk.Tk()
        home_page = Create_NVL(create_nvl_root)
        create_nvl_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(nvl_page_fm)
    create_function_buttons(nvl_page_fm)
def baibao_page():
    bb_page_fm = tk.Frame(main_fm)
    bb_page_lb = tk.Label(bb_page_fm, text='Bài báo', font=('Arial', 25), fg='#0097e8')
    bb_page_lb.pack(pady=30)
    bb_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        tree = ttk.Treeview(parent_frame, columns=("MABB", "Tên bài báo", "Ngày viết", "Nhà báo","Người quản lý"), show="headings", style="Treeview")
        tree.heading("MABB", text="MABB", anchor=tk.CENTER)
        tree.heading("Tên bài báo", text="Tên bài báo", anchor=tk.CENTER)
        tree.heading("Ngày viết", text="Ngày viết", anchor=tk.CENTER)
        tree.heading("Nhà báo", text="Nhà báo", anchor=tk.CENTER)
        tree.heading("Người quản lý", text="Người quản lý", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "Người 1", "Quản lý", "$5000",""),
            ("2", "Người 2", "Nhân viên", "$3000",""),
            ("3", "Người 3", "Nhân viên", "$3500",""),
            ("4", "Người 4", "Quản lý", "$4800",""),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_bb_root = tk.Tk()
        home_page = Create_BB(create_bb_root)
        create_bb_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(bb_page_fm)
    create_function_buttons(bb_page_fm)
def vbpq_page():
    vbpq_page_fm = tk.Frame(main_fm)
    vbpq_page_lb = tk.Label(vbpq_page_fm, text='Văn bản pháp quy', font=('Arial', 25), fg='#0097e8')
    vbpq_page_lb.pack(pady=30)
    vbpq_page_fm.pack(fill=tk.BOTH, expand=True)

    def create_info_table(parent_frame):
        tree = ttk.Treeview(parent_frame, columns=("MAVBPQ", "Tên VBPQ", "Ngày ban hành", "Nhân viên ban hành","Người quản lý"), show="headings", style="Treeview")
        tree.heading("MAVBPQ", text="MAVBPQ", anchor=tk.CENTER)
        tree.heading("Tên VBPQ", text="Tên VBPQ", anchor=tk.CENTER)
        tree.heading("Ngày ban hành", text="Ngày ban hành", anchor=tk.CENTER)
        tree.heading("Nhân viên ban hành", text="Nhân viên ban hành", anchor=tk.CENTER)
        tree.heading("Người quản lý", text="Người quản lý", anchor=tk.CENTER)
        for i in range(4):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "Người 1", "Quản lý", "$5000",""),
            ("2", "Người 2", "Nhân viên", "$3000",""),
            ("3", "Người 3", "Nhân viên", "$3500",""),
            ("4", "Người 4", "Quản lý", "$4800",""),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.TOP)
        tree.configure(yscrollcommand=scroll_y.set)
    def open_new_window():
        create_vbpq_root = tk.Tk()
        home_page = Create_VBPQ(create_vbpq_root)
        create_vbpq_root.mainloop()
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm",command = open_new_window, font=("Arial", 14), bg="#5f6f79", fg="black")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", font=("Arial", 14), bg="#5f6f79", fg="black")
        button_logout.pack(side=tk.LEFT, padx=10)


    def insert_options(tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                insert_options(tree, sub_options)
                tree.item(item, open=True)

        # Tạo bảng thông tin
    create_info_table(vbpq_page_fm)
    create_function_buttons(vbpq_page_fm)


main_fm = tk.Frame(root, bg='gray')
main_fm.pack(fill=tk.BOTH, expand=True)



phongban_page()


root.mainloop()