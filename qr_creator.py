import qrcode
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QRcode 生成器")
        self.root.geometry("400x300")

        self.label_url = tk.Label(root, text="請輸入要生成 QRcode 的網址：")
        self.label_url.pack()

        self.entry_url = tk.Entry(root, width=40, bg="pink")
        self.entry_url.pack()

        self.label_filename = tk.Label(root, text="請輸入要儲存 QRcode 的名稱：")
        self.label_filename.pack()

        self.entry_filename = tk.Entry(root, width=40, bg="pink")
        self.entry_filename.pack()

        # 創建選擇儲存位置按鈕
        self.button_select_path = tk.Button(root, text="選擇儲存位置", command=self.select_path, bg="pink")
        self.button_select_path.pack(pady=(10, 0))

        self.label_path = tk.Label(root)
        self.label_path.pack()

        # 創建生成按鈕
        self.button_generate = tk.Button(root, text="生成 QRcode", command=self.generate_qr_code, bg="pink")
        self.button_generate.pack(pady=(10, 0))

        self.selected_path = None

    def select_path(self):
        self.selected_path = filedialog.askdirectory()
        self.label_path.config(text=self.selected_path)

    def validate_filename(self, filename):
        # 檢查是否包含特殊符號
        special_chars = r"\/:*?\"<>|"
        if any(char in special_chars for char in filename):
            return False

        # 檢查長度是否合理
        if len(filename) > 20:
            return False

        return True

    def generate_qr_code(self):
        url = self.entry_url.get()
        filename_input = self.entry_filename.get()

        if not self.validate_filename(filename_input):
            messagebox.showerror("錯誤", "檔案名稱不合法。請避免使用特殊符號，且不超過20個字元。")
            return

        qr_filename = filename_input + ".png"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")

        if not self.selected_path:
            self.selected_path = str(Path.home() / "桌面")

        qr_path = os.path.join(self.selected_path, qr_filename)

        qr_img.save(qr_path)
        messagebox.showinfo("QRcode 生成器", f"已生成 QRcode 並儲存為 {qr_filename}，儲存於：{qr_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()