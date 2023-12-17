import tkinter as tk
from tkinter import ttk, messagebox
from Process.NV import Create_NV
from Process.hopDong import Create_HD

from Process.phongBan import Create_PB
root = tk.Tk()
root.geometry('900x900')
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

options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=750, height=35, background='#0097e8')

def phongban_page(): 
    phongban_page_fm = tk.Frame(main_fm)
    phongban_page_lb = tk.Label(phongban_page_fm, text='Phòng ban', font=('Arial', 25), fg='#0097e8')
    phongban_page_lb.pack(pady=30)
    phongban_page_fm.pack(fill=tk.BOTH, expand=True)
    
    def create_info_table(parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("MAPB", "Tên phòng ban"), show="headings", style="Treeview")
        tree.heading("MAPB", text="MAPB", anchor=tk.CENTER)
        tree.heading("Tên phòng ban", text="Tên phòng ban", anchor=tk.CENTER)

        for i in range(2):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "PB001"),
            ("1", "PB002"),
            ("3", "PB003"),
            ("3", "PB004"),
        ]

        for row in data:
            tree.insert("", "end", values=row)

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
        create_phongban_root = tk.Tk()
        home_page = Create_HD(create_phongban_root)
        create_phongban_root.mainloop()
        
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
        
    def create_function_buttons(parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.TOP, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm", font=("Arial", 14), bg="#5f6f79", fg="black")
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
        tree = ttk.Treeview(parent_frame, columns=("ID", "Tên phòng ban"), show="headings", style="Treeview")
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Tên phòng ban", text="Tên phòng ban", anchor=tk.CENTER)

        for i in range(2):
            tree.column(i, width=180, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "PB001"),
            ("1", "PB002"),
            ("3", "PB003"),
            ("3", "PB004"),
        ]

        for row in data:
            tree.insert("", "end", values=row)

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

main_fm = tk.Frame(root, bg='gray')
main_fm.pack(fill=tk.BOTH, expand=True)



phongban_page()


root.mainloop()