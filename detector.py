import os
import json

class Detector:
    def __init__(self):
        self.blacklist = self.load_list("blacklist.json", "blocked_programs")
        self.whitelist = self.load_list("whitelist.json", "trusted_programs")

    def load_list(self, filename, key):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                return data.get(key, [])
        except:
            return []

    def scan_file(self, filepath):
        findings = []
        score = 0

        filename = os.path.basename(filepath)

        if filename in self.blacklist:
            findings.append(f"{filename} is blacklisted")
            score += 60

        if filename in self.whitelist:
            findings.append(f"{filename} is trusted")
            score -= 20

        if filepath.endswith(".exe"):
            findings.append("Executable file detected")
            score += 20

        size = os.path.getsize(filepath)

        if size > 5000000:
            findings.append("Large file")
            score += 20

        if score < 30:
            risk = "Low"
        elif score < 60:
            risk = "Medium"
        else:
            risk = "High"

        return {
            "score": score,
            "risk": risk,
            "findings": findings
        }