import tkinter
from tkinter import ttk
from tkinter import messagebox
def Create_KH():
    makh = makh_entry.get()
    tenkh = tenkh_entry.get()
    sdt = sdt_entry.get()
    email = email_entry.get()
    mst = mst_entry.get()
    dc = dc_entry.get()
    hd = hd_combobox.get()
    if not makh or not tenkh:
        tkinter.messagebox.showwarning(title="Error", message="Mã KH bắt buộc nhập")
    else:
        print("Mã KH: ", makh, "Tên KH: ", tenkh, "Hợp đồng: ", hd)
        print("SDT:  ", sdt, "Email: ", email, "Mã số thuế:", mst)
        print("Địa chỉ: ", dc)
        print("------------------------------------------")

window = tkinter.Tk()
window.title("Thêm mới khách hàng")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

makh_label = tkinter.Label(user_info_frame, text="Mã KH")
makh_label.grid(row=0, column=0, padx = 10)
makh_entry = tkinter.Entry(user_info_frame)
makh_entry.grid(row=1, column=0, padx = 10)

tenkh_label = tkinter.Label(user_info_frame, text="Tên KH")
tenkh_label.grid(row=0, column=1)
tenkh_entry = tkinter.Entry(user_info_frame)
tenkh_entry.grid(row=1, column=1)

hd_label = tkinter.Label(user_info_frame, text="Hợp đồng")
hd_label.grid(row=0, column=2, padx = 10)
hd_combobox = ttk.Combobox(user_info_frame, values=["223S001", "23P002", "23P003", "23S002", "23S003"])
hd_combobox.grid(row=1, column=2, padx = 10)

sdt_label = tkinter.Label(user_info_frame, text="SĐT")
sdt_label.grid(row=2, column=0)
sdt_entry = tkinter.Entry(user_info_frame)
sdt_entry.grid(row=3, column=0)

email_label = tkinter.Label(user_info_frame, text="Email")
email_label.grid(row=2, column=1)
email_entry = tkinter.Entry(user_info_frame)
email_entry.grid(row=3, column=1)

mst_label = tkinter.Label(user_info_frame, text="MST")
mst_label.grid(row=2, column=2)
mst_entry = tkinter.Entry(user_info_frame)
mst_entry.grid(row=3, column=2)

dc_label = tkinter.Label(user_info_frame, text="Địa chỉ")
dc_label.grid(row=4, column=0)
dc_entry = tkinter.Entry(user_info_frame)
dc_entry.grid(row=5, column=0)
# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_KH)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()