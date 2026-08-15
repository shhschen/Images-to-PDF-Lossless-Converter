import os
import img2pdf
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_images_to_pdf(image_paths: list[str], output_pdf: Path):
    if not image_paths:
        messagebox.showerror("錯誤", "沒有選擇任何圖片檔案！")
        return

    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(image_paths))

    messagebox.showinfo("完成", f"已產出 PDF：{output_pdf}")

def select_images():
    files = filedialog.askopenfilenames(filetypes=[("圖片檔案", "*.png *.jpg *.jpeg *.bmp")])
    if files:
        input_files.clear()
        input_files.extend(files)
        selected_label.config(text=f"已選擇 {len(files)} 張圖片")

def export_pdf():
    if not input_files:
        messagebox.showerror("錯誤", "請先選擇圖片檔案")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if output_file:
        convert_images_to_pdf(sorted(input_files, key=lambda x: x.lower()), Path(output_file))

# GUI
root = tk.Tk()
root.title("圖片轉 PDF 電子書工具")
root.geometry("400x200")

input_files = []

tk.Button(root, text="選擇圖片檔案（可多選）", command=select_images).pack(pady=10)
selected_label = tk.Label(root, text="尚未選擇圖片")
selected_label.pack()

tk.Button(root, text="匯出 PDF", command=export_pdf, bg="green", fg="white").pack(pady=20)

root.mainloop()