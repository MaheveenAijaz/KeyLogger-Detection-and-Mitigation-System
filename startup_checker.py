class StartupChecker:

    def check_startup_items(self):
        return [
            {"name": "Windows Defender", "status": "Trusted"},
            {"name": "ExampleApp", "status": "Trusted"},
            {"name": "UnknownTool", "status": "Review Required"}
        ]