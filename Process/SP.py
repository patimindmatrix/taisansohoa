import tkinter
from tkinter import ttk
from tkinter import messagebox
def Create_SP():
    masp = masp_entry.get()
    tensp = tensp_entry.get()
    dvt = dvt_entry.get()
    dongia = dg_entry.get()
    nvl = nvl_combobox.get()
    nvql = nvql_combobox.get()
    nvcr = nvcr_combobox.get()

    if not masp or not tensp or not dvt or not nvl or not nvql or not nvcr or not dongia :
        tkinter.messagebox.showwarning(title="Error", message="Thông tin không được bỏ trống")
    else:
        print("Mã NV: ", masp, "Tên NV: ", tensp, "Phòng ban: ", dvt)
        print("SDT:  ", dongia, "Email: ", nvl, "STK:", nvql)
        print("Địa chỉ: ", nvcr)
        print("------------------------------------------")

window = tkinter.Tk()
window.title("Thêm mới Sản phẩm")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

masp_label = tkinter.Label(user_info_frame, text="Mã SP")
masp_label.grid(row=0, column=0, padx = 10)
masp_entry = tkinter.Entry(user_info_frame)
masp_entry.grid(row=1, column=0, padx = 10)

tensp_label = tkinter.Label(user_info_frame, text="Tên SP")
tensp_label.grid(row=0, column=1)
tensp_entry = tkinter.Entry(user_info_frame)
tensp_entry.grid(row=1, column=1)

nvql_label = tkinter.Label(user_info_frame, text="Nhân viên QL")
nvql_label.grid(row=0, column=2, padx = 10)
nvql_combobox = ttk.Combobox(user_info_frame, values=["NVK0001", "NVK0002"])
nvql_combobox.grid(row=1, column=2, padx = 10)

dvt_label = tkinter.Label(user_info_frame, text="ĐVT")
dvt_label.grid(row=2, column=0)
dvt_entry = tkinter.Entry(user_info_frame)
dvt_entry.grid(row=3, column=0)

dg_label = tkinter.Label(user_info_frame, text="Đơn giá")
dg_label.grid(row=2, column=1)
dg_entry = tkinter.Entry(user_info_frame)
dg_entry.grid(row=3, column=1)

nvcr_label = tkinter.Label(user_info_frame, text="Nhân viên tạo")
nvcr_label.grid(row=2, column=2, padx = 10)
nvcr_combobox = ttk.Combobox(user_info_frame, values=["NVSX001", "NVSX002","NVSX003", "NVSX004","NVSX005"])
nvcr_combobox.grid(row=3, column=2, padx = 10)

nvl_label = tkinter.Label(user_info_frame, text="Nguyên vật liệu")
nvl_label.grid(row=4, column=0, padx = 10)
nvl_combobox = ttk.Combobox(user_info_frame, values=["YX-QB026", "YX-DZ006","YS-DM011", "YS-ZY014","YW-XG039","YS-FH001"])
nvl_combobox.grid(row=5, column=0, padx = 10)

# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_SP)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()