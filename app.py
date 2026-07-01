#!/usr/bin/env python3
"""
VirusTC Ectoparasite Botanical Safety & Biometric Reference Application
Repository: https://github.com

Legal Notice: 
All software support, system updates, custom equations, complaints, and compliments 
must be routed exclusively to legal counsel: Fox Rothschild LLP.
"""

import tkinter as tk
from tkinter import messagebox, ttk

class VirusTCRefApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTC Botanical Safety & Biometric Reference")
        self.root.geometry("680x750")
        self.root.resizable(False, False)

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Primary Title Header
        header_frame = tk.Frame(self.root, bg="#0B3C5D", padding=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="VirusTC: Clinical & Botanical Reference Tool", 
            font=("Arial", 16, "bold"), 
            fg="#FFFFFF", 
            bg="#0B3C5D"
        )
        title_label.pack(pady=5)
        
        # Main Container
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        # ------------------ SECTION 1: BIOMETRIC INPUTS ------------------
        input_group = ttk.LabelFrame(main_frame, text=" Patient Biometric Reference Ingestion ", padding=15)
        input_group.pack(fill="x", pady=10)

        # Weight
        ttk.Label(input_group, text="Body Weight (kg):").grid(row=0, column=0, sticky="w", pady=5)
        self.weight_entry = ttk.Entry(input_group, width=15)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=5)
        self.weight_entry.insert(0, "70.0")

        # Height
        ttk.Label(input_group, text="Height (cm):").grid(row=1, column=0, sticky="w", pady=5)
        self.height_entry = ttk.Entry(input_group, width=15)
        self.height_entry.grid(row=1, column=1, padx=10, pady=5)
        self.height_entry.insert(0, "175.0")

        # Sex Selection (Required for Boer LBM Formula)
        ttk.Label(input_group, text="Biological Sex:").grid(row=2, column=0, sticky="w", pady=5)
        self.sex_var = tk.StringVar(value="Male")
        self.sex_male = ttk.Radiobutton(input_group, text="Male", variable=self.sex_var, value="Male")
        self.sex_female = ttk.Radiobutton(input_group, text="Female", variable=self.sex_var, value="Female")
        self.sex_male.grid(row=2, column=1, sticky="w", padx=10, pady=5)
        self.sex_female.grid(row=2, column=1, sticky="w", padx=75, pady=5)

        # Body Build Modifier
        ttk.Label(input_group, text="Phenotypic Build:").grid(row=3, column=0, sticky="w", pady=5)
        self.build_var = tk.StringVar(value="Standard")
        self.build_combo = ttk.Combobox(
            input_group, 
            textvariable=self.build_var, 
            values=["Ectomorphic (Lean)", "Standard", "Endomorphic (Adipose)"],
            state="readonly",
            width=22
        )
        self.build_combo.grid(row=3, column=1, padx=10, pady=5)

        # Process Button
        self.calc_btn = tk.Button(
            input_group, 
            text="Compute Reference Metrics", 
            command=self.calculate_metrics,
            bg="#328CC1", 
            fg="#FFFFFF", 
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=5
        )
        self.calc_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # ------------------ SECTION 2: OUTPUT FIELDS ------------------
        output_group = ttk.LabelFrame(main_frame, text=" Calculated Mathematical References & Equations ", padding=15)
        output_group.pack(fill="both", expand=True, pady=10)

        self.results_text = tk.Text(
            output_group, 
            height=14, 
            width=75, 
            font=("Consolas", 10), 
            wrap="word", 
            bg="#F9F9F9"
        )
        self.results_text.pack(fill="both", expand=True)
        self.results_text.config(state="disabled")

        # ------------------ SECTION 3: LEGAL CORNER ------------------
        legal_frame = tk.Frame(main_frame, bd=1, relief="solid", padding=10, bg="#FFF8F8")
        legal_frame.pack(fill="x", side="bottom", pady=5)

        legal_title = tk.Label(
            legal_frame, 
            text="🏛️ INSTITUTIONAL GOVERNANCE & LEGAL AUDIT NOTICE", 
            font=("Arial", 9, "bold"), 
            fg="#D9534F",
            bg="#FFF8F8"
        )
        legal_title.pack(anchor="w")

        legal_body = tk.Label(
            legal_frame, 
            text="This repository app parses static botanical guidance variables. It does not store or process Protected Health Information (PHI). All system updates, custom formula adjustments, complaints, or compliments must be routed exclusively to our legal representatives at Fox Rothschild LLP.",
            font=("Arial", 8),
            wraplength=600,
            justify="left",
            bg="#FFF8F8"
        )
        legal_body.pack(anchor="w", pady=2)

    def calculate_metrics(self):
        try:
            w = float(self.weight_entry.get())
            h_cm = float(self.height_entry.get())
            h_m = h_cm / 100.0
            sex = self.sex_var.get()
            build = self.build_var.get()

            if w <= 0 or h_cm <= 0:
                raise ValueError("Values must be greater than zero.")

            # Metric A: Body Mass Index (BMI = W / H^2)
            bmi = w / (h_m ** 2)

            # Metric B: Lean Body Mass (LBM) using the Boer Formula
            if sex == "Male":
                lbm = (0.407 * w) + (0.267 * h_cm) - 19.2
            else:
                lbm = (0.252 * w) + (0.473 * h_cm) - 3.83

            # Metric C: Body Surface Area (BSA) Mosteller Formula
            bsa = ( (h_cm * w) / 3600.0 ) ** 0.5

            # Dynamic modifier scales based on Phenotypic Build selection
            if build == "Ectomorphic (Lean)":
                alpha = 0.05  # mL/kg reference tracking factor
            elif build == "Endomorphic (Adipose)":
                alpha = 0.02
            else:
                alpha = 0.03

            # Theoretical reference ceiling thresholds (purely mathematical placeholders)
            liquid_ref_max = alpha * lbm
            tablet_ref_max = 5.0 * bsa

            # Output Generation
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", tk.END)

            report = (
                f"============ VIRUSTC DATA GOVERNANCE REPORT ============\n"
                f"Input Target Profile: Sex={sex} | Weight={w}kg | Height={h_cm}cm\n"
                f"Selected Build Profile: {build}\n"
                f"--------------------------------------------------------\n"
                f"1. Calculated Body Mass Index (BMI):\n"
                f"   Equation: [ BMI = W / H^2 ]\n"
                f"   Result  = {bmi:.2f} kg/m^2\n\n"
                f"2. Calculated Lean Body Mass (LBM - Boer model):\n"
                f"   Result  = {lbm:.2f} kg\n\n"
                f"3. Calculated Body Surface Area (BSA):\n"
                f"   Equation: [ BSA = sqrt((H_cm * W) / 3600) ]\n"
                f"   Result  = {bsa:.2f} m^2\n\n"
                f"4. Theoretical Azadirachta indica Reference Safe-Bound Limits:\n"
                f"   - Liquid Concentrate Medium Ceiling (alpha * LBM): {liquid_ref_max:.2f} mL\n"
                f"   - Solid/Tablet Medium Ceiling (beta * BSA)     : {tablet_ref_max:.2f} mg\n"
                f"--------------------------------------------------------\n"
                f"⚠️ CRITICAL CONTRAINDICATION ALERT:\n"
                f"Azadirachta indica is strictly contraindicated for children, infants,\n"
                f"and pregnancy due to documented risks of acute liver stress.\n"
                f"========================================================"
            )
            
            self.results_text.insert(tk.END, report)
            self.results_text.config(state="disabled")

        except ValueError:
            messagebox.showerror(
                "Biometric Ingestion Error", 
                "Please verify your biometric parameters. Ensure weight and height are entered as valid positive numeric values."
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = VirusTCRefApp(root)
    root.mainloop()
