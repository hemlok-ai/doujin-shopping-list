import tkinter as tk
from tkinter import messagebox

class DoujinShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("同人誌即売会買い物リスト入力ツール")
        self.root.geometry("600x400")

        self.text_var = tk.StringVar()

        # テキスト表示エリア
        self.text_display = tk.Text(root, height=8, width=60, font=("Arial", 14))
        self.text_display.pack(pady=10)

        # フレーム作成
        self.frame_categories = tk.Frame(root)
        self.frame_categories.pack(pady=5)
        self.frame_quantity = tk.Frame(root)
        self.frame_quantity.pack(pady=5)
        self.frame_price = tk.Frame(root)
        self.frame_price.pack(pady=5)
        self.frame_numpad = tk.Frame(root)
        self.frame_numpad.pack(pady=5)
        self.frame_copy = tk.Frame(root)
        self.frame_copy.pack(pady=10)

        # カテゴリボタン
        categories = ["新刊", "既刊", "新刊セット", "グッズ", "その他", "/"]
        for cat in categories:
            btn = tk.Button(self.frame_categories, text=cat, width=8, command=lambda c=cat: self.append_text(c))
            btn.pack(side=tk.LEFT, padx=3)

        # 数量ボタン
        quantities = ["部", "個", "つ"]
        for qty in quantities:
            btn = tk.Button(self.frame_quantity, text=qty, width=8, command=lambda q=qty: self.append_text(q))
            btn.pack(side=tk.LEFT, padx=3)

        # 価格ボタン
        prices = ["500円", "1000円", "1500円", "2000円", "3000円"]
        for price in prices:
            btn = tk.Button(self.frame_price, text=price, width=8, command=lambda p=price: self.append_text(p))
            btn.pack(side=tk.LEFT, padx=3)

        # テンキーボタン
        numpad_buttons = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "0", "00"
        ]
        for i, num in enumerate(numpad_buttons):
            btn = tk.Button(self.frame_numpad, text=num, width=5, command=lambda n=num: self.append_text(n))
            btn.grid(row=i//3, column=i%3, padx=2, pady=2)

        # コピー用ボタン
        copy_btn = tk.Button(self.frame_copy, text="コピー", width=10, command=self.copy_to_clipboard)
        copy_btn.pack()

    def append_text(self, text):
        self.text_display.insert(tk.END, text)

    def copy_to_clipboard(self):
        text = self.text_display.get("1.0", tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("コピー完了", "テキストをクリップボードにコピーしました。")
        else:
            messagebox.showwarning("警告", "コピーするテキストがありません。")

def main():
    root = tk.Tk()
    app = DoujinShoppingListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
