import os
from datetime import datetime

class ReportGenerator:

    def generate_report(self, result):
        os.makedirs("scan_reports", exist_ok=True)

        filename = datetime.now().strftime(
            "scan_reports/report_%Y%m%d_%H%M%S.txt"
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== Scan Report ===\n\n")
            f.write(f"Risk Level: {result['risk']}\n")
            f.write(f"Threat Score: {result['score']}\n\n")

            f.write("Findings:\n")

            for item in result["findings"]:
                f.write(f"- {item}\n")

        return filename