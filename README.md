# Keylogger Detection and Mitigation System

## Overview

Keylogger Detection and Mitigation System is a Python-based cybersecurity application developed to analyze files, assess potential threats, review startup programs, and generate security reports through an intuitive graphical user interface.

The project demonstrates cybersecurity fundamentals including threat analysis, risk assessment, blacklist/whitelist management, and automated reporting.

---

## Features

- File threat analysis
- Threat scoring engine
- Risk level assessment
- Blacklist management
- Whitelist management
- Startup program review
- Security report generation
- Interactive Tkinter GUI
- Modular system architecture

---

## Technologies Used

### Programming Language
- Python

### GUI Framework
- Tkinter

### Data Storage
- JSON

### Concepts
- Cybersecurity Fundamentals
- Threat Analysis
- Risk Assessment
- File Processing
- Report Generation

---

## Project Structure

```text
Keylogger_Detection_System/
│
├── main.py
├── detector.py
├── startup_checker.py
├── process_monitor.py
├── report_generator.py
├── blacklist.json
├── whitelist.json
├── scan_reports/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Keylogger_Detection_System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python main.py
```

---

## Workflow

1. Launch the application.
2. Select a file for analysis.
3. Review threat score and risk level.
4. Analyze startup program status.
5. Generate security report.
6. Save findings for future reference.

---

## Key Functionalities

### Threat Analysis
Evaluates selected files and identifies potentially suspicious indicators.

### Risk Assessment
Assigns threat scores and categorizes risk levels.

### Startup Review
Reviews startup entries and flags items requiring attention.

### Security Reporting
Automatically generates reports containing scan results and findings.

### Blacklist and Whitelist Management
Maintains trusted and blocked application records.

---

## Future Enhancements

- Real-time process monitoring
- Machine learning-based threat classification
- PDF report generation
- Advanced threat intelligence integration
- Live security dashboard
- Automated mitigation actions

---

## Project Highlights

- Designed a modular cybersecurity monitoring application
- Implemented threat analysis and reporting workflows
- Developed a graphical user interface using Tkinter
- Applied cybersecurity concepts including risk assessment and monitoring
