from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "id": "mobile-app-pentest",
        "name": "Mobile App Security Assessment",
        "full_name": "Android / API / Cloud Backend Penetration Test",
        "summary": "Full-scope, authorized security assessment of an Android application "
                    "and its API and cloud backend, conducted under signed NDA and agreed rules of "
                    "engagement. Covered an 8-phase methodology across static APK analysis, live API "
                    "and authorization testing, source-level code review, local storage inspection, "
                    "and dependency review. Identified a critical authorization vulnerability exposing "
                    "user data across accounts, reported and remediated same-day, with 17 total "
                    "findings documented and 8 positive controls independently verified.",
        "stack": ["Android", "Burp Suite", "OWASP Top 10", "API Security", "MITRE ATT&CK"],
        "status": "Client engagement NDA",
   },
   {
        "id": "adaptive-firewall",
        "name": "AdaptiveShield",
        "full_name": "AdaptiveShield — Adaptive Firewall using Deep Q-Network Reinforcement Learning",
        "summary": "AdaptiveShield is a production-deployable autonomous adaptive firewall powered by "
                    "a Deep Q-Network (DQN) reinforcement learning agent. Unlike conventional static "
                    "rule-based firewalls that can only block known threats, AdaptiveShield continuously "
                    "learns optimal traffic filtering policies through real-time interaction with network "
                    "traffic — no manual rule updates, no offline retraining required. The system is "
                    "trained and evaluated on the CICIDS 2017 benchmark dataset — the most widely "
                    "adopted standardised dataset in intrusion detection research — and deployed via a "
                    "real-time Python/Flask operational dashboard with live packet classification, "
                    "attack distribution visualisation, and DQN engine telemetry. Submitted to IEEE "
                    "NIGERCON 2026 — AdaptiveShield: An End-to-End Adaptive Firewall Using Deep "
                    "Q-Network Reinforcement Learning.",
        "stack": ["Python", "Deep Q-Network (DQN)", "Reinforcement Learning", "Flask", "CICIDS 2017"],
        "status": "Submitted to & Accepted by IEEE NIGERCON 2026",
        "link": "https://github.com/Thinkersjnr1/ADAPTIVE-FIREWALL-USING-REINFORCEMENT-LEARNING",
    },
    {
        "id": "ensop",
        "name": "ENSOP",
        "full_name": "Enterprise Network Security Operations Platform",
        "summary": "Self-hosted Zero Trust network lab: pfSense with VLAN-segmented zones, "
                    "Suricata IPS, Wazuh SIEM, and Zeek+ELK for full traffic analysis. Includes "
                    "a red team simulation mapped to MITRE ATT&CK with a detection-validation "
                    "report grading the defenses against the attacks.",
        "stack": ["pfSense", "Suricata", "Wazuh", "Zeek", "ELK Stack", "Kali Linux", "MITRE ATT&CK"],
        "status": "Active build",
        "link": "https://github.com/Thinkersjnr1/Enterprise-Network-Security-Operations-Platform-ENSOP-",
    },
    {
        "id": "vapt",
        "name": "Vulnerability Assessment & Penetration Testing",
        "full_name": "Web Application / Network / VAPT Security Assessment",
        "summary": "Conducted full-scope Vulnerability Assessment and Penetration Testing (VAPT) "
                    "engagements across partner projects including CrexBet and LTSU, identifying "
                    "critical vulnerabilities across web application and network attack surfaces. "
                    "Executed structured penetration tests using Burp Suite, OWASP ZAP, and Nmap, "
                    "documenting findings against the OWASP Top 10 with CVSS-based risk ratings. "
                    "Delivered comprehensive penetration-testing reports and security assessments "
                    "directly to partner stakeholders, while supporting continuous security improvement "
                    "through vulnerability triage, remediation validation, retesting, and follow-up "
                    "security documentation.",
        "stack": ["Burp Suite", "OWASP ZAP", "Nmap", "OWASP Top 10", "CVSS", "VAPT"],
        "status": "Professional security engagements",
        "link": "https://github.com/Thinkersjnr1/web-application-penetration-testing",
    },
    {
        "id": "nids",
        "name": "Network Intrusion Detection",
        "full_name": "Simulated Incident Response Exercise",
        "summary": "Simulated ransomware and phishing scenarios in a controlled environment to "
                    "practice incident response following NIST SP 800-61r2, using a Kali Linux "
                    "attacker against a defended, monitored target.",
        "stack": ["Python", "Kali Linux", "NIST SP 800-61r2", "Incident Response"],
        "status": "Complete",
        "link": "https://github.com/Thinkersjnr1/Network-Intrusion-detection-system",
    },
    {
        "id": "email-auth",
        "name": "Email Authentication Analyzer",
        "full_name": "SPF/DKIM/DMARC Diagnostic Tool",
        "summary": "A web-based diagnostic tool that parses raw email headers to verify SPF, DKIM, "
                    "and DMARC alignment in real time, secured by a custom Application-Layer Firewall.",
        "stack": ["HTML", "Email Security", "WAF"],
        "status": "Complete",
        "link": "https://github.com/Thinkersjnr1/email-auth-demo",
    },
]

