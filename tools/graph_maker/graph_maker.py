import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import numpy as np

class GraphMaker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("グラフメーカー")
        self.root.geometry("800x600")
        self.df = None
        self.figure = None  # 作成したグラフを保存するための変数
        self.setup_ui()

    def setup_ui(self):
        # ファイル選択部分
        file_frame = ttk.LabelFrame(self.root, text="ファイル選択", padding=10)
        file_frame.pack(fill="x", padx=5, pady=5)
        
        self.file_btn = ttk.Button(file_frame, text="ファイルを開く", command=self.load_file)
        self.file_btn.pack(side="left", padx=5)
        
        self.file_label = ttk.Label(file_frame, text="ファイルが選択されていません")
        self.file_label.pack(side="left", padx=5)
        
        # 新機能追加: データプレビュー用ボタンを追加
        self.preview_btn = ttk.Button(file_frame, text="データプレビュー", command=self.preview_data)
        self.preview_btn.pack(side="left", padx=5)

        # グラフ設定部分
        graph_frame = ttk.LabelFrame(self.root, text="グラフ設定", padding=10)
        graph_frame.pack(fill="x", padx=5, pady=5)

        # X軸選択
        ttk.Label(graph_frame, text="X軸:").grid(row=0, column=0, padx=5, pady=5)
        self.x_axis = ttk.Combobox(graph_frame, state="readonly")
        self.x_axis.grid(row=0, column=1, padx=5, pady=5)

        # Y軸選択（プルダウンで追加可能）
        ttk.Label(graph_frame, text="Y軸:").grid(row=1, column=0, padx=5, pady=5)
        self.y_axis_frame = ttk.Frame(graph_frame)
        self.y_axis_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.y_axis_comboboxes = []
        self.add_y_axis_combobox()
        self.add_y_axis_btn = ttk.Button(graph_frame, text="Y軸追加", command=self.add_y_axis_combobox)
        self.add_y_axis_btn.grid(row=1, column=2, padx=5, pady=5)

        # グラフタイプ選択
        ttk.Label(graph_frame, text="グラフタイプ:").grid(row=2, column=0, padx=5, pady=5)
        self.graph_type = ttk.Combobox(graph_frame, values=["折れ線グラフ", "棒グラフ", "散布図", "ヒストグラム"], state="readonly")
        self.graph_type.set("折れ線グラフ")
        self.graph_type.grid(row=2, column=1, padx=5, pady=5)
        
        # 新機能追加: グラフタイトル入力フィールドを追加
        ttk.Label(graph_frame, text="グラフタイトル:").grid(row=3, column=0, padx=5, pady=5)
        self.title_input = ttk.Entry(graph_frame)
        self.title_input.grid(row=3, column=1, padx=5, pady=5)
        
        # 新機能追加: グリッド表示のオンオフを切り替えるチェックボックスを追加
        self.grid_var = tk.BooleanVar(value=True)
        self.grid_check = ttk.Checkbutton(graph_frame, text="グリッド表示", variable=self.grid_var)
        self.grid_check.grid(row=4, column=1, padx=5, pady=5, sticky="w")

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
            if columns:
                self.x_axis.set(columns[0])
            for combobox in self.y_axis_comboboxes:
                combobox['values'] = columns
                if not combobox.get() and columns:
                    combobox.set(columns[0])

    def add_y_axis_combobox(self):
        """新しいY軸用のコンボボックスを追加します"""
        combobox = ttk.Combobox(self.y_axis_frame, state="readonly")
        combobox.pack(fill="x", pady=2)
        self.y_axis_comboboxes.append(combobox)
        if self.df is not None:
            columns = self.df.columns.tolist()
            combobox['values'] = columns
            if columns:
                combobox.set(columns[0])

    def create_graph(self):
        if self.df is None:
            messagebox.showwarning("警告", "データが読み込まれていません")
            return

        # グラフ作成: オブジェクト指向のAPIを利用してサブプロットを生成（サイズは10×6）
        self.figure, ax = plt.subplots(figsize=(10, 6))
        x_col = self.x_axis.get()
        y_cols = [cb.get() for cb in self.y_axis_comboboxes if cb.get()]
        if not y_cols:
            messagebox.showwarning("警告", "Y軸の列が選択されていません")
            return

        # 各系列に色を割り当てる
        colors = plt.rcParams['axes.prop_cycle'].by_key().get('color', ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan'])

        if self.graph_type.get() == "折れ線グラフ":
            for i, col in enumerate(y_cols):
                ax.plot(self.df[x_col], self.df[col], marker='o', label=col, color=colors[i % len(colors)])
            ax.legend()
        elif self.graph_type.get() == "棒グラフ":
            positions = np.arange(len(self.df[x_col]))
            num = len(y_cols)
            bar_width = 0.8 / num
            for i, col in enumerate(y_cols):
                offset = (i - num/2) * bar_width + bar_width/2
                ax.bar(positions + offset, self.df[col], width=bar_width, label=col, color=colors[i % len(colors)])
            ax.xticks(positions, self.df[x_col], rotation=45, fontsize=8)
            ax.legend()
        elif self.graph_type.get() == "ヒストグラム":
            for i, col in enumerate(y_cols):
                ax.hist(self.df[col], label=col, alpha=0.5, color=colors[i % len(colors)])
            ax.legend()
        else:  # 散布図
            for i, col in enumerate(y_cols):
                ax.scatter(self.df[x_col], self.df[col], label=col, color=colors[i % len(colors)])
            ax.legend()

        # 軸のラベルを日本語で設定
        ax.set_xlabel(x_col)
        if len(y_cols) == 1:
            ax.set_ylabel(y_cols[0])
        else:
            ax.set_ylabel("値")
        
        # グラフタイトルを日本語で設定
        title_text = self.title_input.get()
        if title_text:
            ax.set_title(title_text)
        else:
            if len(y_cols) == 1:
                ax.set_title(f"{x_col} と {y_cols[0]} に関するグラフ")
            else:
                ax.set_title(f"{x_col} と {', '.join(y_cols)} に関するグラフ")
        
        # グリッド表示（横線のみ）の設定（日本語コメント）
        if self.grid_var.get():
            ax.grid(True, axis='y')
        else:
            ax.grid(False)

        # 横軸ラベルが重ならないように調整する (棒グラフ以外の場合)
        if self.graph_type.get() != "棒グラフ":
            if pd.api.types.is_numeric_dtype(self.df[x_col]):
                ax.locator_params(axis='x', nbins=10)
                ax.set_xticks(rotation=45, fontsize=8)
            else:
                labels = [label.get_text() for label in ax.get_xticklabels()]
                if len(labels) > 10:
                    step = max(1, int(len(labels) / 10))
                    new_labels = [labels[i] if i % step == 0 else '' for i in range(len(labels))]
                    ax.set_xticklabels(new_labels, rotation=45, fontsize=8)
                else:
                    ax.set_xticks(rotation=45, fontsize=8)
        # サブプロットの配置を自動調整（日本語コメント）
        plt.tight_layout()
        plt.show()

    def save_graph(self):
        if not hasattr(self, "figure") or self.figure is None:
            messagebox.showwarning("警告", "グラフが作成されていません")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG画像", "*.png"), ("JPEG画像", "*.jpg"), ("PDF文書", "*.pdf")]
        )
        if file_path:
            # 新機能変更: 自身のfigureを使ってグラフを保存
            self.figure.savefig(file_path, dpi=300, bbox_inches='tight')
            messagebox.showinfo("成功", "グラフを保存しました")

    # 新機能追加: 読み込んだデータのプレビュー表示
    def preview_data(self):
        if self.df is None:
            messagebox.showwarning("警告", "データが読み込まれていません")
            return

        preview_win = tk.Toplevel(self.root)
        preview_win.title("データプレビュー")
        preview_win.geometry("600x400")

        tree = ttk.Treeview(preview_win)
        tree.pack(expand=True, fill='both')

        tree["columns"] = list(self.df.columns)
        tree["show"] = "headings"
        for column in self.df.columns:
            tree.heading(column, text=column)
            tree.column(column, width=100)
        for index, row in self.df.head(10).iterrows():
            tree.insert("", "end", values=list(row))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GraphMaker()
    app.run() 