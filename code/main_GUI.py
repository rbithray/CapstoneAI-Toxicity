import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from llms.load_model import load_ollama_model  # Updated import
from scoring.get_scores import get_responses_scores
import threading


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

        # System prompt input
        ttk.Label(root, text="System Prompt:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.system_prompt_text = tk.Text(root, width=50, height=4)
        self.system_prompt_text.grid(row=1, column=1, padx=10, pady=10)

        # Loaded model label
        ttk.Label(root, text="Loaded Model:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.loaded_model_label = ttk.Label(root, text="None", anchor="w")
        self.loaded_model_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Results display
        ttk.Label(root, text="Results:").grid(row=3, column=0, padx=10, pady=10, sticky="nw")
        self.results_text = tk.Text(root, width=50, height=20, state="disabled")
        self.results_text.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        self.load_model_button = ttk.Button(root, text="Load Model", command=self.load_selected_model)
        self.load_model_button.grid(row=4, column=0, padx=10, pady=10)
        self.kill_model_button = ttk.Button(root, text="Kill Model", command=self.kill_model)
        self.kill_model_button.grid(row=4, column=1, padx=10, pady=10)
        self.load_prompts_button = ttk.Button(root, text="Load Prompts", command=self.load_prompts)
        self.load_prompts_button.grid(row=5, column=0, padx=10, pady=10)
        self.run_button = ttk.Button(root, text="Run Prompts", command=self.run_prompts)
        self.run_button.grid(row=5, column=1, padx=10, pady=10)
        self.save_button = ttk.Button(root, text="Save Results", command=self.save_results)
        self.save_button.grid(row=6, column=0, padx=10, pady=10)

        # Initialize state variables
        self.query_model = None
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

        # Get the system prompt
        system_prompt = self.system_prompt_text.get("1.0", tk.END).strip()

        # Load the model with the system prompt
        try:
            self.query_model = load_ollama_model(internal_model_name, system_prompt=system_prompt)
            self.loaded_model_label.config(text=model_name)
            messagebox.showinfo("Info", f"{model_name} ({internal_model_name}) successfully loaded with system prompt!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {e}")

    def kill_model(self):
        if not self.query_model:
            messagebox.showwarning("Warning", "No model is currently loaded!")
            return

        # Unload the model
        self.query_model = None
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

            # Validate the structure of the JSON file
            if not isinstance(prompts, dict) or "text" not in prompts:
                raise ValueError("Invalid format in prompts file. Expected a dictionary with a 'text' key.")

            self.prompts = prompts["text"]
            messagebox.showinfo("Info", f"Prompts loaded successfully from {file_path}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load prompts: {e}")

    def run_prompts(self):
        if not self.query_model:
            messagebox.showwarning("Warning", "No model loaded!")
            return

        if not self.prompts:
            messagebox.showwarning("Warning", "No prompts loaded!")
            return

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
                self.results = get_responses_scores(list(self.prompts.values()), self.query_model, update_callback=update_gui_text)
                self.results_text.config(state="disabled")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                self.run_button.config(state="normal")

        threading.Thread(target=process_prompts, daemon=True).start()

    def save_results(self):
        if not self.results:
            messagebox.showwarning("Warning", "No results to save!")
            return

        model_name = self.model_var.get()
        if not model_name:
            messagebox.showwarning("Warning", "Model name is missing!")
            return

        file_name = f"../data/{model_name}_results.json"
        try:
            with open(file_name, "w") as f:
                json.dump(self.results, f, indent=4)
            messagebox.showinfo("Info", f"Results saved to {file_name}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save results: {e}")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LmToxicityGUI(root)
    root.mainloop()
