import tkinter
from tkinter import ttk
from tkinter import messagebox
def Create_DH():
    madh = madh_entry.get()
    ngaytao =ngaytao_entry.get()
    tongtien = tt_entry.get()
    kh = kh_combobox.get()
    nvcr = nvcr_combobox.get()
    sp = sp_combobox.get()

    if not madh or not ngaytao or not kh or not tongtien or not nvcr or not sp:
        tkinter.messagebox.showwarning(title="Error", message="Thông tin không được bỏ trống")
    else:
        print("Mã NV: ", madh, "Tên NV: ", ngaytao, "Phòng ban: ", kh)
        print("SDT:  ", tongtien, "Email: ", nvcr, "STK:", sp)
        print("------------------------------------------")

window = tkinter.Tk()
window.title("Thêm mới Đơn hàng")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

madh_label = tkinter.Label(user_info_frame, text="Mã ĐH")
madh_label.grid(row=0, column=0, padx = 10)
madh_entry = tkinter.Entry(user_info_frame)
madh_entry.grid(row=1, column=0, padx = 10)

ngaytao_label = tkinter.Label(user_info_frame, text="Ngày tạo")
ngaytao_label.grid(row=0, column=1)
ngaytao_entry = tkinter.Entry(user_info_frame)
ngaytao_entry.grid(row=1, column=1)

kh_label = tkinter.Label(user_info_frame, text="Khách hàng")
kh_label.grid(row=0, column=2, padx = 10)
kh_combobox = ttk.Combobox(user_info_frame, values=["KH0001", "KH0002","KH0003", "KH0004"])
kh_combobox.grid(row=1, column=2, padx = 10)

nvcr_label = tkinter.Label(user_info_frame, text="Nhân viên tạo")
nvcr_label.grid(row=2, column=0)
nvcr_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002","NVNS003",])
nvcr_combobox.grid(row=3, column=0)

sp_label = tkinter.Label(user_info_frame, text="Sản phẩm")
sp_label.grid(row=2, column=1)
sp_combobox = ttk.Combobox(user_info_frame, values=["10051GS-5", "7561CBMW-6","CL50AW01-000-HXN.MQY"])
sp_combobox.grid(row=3, column=1)

tt_label = tkinter.Label(user_info_frame, text="Tổng tiền")
tt_label.grid(row=2, column=2)
tt_entry = tkinter.Entry(user_info_frame)
tt_entry.grid(row=3, column=2)
# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_DH)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()