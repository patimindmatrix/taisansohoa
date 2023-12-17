import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
def Create_HD():
    mahd = mahd_entry.get()
    tenhd = tenhd_entry.get()
    ngayhd = ngayhd_entry.get()
    ngaytailen = ngaytailen_entry.get()
    nguoitao = ngt_combobox.get()
    doituong = dt_combobox.get()
    tepdinhkem = tepdinhkem_btn.get()
    if not mahd or not tepdinhkem or not nguoitao or not doituong:
        tkinter.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
    else:
        print("Mã HĐ: ", mahd, "Tên HĐ: ", tenhd, "Ngày tải lên: ", ngaytailen, "ngày hợp đồng:", ngayhd)
        print("Nhân viên:  ", nguoitao, "tệp: ", tepdinhkem, "đối tượng:", doituong)
        print("------------------------------------------")
def Openfile():
    filepath = filedialog.askopenfilename()

window = tkinter.Tk()
window.title("Thêm mới hợp đồng")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

mahd_label = tkinter.Label(user_info_frame, text="Mã HĐ")
mahd_label.grid(row=0, column=0, padx = 10)
mahd_entry = tkinter.Entry(user_info_frame)
mahd_entry.grid(row=1, column=0, padx = 10)

tenhd_label = tkinter.Label(user_info_frame, text="Tên HĐ")
tenhd_label.grid(row=0, column=1)
tenhd_entry = tkinter.Entry(user_info_frame)
tenhd_entry.grid(row=1, column=1)

ngt_label = tkinter.Label(user_info_frame, text="Nhân viên")
ngt_label.grid(row=0, column=2, padx = 10)
ngt_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
ngt_combobox.grid(row=1, column=2, padx = 10)

ngayhd_label = tkinter.Label(user_info_frame, text="Ngày hợp đồng")
ngayhd_label.grid(row=2, column=0)
ngayhd_entry = tkinter.Entry(user_info_frame)
ngayhd_entry.grid(row=3, column=0)

ngaytailen_label = tkinter.Label(user_info_frame, text="Ngày tải lên")
ngaytailen_label.grid(row=2, column=1)
ngaytailen_entry = tkinter.Entry(user_info_frame)
ngaytailen_entry.grid(row=3, column=1)

tepdinhkem_label = tkinter.Label(user_info_frame, text="Tệp")
tepdinhkem_label.grid(row=2, column=2)
tepdinhkem_btn = tkinter.Button(user_info_frame)
tepdinhkem_btn.grid(row=3, column=2, command = Openfile())
tepdinhkem_btn.config(width=18, height=1, text = "Chọn tệp")

dt_label = tkinter.Label(user_info_frame, text="Đối tượng")
dt_label.grid(row=4, column=0, padx = 10)
dt_combobox = ttk.Combobox(user_info_frame, values=["KH0001", "KH0002", "KH0003", "NCC001", "NCC002", "NCC003"])
dt_combobox.grid(row=5, column=0, padx = 10)
# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_HD)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()