import tkinter as tk
from tkinter import messagebox, filedialog
import threading

from detector import Detector
from report_generator import ReportGenerator
from process_monitor import ProcessMonitor
from startup_checker import StartupChecker


class KeyloggerDetectorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger Detection and Mitigation System")
        master.geometry("800x500")

        # Modules
        self.detector = Detector()
        self.report_generator = ReportGenerator()
        self.process_monitor = ProcessMonitor()
        self.startup_checker = StartupChecker()

        # Buttons
        self.info_button = tk.Button(
            master,
            text="Info",
            command=self.show_info
        )
        self.info_button.grid(row=0, column=0, padx=5, pady=5)

        self.listen_button = tk.Button(
            master,
            text="Scan File",
            command=self.start_scanning
        )
        self.listen_button.grid(row=0, column=1, padx=5, pady=5)

        self.add_program_button = tk.Button(
            master,
            text="Add Program",
            command=self.add_program
        )
        self.add_program_button.grid(row=0, column=2, padx=5, pady=5)

        self.stop_button = tk.Button(
            master,
            text="Stop",
            command=self.stop_scanning,
            state=tk.DISABLED
        )
        self.stop_button.grid(row=0, column=3, padx=5, pady=5)

        # Output Area
        self.output_text = tk.Text(
            master,
            height=20,
            width=90,
            state=tk.DISABLED
        )
        self.output_text.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=10,
            pady=10
        )

        # Bottom Buttons
        self.save_output_button = tk.Button(
            master,
            text="Save Output",
            command=self.save_output
        )
        self.save_output_button.grid(row=2, column=0, padx=5, pady=5)

        self.clear_chat_button = tk.Button(
            master,
            text="Clear Output",
            command=self.clear_output
        )
        self.clear_chat_button.grid(row=2, column=1, padx=5, pady=5)

        self.blacklist_button = tk.Button(
            master,
            text="Blacklist",
            command=self.show_blacklist
        )
        self.blacklist_button.grid(row=2, column=2, padx=5, pady=5)

        self.whitelist_button = tk.Button(
            master,
            text="Whitelist",
            command=self.show_whitelist
        )
        self.whitelist_button.grid(row=2, column=3, padx=5, pady=5)

        self.scanning_thread = None
        self.is_scanning = False
        self.file_to_scan = ""

    # --------------------
    # Utility Functions
    # --------------------

    def update_output(self, message):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)

    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

    def save_output(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt"
        )

        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                text = self.output_text.get(1.0, tk.END)
                f.write(text)

            messagebox.showinfo(
                "Saved",
                f"Output saved to:\n{filename}"
            )

    # --------------------
    # Buttons
    # --------------------

    def show_info(self):
        messagebox.showinfo(
            "Information",
            "Reports are stored in:\nscan_reports/"
        )

    def show_blacklist(self):
        messagebox.showinfo(
            "Blacklist",
            "Blocked programs are stored in blacklist.json"
        )

    def show_whitelist(self):
        messagebox.showinfo(
            "Whitelist",
            "Trusted programs are stored in whitelist.json"
        )

    def add_program(self):
        response = messagebox.askyesnocancel(
            "Program List",
            "Add program to Blacklist?\n\nYes = Blacklist\nNo = Whitelist"
        )

        if response is True:
            messagebox.showinfo(
                "Blacklist",
                "Program would be added to blacklist."
            )

        elif response is False:
            messagebox.showinfo(
                "Whitelist",
                "Program would be added to whitelist."
            )

    # --------------------
    # Scan Logic
    # --------------------

    def start_scanning(self):

        if self.is_scanning:
            return

        self.file_to_scan = filedialog.askopenfilename(
            title="Select File"
        )

        if not self.file_to_scan:
            return

        self.is_scanning = True

        self.listen_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.update_output("")
        self.update_output(
            f"Scanning file: {self.file_to_scan}"
        )
        self.update_output("-" * 60)

        self.scanning_thread = threading.Thread(
            target=self._scan_file
        )

        self.scanning_thread.start()

    def stop_scanning(self):
        self.is_scanning = False

        self.listen_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        self.update_output("Scan stopped.")

    def _scan_file(self):

        try:

            activity = self.process_monitor.get_sample_activity()

            self.update_output(
                f"Activity: {activity}"
            )

            result = self.detector.scan_file(
                self.file_to_scan
            )

            self.update_output("")
            self.update_output(
                f"Threat Score: {result['score']}"
            )

            self.update_output(
                f"Risk Level: {result['risk']}"
            )

            self.update_output("")
            self.update_output("Findings:")

            for finding in result["findings"]:
                self.update_output(
                    f"- {finding}"
                )

            self.update_output("")
            self.update_output(
                "Startup Analysis:"
            )

            startup_items = (
                self.startup_checker
                .check_startup_items()
            )

            for item in startup_items:
                self.update_output(
                    f"{item['name']} : {item['status']}"
                )

            report_path = (
                self.report_generator
                .generate_report(result)
            )

            self.update_output("")
            self.update_output(
                f"Report saved: {report_path}"
            )

        except Exception as e:

            self.update_output(
                f"Error: {str(e)}"
            )

        self.is_scanning = False

        self.master.after(
            0,
            lambda: self.listen_button.config(
                state=tk.NORMAL
            )
        )

        self.master.after(
            0,
            lambda: self.stop_button.config(
                state=tk.DISABLED
            )
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerDetectorGUI(root)
    root.mainloop()