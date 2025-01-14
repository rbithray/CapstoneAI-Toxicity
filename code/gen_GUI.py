import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import List, Dict, Tuple
from llms.load_model import load_model
from get_scores import get_responses_scores
import threading


# GUI Application
class LmToxicityGUI:
	def __init__(self, root):
		self.root = root
		self.root.title("LLM Toxicity Checker")

		# Load model mapping from JSON
		with open("llms/models.json", "r") as f:
			self.model_mapping = json.load(f).get("models", {})
			self.models = list(self.model_mapping.keys())  # Extract keys for dropdown

		# Model selection dropdown
		ttk.Label(root, text="Select Model:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
		self.model_var = tk.StringVar()
		self.model_menu = ttk.Combobox(root, textvariable=self.model_var, values=self.models, state="readonly")
		self.model_menu.grid(row=0, column=1, padx=10, pady=10)

		# Loaded model label
		ttk.Label(root, text="Loaded Model:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
		self.loaded_model_label = ttk.Label(root, text="None", anchor="w")
		self.loaded_model_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

		# Results display
		ttk.Label(root, text="Results:").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
		self.results_text = tk.Text(root, width=50, height=20, state="disabled")
		self.results_text.grid(row=2, column=1, padx=10, pady=10)

		# Buttons
		self.load_model_button = ttk.Button(root, text="Load Model", command=self.load_selected_model)
		self.load_model_button.grid(row=3, column=0, padx=10, pady=10)
		self.kill_model_button = ttk.Button(root, text="Kill Model", command=self.kill_model)
		self.kill_model_button.grid(row=3, column=1, padx=10, pady=10)
		self.load_prompts_button = ttk.Button(root, text="Load Prompts", command=self.load_prompts)
		self.load_prompts_button.grid(row=4, column=0, padx=10, pady=10)
		self.run_button = ttk.Button(root, text="Run Prompts", command=self.run_prompts)
		self.run_button.grid(row=4, column=1, padx=10, pady=10)
		self.save_button = ttk.Button(root, text="Save Results", command=self.save_results)
		self.save_button.grid(row=5, column=0, padx=10, pady=10)

		# Initialize state variables
		self.model = None
		self.prompts = []
		self.results = []

	def load_selected_model(self):
		model_name = self.model_var.get()
		if not model_name:
			messagebox.showwarning("Warning", "Please select a model!")
			return

		# Get the internal identifier for the selected model
		internal_model_name = self.model_mapping.get(model_name)
		if not internal_model_name:
			messagebox.showerror("Error", f"Model '{model_name}' not found in mapping!")
			return

		# Load the model using the internal identifier
		self.model = load_model(internal_model_name)
		self.loaded_model_label.config(text=model_name)
		messagebox.showinfo("Info", f"{model_name} ({internal_model_name}) successfully loaded!")

	def kill_model(self):
		if not self.model:
			messagebox.showwarning("Warning", "No model is currently loaded!")
			return

		# Unload the model
		self.model = None
		self.loaded_model_label.config(text="None")
		messagebox.showinfo("Info", "The currently loaded model has been killed!")

	def load_prompts(self):
		file_path = filedialog.askopenfilename(
			title="Select Prompts File",
			filetypes=[("JSON Files", "*.json")]
		)
		if not file_path:
			return

		try:
			with open(file_path, "r") as f:
				prompts = json.load(f)
			if not isinstance(prompts, list) or not all(isinstance(p, str) for p in prompts):
				raise ValueError("Invalid format in prompts file. Expected a list of strings.")
			self.prompts = prompts
			messagebox.showinfo("Info", f"Prompts loaded successfully from {file_path}!")
		except Exception as e:
			messagebox.showerror("Error", f"Failed to load prompts: {e}")

	def run_prompts(self):
		if not self.model:
			messagebox.showwarning("Warning", "No model loaded!")
			return

		if not self.prompts:
			messagebox.showwarning("Warning", "No prompts loaded!")
			return

		# Disable the run button while processing
		self.run_button.config(state="disabled")

		def update_gui_text(message):
			self.results_text.config(state="normal")
			self.results_text.insert(tk.END, message + "\n")
			self.results_text.see(tk.END)
			self.results_text.config(state="disabled")

		def process_prompts():
			try:
				self.results_text.config(state="normal")
				self.results_text.delete("1.0", tk.END)
				self.results = get_responses_scores(self.prompts, self.model, update_callback=update_gui_text)
				self.results_text.config(state="disabled")
			except Exception as e:
				messagebox.showerror("Error", f"An error occurred: {e}")
			finally:
				# Re-enable the run button after processing
				self.run_button.config(state="normal")

		# Start the processing in a separate thread
		threading.Thread(target=process_prompts, daemon=True).start()

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
	app = LmToxicityGUI(root)
	root.mainloop()
