import customtkinter as ctk
from tkinter import messagebox

class DoujinShoppingListApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("同人誌即売会買い物リスト入力ツール")
        self.geometry("600x400")

        # テキスト表示エリア
        self.text_display = ctk.CTkTextbox(self, height=3, width=70, font=("Arial", 14))
        self.text_display.pack(pady=10, fill="both", expand=True)

        # フレーム作成
        self.frame_categories = ctk.CTkFrame(self)
        self.frame_categories.pack(pady=5, fill="x")
        self.frame_quantity = ctk.CTkFrame(self)
        self.frame_quantity.pack(pady=5, fill="x")
        self.frame_price = ctk.CTkFrame(self)
        self.frame_price.pack(pady=5, fill="x")
        self.frame_numpad = ctk.CTkFrame(self)
        self.frame_numpad.pack(pady=5, fill="x")
        self.frame_copy = ctk.CTkFrame(self)
        self.frame_copy.pack(pady=10, fill="x")

        # カテゴリボタン
        categories = ["新刊", "既刊", "新刊セット", "グッズ", "その他", "/"]
        for cat in categories:
            btn = ctk.CTkButton(self.frame_categories, text=cat, font=("Arial", 14), width=80, command=lambda c=cat: self.append_text(c))
            btn.pack(side="left", padx=4, pady=4)

        # 数量ボタン
        quantities = ["部", "個"]  # 「つ」ボタンを削除
        for qty in quantities:
            btn = ctk.CTkButton(self.frame_quantity, text=qty, font=("Arial", 14), width=80, command=lambda q=qty: self.append_text(q))
            btn.pack(side="left", padx=4, pady=4)

        # 「1部」「1セット」ボタン追加
        one_unit_buttons = ["1部", "1セット"]
        for unit in one_unit_buttons:
            btn = ctk.CTkButton(self.frame_quantity, text=unit, font=("Arial", 14), width=80, command=lambda u=unit: self.append_text(u))
            btn.pack(side="left", padx=4, pady=4)

        # 価格ボタン
        prices = ["500円", "1000円", "1500円", "2000円", "3000円"]
        for price in prices:
            btn = ctk.CTkButton(self.frame_price, text=price, font=("Arial", 14), width=80, command=lambda p=price: self.append_text(p))
            btn.pack(side="left", padx=4, pady=4)

        # テンキーボタン
        numpad_buttons = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "0", "00", "000"
        ]
        for i, num in enumerate(numpad_buttons):
            btn = ctk.CTkButton(self.frame_numpad, text=num, font=("Arial", 14), width=60, command=lambda n=num: self.append_text(n))
            btn.grid(row=i//3, column=i%3, padx=2, pady=2)

        # テンキーフレームのグリッド設定で均等割り当て
        for i in range(4):
            self.frame_numpad.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.frame_numpad.grid_columnconfigure(j, weight=1)

        # コピー用ボタン
        copy_btn = ctk.CTkButton(self.frame_copy, text="コピー", font=("Arial", 12), width=120, command=self.copy_to_clipboard)
        copy_btn.pack(padx=2, pady=2)

        # クリア用ボタン
        clear_btn = ctk.CTkButton(self.frame_copy, text="クリア", font=("Arial", 12), width=120, command=self.clear_text)
        clear_btn.pack(padx=2, pady=2)

    def append_text(self, text):
        current_text = self.text_display.get("1.0", "end-1c")

        # 「/」ボタンは区切りとして扱う（スペースなし）
        if text == "/":
            self.text_display.insert("end", "/")
            return

        # 数字（0-9, 00）の場合は連結する（スペースなし）
        if text.isdigit() or text == "00":
            if current_text and current_text[-1].isdigit():
                self.text_display.insert("end", text)
            else:
                self.text_display.insert("end", text)
            return

        # それ以外の文字はスペースを入れずに追加（連結）
        self.text_display.insert("end", text)

    def copy_to_clipboard(self):
        text = self.text_display.get("1.0", "end-1c").strip()
        if text:
            self.clipboard_clear()
            self.clipboard_append(text)
            messagebox.showinfo("コピー完了", "テキストをクリップボードにコピーしました。")
        else:
            messagebox.showwarning("警告", "コピーするテキストがありません。")

    def clear_text(self):
        self.text_display.delete("1.0", "end")

def main():
    app = DoujinShoppingListApp()
    app.mainloop()

if __name__ == "__main__":
    main()
