import random

class ProcessMonitor:

    def get_sample_activity(self):
        samples = [
            "Browser running",
            "Document editor active",
            "File scan initiated",
            "Executable analyzed",
            "System check completed"
        ]

        return random.choice(samples)