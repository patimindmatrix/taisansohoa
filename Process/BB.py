import tkinter
from tkinter import ttk
from tkinter import messagebox
def Create_DH():
    mabb = mabb_entry.get()
    tenbb =tenbb_entry.get()
    ngayviet = ngayviet_entry.get()
    nb = nb_entry.get()
    nvql = nvql_combobox.get()

    if not mabb or not tenbb or not ngayviet or not nb or not nvql :
        tkinter.messagebox.showwarning(title="Error", message="Thông tin không được bỏ trống")
    else:
        print("Mã NV: ", mabb, "Tên NV: ", tenbb, "Phòng ban: ", ngayviet)
        print("NB:  ", nb, "NVQL: ", nvql)
        print("------------------------------------------")

window = tkinter.Tk()
window.title("Thêm mới Bài báo")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

mabb_label = tkinter.Label(user_info_frame, text="Mã bài báo")
mabb_label.grid(row=0, column=0, padx = 10)
mabb_entry = tkinter.Entry(user_info_frame)
mabb_entry.grid(row=1, column=0, padx = 10)

tenbb_label = tkinter.Label(user_info_frame, text="Tên bài báo")
tenbb_label.grid(row=0, column=1)
tenbb_entry = tkinter.Entry(user_info_frame)
tenbb_entry.grid(row=1, column=1)

nviet_label = tkinter.Label(user_info_frame, text="Ngày viết")
nviet_label.grid(row=0, column=2)
ngayviet_entry = tkinter.Entry(user_info_frame)
ngayviet_entry.grid(row=1, column=2)

nb_label = tkinter.Label(user_info_frame, text="Nhà báo")
nb_label.grid(row=2, column=0)
nb_entry = tkinter.Entry(user_info_frame)
nb_entry.grid(row=3, column=0)

nvql_label = tkinter.Label(user_info_frame, text="Nhân viên QL")
nvql_label.grid(row=2, column=1)
nvql_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002","NVNS003",])
nvql_combobox.grid(row=3, column=1)

# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_DH)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()