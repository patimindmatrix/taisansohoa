import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
def Create_TSCD():
    matscd = matscd_entry.get()
    tentscd = tentscd_entry.get()
    tt = tt_combobox.get()
    giatri = gt_entry.get()
    thsd = thsd_entry.get()
    ngaymua = ngaymua_entry.get()
    khauhao = kh_entry.get()
    pb = pb_combobox.get()
    nv = nv_combobox.get()
    if not matscd or not pb or not nv or not khauhao or not giatri or not thsd or not ngaymua:
        tkinter.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
    else:
        print("Mã TSCD: ", matscd, "Tên HĐ: ", tentscd, "Ngày tải lên: ", thsd, "ngày hợp đồng:", giatri)
        print("Nhân viên:  ", khauhao, "tệp: ", nv, "đối tượng:", ngaymua)
        print("------------------------------------------")
def Openfile():
    filepath = filedialog.askopenfilename()

window = tkinter.Tk()
window.title("Thêm mới TSCĐ")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

matscd_label = tkinter.Label(user_info_frame, text="Mã TSCĐ")
matscd_label.grid(row=0, column=0, padx = 10)
matscd_entry = tkinter.Entry(user_info_frame)
matscd_entry.grid(row=1, column=0, padx = 10)

tentscd_label = tkinter.Label(user_info_frame, text="Tên TSCĐ")
tentscd_label.grid(row=0, column=1)
tentscd_entry = tkinter.Entry(user_info_frame)
tentscd_entry.grid(row=1, column=1)

tt_label = tkinter.Label(user_info_frame, text="Tình trạng")
tt_label.grid(row=0, column=2, padx = 10)
tt_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
tt_combobox.grid(row=1, column=2, padx = 10)

gt_label = tkinter.Label(user_info_frame, text="Giá trị")
gt_label.grid(row=2, column=0)
gt_entry = tkinter.Entry(user_info_frame)
gt_entry.grid(row=3, column=0)

thsd_label = tkinter.Label(user_info_frame, text="THSD")
thsd_label.grid(row=2, column=2)
thsd_entry = tkinter.Entry(user_info_frame)
thsd_entry.grid(row=3, column=2)

ngaymua_label = tkinter.Label(user_info_frame, text="Ngày mua")
ngaymua_label.grid(row=2, column=1)
ngaymua_entry = tkinter.Entry(user_info_frame)
ngaymua_entry.grid(row=3, column=1)

khauhao_label = tkinter.Label(user_info_frame, text="Khấu hao")
khauhao_label.grid(row=4, column=0)
kh_entry = tkinter.Entry(user_info_frame)
kh_entry.grid(row=5, column=0)

pb_label = tkinter.Label(user_info_frame, text="Phòng ban")
pb_label.grid(row=4, column=1, padx = 10)
pb_combobox = ttk.Combobox(user_info_frame, values=["KH0001", "KH0002", "KH0003", "NCC001", "NCC002", "NCC003"])
pb_combobox.grid(row=5, column=1, padx = 10)

nv_label = tkinter.Label(user_info_frame, text="Nhân viên")
nv_label.grid(row=4, column=2, padx = 10)
nv_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
nv_combobox.grid(row=5, column=2, padx = 10)


# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_TSCD)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
window.mainloop()