import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import numpy as np
import mplcursors
import plotly.express as px
import plotly.graph_objects as go

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
        # 新機能追加: 追加したY軸を削除するためのボタンを追加
        self.remove_y_axis_btn = ttk.Button(graph_frame, text="Y軸削除", command=self.remove_y_axis_combobox)
        self.remove_y_axis_btn.grid(row=1, column=3, padx=5, pady=5)

        # グラフタイプ選択
        ttk.Label(graph_frame, text="グラフタイプ:").grid(row=2, column=0, padx=5, pady=5)
        self.graph_type = ttk.Combobox(graph_frame, values=["折れ線グラフ", "棒グラフ", "散布図", "ヒストグラム", "面グラフ", "箱ひげ図", "パイチャート"], state="readonly")
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

    def remove_y_axis_combobox(self):
        """追加されたY軸のコンボボックスを削除します（最低1つは残す）"""
        if len(self.y_axis_comboboxes) > 1:
            # 最後に追加されたコンボボックスを取得して削除
            combobox = self.y_axis_comboboxes.pop()
            combobox.destroy()
        else:
            messagebox.showinfo("情報", "最低1つのY軸は必要です")

    def create_graph(self):
        if self.df is None:
            messagebox.showwarning("警告", "データが読み込まれていません")
            return

        x_col = self.x_axis.get()
        y_cols = [cb.get() for cb in self.y_axis_comboboxes if cb.get()]
        if not y_cols:
            messagebox.showwarning("警告", "Y軸の列が選択されていません")
            return

        # カラーパレット（Plotly の標準カラーセットを利用）
        colors = px.colors.qualitative.Plotly

        # グラフ作成（グラフタイプに応じた処理）
        if self.graph_type.get() == "折れ線グラフ":
            fig = go.Figure()
            for i, col in enumerate(y_cols):
                fig.add_trace(go.Scatter(x=self.df[x_col], y=self.df[col],
                                          mode='lines+markers',
                                          name=col,
                                          marker=dict(color=colors[i % len(colors)])))
        elif self.graph_type.get() == "棒グラフ":
            fig = go.Figure()
            for i, col in enumerate(y_cols):
                fig.add_trace(go.Bar(x=self.df[x_col], y=self.df[col],
                                       name=col,
                                       marker_color=colors[i % len(colors)]))
            fig.update_layout(barmode='group')
        elif self.graph_type.get() == "ヒストグラム":
            fig = go.Figure()
            for i, col in enumerate(y_cols):
                fig.add_trace(go.Histogram(x=self.df[col],
                                           name=col,
                                           opacity=0.5,
                                           marker=dict(color=colors[i % len(colors)])))
            fig.update_layout(barmode='overlay')
        elif self.graph_type.get() == "面グラフ":
            fig = go.Figure()
            for i, col in enumerate(y_cols):
                fig.add_trace(go.Scatter(x=self.df[x_col], y=self.df[col],
                                          mode='lines',
                                          fill='tozeroy',
                                          name=col,
                                          marker=dict(color=colors[i % len(colors)])))
        elif self.graph_type.get() == "箱ひげ図":
            fig = go.Figure()
            for i, col in enumerate(y_cols):
                fig.add_trace(go.Box(y=self.df[col],
                                      name=col,
                                      marker=dict(color=colors[i % len(colors)])))
        elif self.graph_type.get() == "パイチャート":
            if len(y_cols) != 1:
                messagebox.showwarning("警告", "パイチャートは1つのY軸を選択してください")
                return
            fig = go.Figure(data=[go.Pie(labels=self.df[x_col], values=self.df[y_cols[0]], name=y_cols[0])])
        elif self.graph_type.get() == "散布図":
            fig = go.Figure()
            for i, col in enumerate(y_cols):
                fig.add_trace(go.Scatter(x=self.df[x_col], y=self.df[col],
                                          mode='markers',
                                          name=col,
                                          marker=dict(color=colors[i % len(colors)])))
        else:
            # それ以外の場合は散布図をデフォルトとする
            fig = go.Figure()
            for i, col in enumerate(y_cols):
                fig.add_trace(go.Scatter(x=self.df[x_col], y=self.df[col],
                                          mode='markers',
                                          name=col,
                                          marker=dict(color=colors[i % len(colors)])))

        # 軸ラベルの設定（ヒストグラム、箱ひげ図、パイチャート以外はX軸に指定列を使用）
        if self.graph_type.get() not in ["ヒストグラム", "箱ひげ図", "パイチャート"]:
            fig.update_xaxes(title_text=x_col)
            if len(y_cols) == 1:
                fig.update_yaxes(title_text=y_cols[0])
            else:
                fig.update_yaxes(title_text="値")

        # グラフタイトルの設定
        title_text = self.title_input.get()
        if not title_text:
            if self.graph_type.get() == "ヒストグラム":
                title_text = f"{', '.join(y_cols)} のヒストグラム"
            elif self.graph_type.get() == "箱ひげ図":
                title_text = f"{', '.join(y_cols)} の箱ひげ図"
            elif self.graph_type.get() == "パイチャート":
                title_text = f"{x_col} と {y_cols[0]} のパイチャート"
            elif self.graph_type.get() == "面グラフ":
                title_text = f"{x_col} と {', '.join(y_cols)} の面グラフ"
            else:
                if len(y_cols) == 1:
                    title_text = f"{x_col} と {y_cols[0]} に関するグラフ"
                else:
                    title_text = f"{x_col} と {', '.join(y_cols)} に関するグラフ"
        fig.update_layout(title=title_text, template="plotly_white")

        # Plotly はデフォルトでインタラクティブなツールチップなどを提供します
        self.figure = fig
        fig.show()

    def save_graph(self):
        if not hasattr(self, "figure") or self.figure is None:
            messagebox.showwarning("警告", "グラフが作成されていません")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG画像", "*.png"), ("JPEG画像", "*.jpg"), ("PDF文書", "*.pdf")]
        )
        if file_path:
            try:
                # Plotly でグラフを画像として保存する場合は、kaleido のインストールが必要です
                if file_path.endswith(".html"):
                    self.figure.write_html(file_path)
                else:
                    self.figure.write_image(file_path)
                messagebox.showinfo("成功", "グラフを保存しました")
            except Exception as e:
                messagebox.showerror("エラー", f"グラフの保存に失敗しました: {e}")

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