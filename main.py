import tkinter as tk
import tkinter.filedialog as fl
import pandas as pd

def main():
	def selectCSV():
		path = fl.askopenfilename(initialdir=".",filetypes=[("all file", "*")])
		if path:
			ent.delete(0, tk.END)
			ent.insert(0, path)
	
	def convert():
		path = ent.get()
		ans = ""
		try:
			df = pd.read_csv(path, header=None)
			for i, row in df.iterrows():
				for j, v in row.items():
					ans += str(v) + " & "
				ans = ans[:-3] + "\\\\\n"
		except:
				ans = "正しいパスを入力してください"
		ta.delete(1.0, tk.END)
		ta.insert(tk.END, ans)

	root = tk.Tk()
	root.title("csv2table")
	root.geometry("500x400")

	desc = tk.Label(root, text="CSVファイルをLaTeX-table形式に変換します", font=("", 16))
	desc.pack(pady=8)

	# ファイル選択フレーム
	frm = tk.Frame(root)
	frm.pack(pady=8)
	# CSVファイル選択ボタン
	btn = tk.Button(frm, text="CSVファイルを選択", font=("", 16), command=selectCSV)
	btn.pack()
	# ファイルパス選択エントリ
	ent = tk.Entry(frm, font=("", 16), width=64)
	ent.pack()

	# 変換フレーム
	frm2 = tk.Frame(root)
	frm2.pack(pady=4)
	# 変換開始ボタン
	btn2 = tk.Button(frm2, text="変換", font=("", 16), command=convert)
	btn2.pack()
	# 出力テキストエリア
	ta = tk.Text(frm2, font=("", 16), width=64)
	ta.pack()

	root.mainloop()

if __name__ == "__main__":
	main()

