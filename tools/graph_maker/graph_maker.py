import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

class GraphMaker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("グラフメーカー")
        self.root.geometry("800x600")
        self.df = None
        self.setup_ui()

    def setup_ui(self):
        # ファイル選択部分
        file_frame = ttk.LabelFrame(self.root, text="ファイル選択", padding=10)
        file_frame.pack(fill="x", padx=5, pady=5)
        
        self.file_btn = ttk.Button(file_frame, text="ファイルを開く", command=self.load_file)
        self.file_btn.pack(side="left", padx=5)
        
        self.file_label = ttk.Label(file_frame, text="ファイルが選択されていません")
        self.file_label.pack(side="left", padx=5)

        # グラフ設定部分
        graph_frame = ttk.LabelFrame(self.root, text="グラフ設定", padding=10)
        graph_frame.pack(fill="x", padx=5, pady=5)

        # X軸選択
        ttk.Label(graph_frame, text="X軸:").grid(row=0, column=0, padx=5, pady=5)
        self.x_axis = ttk.Combobox(graph_frame, state="readonly")
        self.x_axis.grid(row=0, column=1, padx=5, pady=5)

        # Y軸選択
        ttk.Label(graph_frame, text="Y軸:").grid(row=1, column=0, padx=5, pady=5)
        self.y_axis = ttk.Combobox(graph_frame, state="readonly")
        self.y_axis.grid(row=1, column=1, padx=5, pady=5)

        # グラフタイプ選択
        ttk.Label(graph_frame, text="グラフタイプ:").grid(row=2, column=0, padx=5, pady=5)
        self.graph_type = ttk.Combobox(graph_frame, values=["折れ線グラフ", "棒グラフ", "散布図"], state="readonly")
        self.graph_type.set("折れ線グラフ")
        self.graph_type.grid(row=2, column=1, padx=5, pady=5)

        # ボタン類
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=5, pady=5)

        self.plot_btn = ttk.Button(button_frame, text="グラフ作成", command=self.create_graph)
        self.plot_btn.pack(side="left", padx=5)

        self.save_btn = ttk.Button(button_frame, text="グラフを保存", command=self.save_graph)
        self.save_btn.pack(side="left", padx=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel/CSVファイル", "*.xlsx *.xls *.csv")]
        )
        if not file_path:
            return

        try:
            if file_path.endswith('.csv'):
                self.df = pd.read_csv(file_path, encoding='utf-8')
            else:
                self.df = pd.read_excel(file_path)

            self.file_label.config(text=Path(file_path).name)
            self.update_columns()
            messagebox.showinfo("成功", "ファイルを読み込みました")
        except Exception as e:
            messagebox.showerror("エラー", f"ファイルの読み込みに失敗しました: {str(e)}")

    def update_columns(self):
        if self.df is not None:
            columns = self.df.columns.tolist()
            self.x_axis['values'] = columns
            self.y_axis['values'] = columns
            if columns:
                self.x_axis.set(columns[0])
                self.y_axis.set(columns[1] if len(columns) > 1 else columns[0])

    def create_graph(self):
        if self.df is None:
            messagebox.showwarning("警告", "データが読み込まれていません")
            return

        plt.figure(figsize=(10, 6))
        x_col = self.x_axis.get()
        y_col = self.y_axis.get()

        if self.graph_type.get() == "折れ線グラフ":
            plt.plot(self.df[x_col], self.df[y_col], marker='o')
        elif self.graph_type.get() == "棒グラフ":
            plt.bar(self.df[x_col], self.df[y_col])
        else:  # 散布図
            plt.scatter(self.df[x_col], self.df[y_col])

        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"{y_col} vs {x_col}")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def save_graph(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG画像", "*.png"), ("JPEG画像", "*.jpg"), ("PDF文書", "*.pdf")]
        )
        if file_path:
            plt.savefig(file_path, dpi=300, bbox_inches='tight')
            messagebox.showinfo("成功", "グラフを保存しました")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GraphMaker()
    app.run() 