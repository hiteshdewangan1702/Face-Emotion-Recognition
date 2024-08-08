import tkinter as tk
from tkinter import ttk
import subprocess

class PythonScriptRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face_Emotion_Recognition")
        self.root.geometry("400x200")  # Set the initial size

        # Set the window icon
        icon_path = "logo.ico"  # Replace with the actual path to your ICO file
        self.root.iconbitmap(default=icon_path)

        # Frame for radio buttons
        radio_frame = ttk.Frame(root)
        radio_frame.pack(side=tk.TOP, pady=10)

        self.selected_script = tk.StringVar()
        script_choices = ["Realtime", "ThroughVideo", "Fromimage"]

        for script_choice in script_choices:
            ttk.Radiobutton(radio_frame, text=script_choice, variable=self.selected_script, value=script_choice).pack(side=tk.LEFT, padx=5,pady=30)

        # Frame for buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(side=tk.BOTTOM)

        ttk.Button(button_frame, text="Check", command=self.run_selected_script).pack(side=tk.LEFT, padx=10,pady=30)
        ttk.Button(button_frame, text="Stop", command=self.stop_script).pack(side=tk.LEFT, padx=10,pady=30)

    def run_selected_script(self):
        selected_script = self.selected_script.get()

        if selected_script:
            print(f"Running {selected_script}...")
            # Terminate the existing process if any
            self.stop_script()

            # Start a new process
            self.process = subprocess.Popen(["python", f"{selected_script}.py"])

    def stop_script(self):
        if hasattr(self, 'process') and self.process and self.process.poll() is None:
            print("Stopping the current script...")
            self.process.terminate()
            self.process.wait()  # Wait for the process to finish

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonScriptRunnerApp(root)
    root.mainloop()
