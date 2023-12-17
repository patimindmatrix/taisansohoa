import tkinter
from tkinter import ttk
from tkinter import messagebox
def Create_NV():
    manv = manv_entry.get()
    tennv = tennv_entry.get()
    pb = pb_combobox.get()
    sdt = sdt_entry.get()
    email = email_entry.get()
    stknh = stknh_entry.get()
    dc = dc_entry.get()
    if not manv or not tennv:
        tkinter.messagebox.showwarning(title="Error", message="Mã NV bắt buộc nhập")
    else:
        print("Mã NV: ", manv, "Tên NV: ", tennv, "Phòng ban: ", pb)
        print("SDT:  ", sdt, "Email: ", email, "STK:", stknh)
        print("Địa chỉ: ", dc)
        print("------------------------------------------")

window = tkinter.Tk()
window.title("Thêm mới nhân viên")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

manv_label = tkinter.Label(user_info_frame, text="Mã NV")
manv_label.grid(row=0, column=0, padx = 10)
manv_entry = tkinter.Entry(user_info_frame)
manv_entry.grid(row=1, column=0, padx = 10)

tennv_label = tkinter.Label(user_info_frame, text="Tên NV")
tennv_label.grid(row=0, column=1)
tennv_entry = tkinter.Entry(user_info_frame)
tennv_entry.grid(row=1, column=1)

pb_label = tkinter.Label(user_info_frame, text="Phòng ban")
pb_label.grid(row=0, column=2, padx = 10)
pb_combobox = ttk.Combobox(user_info_frame, values=["Điều hành", "Nhân sự", "QC", "Kho", "Sản xuất"])
pb_combobox.grid(row=1, column=2, padx = 10)

sdt_label = tkinter.Label(user_info_frame, text="SĐT")
sdt_label.grid(row=2, column=0)
sdt_entry = tkinter.Entry(user_info_frame)
sdt_entry.grid(row=3, column=0)

email_label = tkinter.Label(user_info_frame, text="Email")
email_label.grid(row=2, column=1)
email_entry = tkinter.Entry(user_info_frame)
email_entry.grid(row=3, column=1)

stknh_label = tkinter.Label(user_info_frame, text="STK")
stknh_label.grid(row=2, column=2)
stknh_entry = tkinter.Entry(user_info_frame)
stknh_entry.grid(row=3, column=2)

mk_label = tkinter.Label(user_info_frame, text="Mật khẩu")
mk_label.grid(row=4, column=0)
mk_entry = tkinter.Entry(user_info_frame, show="*")
mk_entry.grid(row=5, column=0)

mkl_label = tkinter.Label(user_info_frame, text="Nhập lại MK")
mkl_label.grid(row=4, column=1)
mkl_entry = tkinter.Entry(user_info_frame, show="*")
mkl_entry.grid(row=5, column=1)

dc_label = tkinter.Label(user_info_frame, text="Địa chỉ")
dc_label.grid(row=6, column=0)
dc_entry = tkinter.Entry(user_info_frame)
dc_entry.grid(row=7, column=0)
# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_NV)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()