EXPERIENCE = [
    { 
        "role": "Cybersecurity Intern — Job Shadowing 2.0",
        "org": "Interswitch Group",
        "location": "Remote — Lagos State, Nigeria",
        "period": "Apr 2025 – May 2026",
        "points": [
            "Selected for Interswitch's Job Shadowing 2.0 program, completing structured sessions on "
            "personal branding, career strategy, and problem-solving frameworks (root cause analysis, "
            "fishbone diagrams) facilitated with Human Capital Partners.",
            "Developed and presented \"CyberSecure Nexora,\" a fintech cybersecurity strategy spanning "
            "AI-driven fraud detection, Zero Trust architecture, and compliance across DORA, NDPR, "
            "PCI-DSS, ISO 27001, and GDPR.",
            "Applied SWOT analysis and the McKinsey 7S framework to assess organizational cybersecurity "
            "readiness, building a phased 2025–2028 implementation roadmap with defined KPIs.",
            "Recommended structural improvements including direct CISO-to-CEO reporting, periodic Red "
            "Team/Blue Team exercises, and a cross-functional Cybersecurity Advisory Board.",
        ],
    },
    {
        "role": "Cybersecurity Intern",
        "org": "Employment Express Verband LLP",
        "location": "Remote — Lagos State, Nigeria",
        "period": "Aug 2025 – Nov 2025",
        "points": [
            "Conducted full-scope VAPT on partner projects including CrexBet and LTSU, identifying "
            "critical vulnerabilities across web application and network attack surfaces.",
            "Executed structured penetration tests using Burp Suite, OWASP ZAP, and Nmap, documenting "
            "findings mapped to OWASP Top 10 with CVSS-scored risk ratings.",
            "Delivered pentest reports and security assessments directly to partner stakeholders.",
            "Supported continuous security improvement through vulnerability triage, retesting, and "
            "follow-up documentation.",
        ],
    },
    {
        "role": "Network Security Intern",
        "org": "Redynox",
        "location": "Remote — India",
        "period": "Jun 2025 – Aug 2025",
        "points": [
            "Conducted web application vulnerability assessments on WebGoat using OWASP ZAP on Kali "
            "Linux, identifying SQL Injection, XSS, and CSRF vulnerabilities.",
            "Performed deep-packet network traffic analysis with Wireshark, detecting unauthorized "
            "port scans and anomalous activity across live network environments.",
            "Designed IDS deployment architectures to strengthen organizational perimeter defenses.",
        ],
    },
    {
        "role": "Cybersecurity Intern",
        "org": "Hacktify",
        "location": "Remote — Lagos, Nigeria",
        "period": "Feb 2025 – Mar 2025",
        "points": [
            "Executed penetration testing using Burp Suite, Nmap, and OWASP ZAP across assessed systems.",
            "Performed end-to-end VAPT of Hacktify's infrastructure, uncovering critical misconfigurations "
            "aligned to OWASP Top 10.",
            "Awarded Hacktify Penetration Testing Certificate for outstanding performance.",
        ],
    },
]

CERTIFICATIONS = [
    {"name": "Certified Computer Forensics Analyst (CCFA)", "issuer": "eSecurity Institute", "date": "Sep 2026", "link": "https://app.esecurityinstitute.com/certificates/iopasljamq"},
    {"name": "Certified Ransomware Protection Officer (CRPO)", "issuer": "EU Cyber Academy", "date": "Dec 2025"},
    {"name": "Securing LLM and NLP APIs", "issuer": "APIsec University", "date": "Jul 2025"},
    {"name": "Building Security into AI", "issuer": "APIsec University", "date": "Jul 2025"},
    {"name": "API Security for PCI Compliance", "issuer": "APIsec University", "date": "Jul 2025"},
    {"name": "Cisco CyberOps Associate", "issuer": "Cisco Networking Academy", "date": "May 2025"},
    {"name": "Cisco Certified Ethical Hacker", "issuer": "Cisco", "date": "May 2025"},
    {"name": "Security Operations & Defense Analyst", "issuer": "Splunk", "date": "Sep 2023"},
    {"name": "Intro to Critical Infrastructure Protection", "issuer": "OPSWAT Academy", "date": "Aug 2023"},
    {"name": "Certified in Cybersecurity (CC)", "issuer": "ISC²", "date": "Dec 2022"},
    {"name": "GDSC Cybersecurity Bootcamp", "issuer": "Google Developer Student Clubs", "date": "Feb 2023"},
]

EDUCATION = [
    {
        "program": "B.Sc. Cybersecurity",
        "org": "Lead City University",
        "location": "Ibadan, Nigeria",
        "period": "Expected December 2026",
        "points": [],
    },
    {
        "program": "Cybersecurity, Ethical Hacking & CyberOps Associate",
        "org": "Cisco Networking Academy",
        "location": "",
        "period": "2025",
        "points": [
            "Coursework: Network Security, Ethical Hacking, CyberOps (incident response, threat "
            "detection), Security Best Practices.",
            "Badges: Cisco CyberOps Associate Badge, Cisco Ethical Hacker Badge.",
        ],
    },
    {
        "program": "Cybersecurity, AI & Compliance",
        "org": "APIsec University",
        "location": "",
        "period": "Jun 2024 – Sep 2025",
        "points": [
            "API security testing, penetration testing, AI/LLM security, and PCI compliance using "
            "Postman, Burp Suite, ZAP Proxy.",
        ],
    },
]

SKILLS = {
    "Networking & Firewalls": ["pfSense", "802.1Q VLANs", "Cisco fundamentals", "Zero Trust architecture"],
    "Monitoring & Detection": ["Suricata", "Zeek", "Wazuh", "ELK Stack", "MITRE ATT&CK"],
    "Offensive Security": ["Burp Suite", "OWASP ZAP", "Nmap", "Metasploit", "SQLmap", "Kali Linux"],
    "Operating Systems & Platforms": ["Kali Linux", "Ubuntu", "Windows Server", "AWS (fundamentals)"],
    "Languages": ["Python", "Bash"],
}


@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS[:3])


@app.route("/about")
def about():
    return render_template("about.html", skills=SKILLS)


@app.route("/experience")
def experience():
    return render_template("experience.html", experience=EXPERIENCE)


@app.route("/credentials")
def credentials():
    return render_template("credentials.html", certifications=CERTIFICATIONS, education=EDUCATION)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
