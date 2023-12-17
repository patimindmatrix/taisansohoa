import tkinter
from tkinter import ttk
from tkinter import messagebox
def Create_NVL():
    manvl = manvl_entry.get()
    tennvl =tennvl_entry.get()
    ncc = ncc_combobox.get()
    dvt = dvt_entry.get()
    dongia = dg_entry.get()
    nvql = nvql_combobox.get()

    if not manvl or not tennvl or not ncc or not dvt or not nvql or not dongia or not nvql :
        tkinter.messagebox.showwarning(title="Error", message="Thông tin không được bỏ trống")
    else:
        print("Mã NV: ", manvl, "Tên NV: ", tennvl, "Phòng ban: ", ncc)
        print("SDT:  ", dongia, "Email: ", dvt, "STK:", nvql)
        print("------------------------------------------")

window = tkinter.Tk()
window.title("Thêm mới Sản phẩm")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

manvl_label = tkinter.Label(user_info_frame, text="Mã NVL")
manvl_label.grid(row=0, column=0, padx = 10)
manvl_entry = tkinter.Entry(user_info_frame)
manvl_entry.grid(row=1, column=0, padx = 10)

tennvl_label = tkinter.Label(user_info_frame, text="Tên NVL")
tennvl_label.grid(row=0, column=1)
tennvl_entry = tkinter.Entry(user_info_frame)
tennvl_entry.grid(row=1, column=1)

ncc_label = tkinter.Label(user_info_frame, text="Nhà cung cấp")
ncc_label.grid(row=0, column=2, padx = 10)
ncc_combobox = ttk.Combobox(user_info_frame, values=["NCC001", "NCC002","NCC003", "NCC004"])
ncc_combobox.grid(row=1, column=2, padx = 10)

dvt_label = tkinter.Label(user_info_frame, text="ĐVT")
dvt_label.grid(row=2, column=0)
dvt_entry = tkinter.Entry(user_info_frame)
dvt_entry.grid(row=3, column=0)

dg_label = tkinter.Label(user_info_frame, text="Đơn giá")
dg_label.grid(row=2, column=1)
dg_entry = tkinter.Entry(user_info_frame)
dg_entry.grid(row=3, column=1)

nvql_label = tkinter.Label(user_info_frame, text="Nhân viên QL")
nvql_label.grid(row=2, column=2, padx = 10)
nvql_combobox = ttk.Combobox(user_info_frame, values=["NVK0001", "NVK0002"])
nvql_combobox.grid(row=3, column=2, padx = 10)

# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_NVL)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()