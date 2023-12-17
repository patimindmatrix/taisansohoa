import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
def Create_CCDC():
    maccdc = maccdc_entry.get()
    tenccdc = tenccdc_entry.get()
    tt = tt_combobox.get()
    giatri = gt_entry.get()
    pb = pb_combobox.get()
    nv = nv_combobox.get()
    if not maccdc or not pb or not nv:
        tkinter.messagebox.showwarning(title="Error", message="Không được bỏ trống !!!")
    else:
        print("Mã TSCD: ", maccdc, "Tên HĐ: ", tenccdc, "ngày hợp đồng:", giatri)
        print( "tệp: ", nv)
        print("------------------------------------------")
def Openfile():
    filepath = filedialog.askopenfilename()

window = tkinter.Tk()
window.title("Thêm mới CCDC")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

maccdc_label = tkinter.Label(user_info_frame, text="Mã CCDC")
maccdc_label.grid(row=0, column=0, padx = 10)
maccdc_entry = tkinter.Entry(user_info_frame)
maccdc_entry.grid(row=1, column=0, padx = 10)

tenccdc_label = tkinter.Label(user_info_frame, text="Tên CCDC")
tenccdc_label.grid(row=0, column=1)
tenccdc_entry = tkinter.Entry(user_info_frame)
tenccdc_entry.grid(row=1, column=1)

tt_label = tkinter.Label(user_info_frame, text="Tình trạng")
tt_label.grid(row=0, column=2, padx = 10)
tt_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
tt_combobox.grid(row=1, column=2, padx = 10)

gt_label = tkinter.Label(user_info_frame, text="Giá trị")
gt_label.grid(row=2, column=0)
gt_entry = tkinter.Entry(user_info_frame)
gt_entry.grid(row=3, column=0)

pb_label = tkinter.Label(user_info_frame, text="Phòng ban")
pb_label.grid(row=2, column=1, padx = 10)
pb_combobox = ttk.Combobox(user_info_frame, values=["KH0001", "KH0002", "KH0003", "NCC001", "NCC002", "NCC003"])
pb_combobox.grid(row=3, column=1, padx = 10)

nv_label = tkinter.Label(user_info_frame, text="Nhân viên")
nv_label.grid(row=2, column=2, padx = 10)
nv_combobox = ttk.Combobox(user_info_frame, values=["NVNS001", "NVNS002", "NVNS003"])
nv_combobox.grid(row=3, column=2, padx = 10)


# Button
save_button= tkinter.Button(frame, text="Lưu", command=Create_CCDC)
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
window.mainloop()