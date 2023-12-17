import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
class Create_TL:
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm mới tài liệu")
        self.root.geometry("1000x400")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        frame = ttk.Frame(root, style="TFrame")
        frame.pack(fill=tk.BOTH, expand=True)

        self.create_ui(frame)

    def create(self):
        matl = self.matl_entry.get()
        tentl = self.tentl_entry.get()
        ngaytailen = self.ngaytailen_entry.get()
        nguoitao = self.nguoitao_combobox.get()
        tepdinhkem = self.tepdinhkem_entry.get()

        if not matl or not tepdinhkem or not nguoitao or not tentl:
            tk.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
        else:
            print("Mã HĐ: ", "Tên HĐ: ",  "Ngày tải lên: ", ngaytailen, "ngày hợp đồng:")
            print("Nhân viên:  ", nguoitao, "tệp: ", tepdinhkem, "đối tượng:")
            print("------------------------------------------")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        self.tepdinhkem_entry.delete(0, tk.END)
        self.tepdinhkem_entry.insert(0, file_path)

    def create_ui(self, parent_frame):

        # Saving User Info
        user_info_frame = tk.LabelFrame(parent_frame)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)
        matl_label = tk.Label(user_info_frame, text="Mã TL")
        matl_label.grid(row=0, column=0, padx = 10)
        self.matl_entry = tk.Entry(user_info_frame)
        self.matl_entry.grid(row=1, column=0, padx = 10)

        tentl_label = tk.Label(user_info_frame, text="Tên TL")
        tentl_label.grid(row=0, column=1)
        self.tentl_entry = tk.Entry(user_info_frame)
        self.tentl_entry.grid(row=1, column=1)

        nguoitao_label = tk.Label(user_info_frame, text="Nhân viên")
        nguoitao_label.grid(row=0, column=2, padx = 10)
        self.nguoitao_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
        self.nguoitao_combobox.grid(row=1, column=2, padx = 10)

        ngaytailen_label = tk.Label(user_info_frame, text="Ngày tải lên")
        ngaytailen_label.grid(row=2, column=0)
        self.ngaytailen_entry = tk.Entry(user_info_frame)
        self.ngaytailen_entry.grid(row=3, column=0)

        tepdinhkem_label = tk.Label(user_info_frame, text="Tệp")
        tepdinhkem_label.grid(row=2, column=2)
        tepdinhkem_btn = tk.Button(user_info_frame, text="Chọn tệp", command=self.open_file, bg="#000")
        tepdinhkem_btn.grid(row=3, column=2, padx=10)

        # Button
        save_button = tk.Button(parent_frame, text="Lưu", command=self.create)
        save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# import tkinter
# from tkinter import ttk
# from tkinter import messagebox
# from tkinter import filedialog
# def Create_TL():
#     matl = matl_entry.get()
#     tentl = tentl_entry.get()
#     ngaytailen = ngaytailen_entry.get()
#     nguoitao = nguoitao_combobox.get()
#     tepdinhkem = tepdinhkem_btn.get()
#     if not matl or not tepdinhkem or not nguoitao:
#         tkinter.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
#     else:
#         print("Mã TL: ", matl, "Tên TL: ", tentl, "Ngày tải lên: ", ngaytailen)
#         print("Nhân viên:  ", nguoitao, "tệp: ", tepdinhkem)
#         print("------------------------------------------")
# def Openfile():
#     filepath = filedialog.askopenfilename()
#
# window = tkinter.Tk()
# window.title("Thêm mới tài liệu")
#
# frame = tkinter.Frame(window)
# frame.pack()
#
# # Saving User Info
# user_info_frame = tkinter.LabelFrame(frame)
# user_info_frame.grid(row=0, column=0, padx=20, pady=10)
#
# matl_label = tkinter.Label(user_info_frame, text="Mã TL")
# matl_label.grid(row=0, column=0, padx = 10)
# matl_entry = tkinter.Entry(user_info_frame)
# matl_entry.grid(row=1, column=0, padx = 10)
#
# tentl_label = tkinter.Label(user_info_frame, text="Tên TL")
# tentl_label.grid(row=0, column=1)
# tentl_entry = tkinter.Entry(user_info_frame)
# tentl_entry.grid(row=1, column=1)
#
# nguoitao_label = tkinter.Label(user_info_frame, text="Nhân viên")
# nguoitao_label.grid(row=0, column=2, padx = 10)
# nguoitao_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
# nguoitao_combobox.grid(row=1, column=2, padx = 10)
#
# ngaytailen_label = tkinter.Label(user_info_frame, text="Ngày tải lên")
# ngaytailen_label.grid(row=2, column=0)
# ngaytailen_entry = tkinter.Entry(user_info_frame)
# ngaytailen_entry.grid(row=3, column=0)
#
# tepdinhkem_label = tkinter.Label(user_info_frame, text="Tệp")
# tepdinhkem_label.grid(row=2, column=1)
# tepdinhkem_btn = tkinter.Button(user_info_frame)
# tepdinhkem_btn.grid(row=3, column=1, command = Openfile())
# tepdinhkem_btn.config(width=18, height=1, text = "Chọn tệp")
# # Button
# save_button= tkinter.Button(frame, text="Lưu", command=Create_TL)
# save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
#
# window.mainloop()