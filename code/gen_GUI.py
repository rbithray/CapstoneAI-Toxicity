import json
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict, Tuple
from llms.load_model import load_model
from get_scores import get_responses_scores


# GUI Application
class LLMGUI:
	def __init__(self, root):
		self.root = root
		self.root.title("LLM Toxicity Checker")

		# Load models
		with open("llms/models.json", "r") as f:
			self.models = json.load(f).get("models", [])

		# Model selection
		ttk.Label(root, text="Select Model:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
		self.model_var = tk.StringVar()
		self.model_menu = ttk.Combobox(root, textvariable=self.model_var, values=self.models, state="readonly")
		self.model_menu.grid(row=0, column=1, padx=10, pady=10)

		# Prompt input
		ttk.Label(root, text="Enter Prompts (one per line):").grid(row=1, column=0, padx=10, pady=10, sticky="nw")
		self.prompt_text = tk.Text(root, width=50, height=10)
		self.prompt_text.grid(row=1, column=1, padx=10, pady=10)

		# Results display
		ttk.Label(root, text="Results:").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
		self.results_text = tk.Text(root, width=50, height=15, state="disabled")
		self.results_text.grid(row=2, column=1, padx=10, pady=10)

		# Buttons
		self.load_button = ttk.Button(root, text="Load Model", command=self.load_selected_model)
		self.load_button.grid(row=3, column=0, padx=10, pady=10)
		self.run_button = ttk.Button(root, text="Run Prompts", command=self.run_prompts)
		self.run_button.grid(row=3, column=1, padx=10, pady=10)
		self.save_button = ttk.Button(root, text="Save Results", command=self.save_results)
		self.save_button.grid(row=4, column=1, padx=10, pady=10)

		self.model = None
		self.results = []

	def load_selected_model(self):
		model_name = self.model_var.get()
		if not model_name:
			messagebox.showwarning("Warning", "Please select a model!")
			return
		self.model = load_model(model_name)
		messagebox.showinfo("Info", f"{self.model} successfully loaded!")

	def run_prompts(self):
		if not self.model:
			messagebox.showwarning("Warning", "No model loaded!")
			return

		prompts = self.prompt_text.get("1.0", tk.END).strip().split("\n")
		if not prompts or prompts == [""]:
			messagebox.showwarning("Warning", "Please enter prompts!")
			return

		def update_gui_text(message):
			self.results_text.config(state="normal")
			self.results_text.insert(tk.END, message)
			self.results_text.see(tk.END)  # Scroll to the latest text
			self.results_text.config(state="disabled")

		try:
			self.results_text.config(state="normal")
			self.results_text.delete("1.0", tk.END)  # Clear existing content
			self.results = get_responses_scores(prompts, self.model, update_callback=update_gui_text)
			self.results_text.config(state="disabled")
		except Exception as e:
			messagebox.showerror("Error", f"An error occurred: {e}")

	def save_results(self):
		if not self.results:
			messagebox.showwarning("Warning", "No results to save!")
			return

		model_name = self.model_var.get()
		if not model_name:
			messagebox.showwarning("Warning", "Model name is missing!")
			return

		results_dict = {
			prompt: {"response": response, "score": score}
			for prompt, response, score in self.results
		}
		file_name = f"{model_name}.json"
		try:
			with open(file_name, "w") as f:
				json.dump(results_dict, f, indent=4)
			messagebox.showinfo("Info", f"Results saved to {file_name}!")
		except Exception as e:
			messagebox.showerror("Error", f"Failed to save results: {e}")


# Run the application
if __name__ == "__main__":
	root = tk.Tk()
	app = LLMGUI(root)
	root.mainloop()
