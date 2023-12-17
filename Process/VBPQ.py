import tkinter
from tkinter import ttk
from tkinter import messagebox
def Create_DH():
    mavbpq = mavbpq_entry.get()
    tenvbpq = tenvbpq_entry.get()
    ngaybh = ngaybh_entry.get()
    nvbh =nvbh_combobox.get()
    nvql = nvql_combobox.get()

    if not mavbpq or not tenvbpq or not ngaybh or not nvbh or not nvql :
        tkinter.messagebox.showwarning(title="Error", message="Thông tin không được bỏ trống")
    else:
        print("Mã NV: ", mavbpq, "Tên NV: ", tenvbpq, "Phòng ban: ", ngaybh)
        print("NB:  ", nvbh, "NVQL: ", nvql)
        print("------------------------------------------")

window = tkinter.Tk()
window.title("Thêm mới VBPQ")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

mavbpq_label = tkinter.Label(user_info_frame, text="Mã VBPQ")
mavbpq_label.grid(row=0, column=0, padx = 10)
mavbpq_entry = tkinter.Entry(user_info_frame)
mavbpq_entry.grid(row=1, column=0, padx = 10)

tenvbpq_label = tkinter.Label(user_info_frame, text="Tên VBPQ")
tenvbpq_label.grid(row=0, column=1)
tenvbpq_entry = tkinter.Entry(user_info_frame)
tenvbpq_entry.grid(row=1, column=1)

ngaybh_label = tkinter.Label(user_info_frame, text="Ngày ban hành")
ngaybh_label.grid(row=0, column=2)
ngaybh_entry = tkinter.Entry(user_info_frame)
ngaybh_entry.grid(row=1, column=2)

nvbh_label = tkinter.Label(user_info_frame, text="Nhân viên BH")
nvbh_label.grid(row=2, column=0)
nvbh_combobox = ttk.Combobox(user_info_frame, values=["NVDH001", "NVDH002","NVDH003",])
nvbh_combobox.grid(row=3, column=0)

nvql_label = tkinter.Label(user_info_frame, text="Nhân viên QL")
nvql_label.grid(row=2, column=1)
nvql_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002","NVNS003",])
nvql_combobox.grid(row=3, column=1)

# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_DH)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()