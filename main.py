import customtkinter as ctk
import tkinter.filedialog as fl
import numpy as np

FONT_TYPE = "meiryo"

class App(ctk.CTk):
  
	def __init__(self):
		super().__init__()
		
		# メンバ変数の設定
		self.fonts = (FONT_TYPE, 12, "bold")
		self.csv_filepath = ""

		# フォームのセットアップ
		self.setup_form()
	
	def setup_form(self):
		# CustomTktinterのデザイン設定
		ctk.set_appearance_mode("light")
		ctk.set_default_color_theme("blue")

		# フォームサイズ・タイトル設定
		self.geometry("1000x500")
		self.title("CSV2LaTeX_Table")

		# root_frame
		self.grid_rowconfigure(1, weight=1)			# 1行目をレスポンシブ化
		self.grid_columnconfigure(0, weight=1)	# 0列目をレスポンシブ化
		self.read_file_frame = ctk.CTkFrame(master=self)
		self.read_file_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
		self.output_frame = ctk.CTkFrame(master=self)
		self.output_frame.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="ewns")

		# read_file_frame
		self.read_file_frame.grid_columnconfigure(0, weight=1)
		self.read_file_label = ctk.CTkLabel(master=self.read_file_frame, text="ファイル読み込み", font=(FONT_TYPE, 10))
		self.read_file_label.grid(row=0, column=0, padx=10, pady=(4, 0), sticky="w")
		self.read_file_entry = ctk.CTkEntry(master=self.read_file_frame, placeholder_text="CSVファイルを読み込む", font=self.fonts, width=200)
		self.read_file_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")
		self.read_file_button = ctk.CTkButton(master=self.read_file_frame, text="ファイル選択", font=self.fonts, command=self.read_file_button_callback)
		self.read_file_button.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="e")
		self.convert_button = ctk.CTkButton(master=self.read_file_frame, text="変換", font=self.fonts, command=self.convert_button_callback)
		self.convert_button.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="e")

		# main_frame
		self.output_frame.grid_rowconfigure(1, weight=1)
		self.output_frame.grid_columnconfigure(0, weight=1)
		self.output_label = ctk.CTkLabel(master=self.output_frame, text="出力", font=(FONT_TYPE, 10))
		self.output_label.grid(row=0, column=0, padx=10, pady=(4, 0), sticky="w")
		self.output_text = ctk.CTkTextbox(master=self.output_frame, font=self.fonts)
		self.output_text.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ewns")

	def read_file_button_callback(self):
		path = fl.askopenfilename(initialdir=".", filetypes=[("csv file", "*.csv")])
		if path:
			self.read_file_entry.delete(0, ctk.END)
			self.read_file_entry.insert(0, path)

	def convert_button_callback(self):
		path = self.read_file_entry.get()
		ans = ""
		try:
			data = np.loadtxt(path, delimiter=",", dtype="unicode")
			for row in data:
				for value in row:
					ans += str(value).strip() + " & "
				ans = ans[:-3] + "\\\\\n"
		except:
			ans = "ファイルの読み込みに失敗しました"
		self.output_text.delete(1.0, ctk.END)
		self.output_text.insert(ctk.END, ans)

if __name__ == "__main__":
	app = App()
	app.mainloop()