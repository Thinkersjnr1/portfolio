from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
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
        "id": "adaptive-firewall",
        "name": "Adaptive Firewall",
        "full_name": "Adaptive Firewall using Reinforcement Learning",
        "summary": "A firewall that learns optimal traffic-filtering policies in real time "
                    "through trial-and-error interaction, rather than relying on static rules.",
        "stack": ["Python", "Reinforcement Learning", "Network Security"],
        "status": "Complete",
        "link": "https://github.com/Thinkersjnr1/ADAPTIVE-FIREWALL-USING-REINFORCEMENT-LEARNING",
    },
    {
        "id": "siem-dashboard",
        "name": "SIEM Dashboard",
        "full_name": "Enterprise SIEM Dashboard with ELK Stack",
        "summary": "A Security Information and Event Management system built on the open-source "
                    "Elastic Stack for log ingestion, storage, and visualization.",
        "stack": ["Elasticsearch", "Logstash", "Kibana"],
        "status": "Complete",
        "link": "https://github.com/Thinkersjnr1/Enterprise-SIEM-Dashboard-with-ELK-Stack",
    },
    {
        "id": "web-vuln-scanner",
        "name": "Web Vuln Scanner",
        "full_name": "Web Vulnerability Scanner",
        "summary": "Python web app automating vulnerability scanning via OWASP ZAP, with an "
                    "interactive dashboard and PDF report generation. Deployed live.",
        "stack": ["Python", "OWASP ZAP", "Kali Linux"],
        "status": "Complete — live demo",
        "link": "https://github.com/Thinkersjnr1/web_vuln_scanner",
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
        "role": "Cybersecurity Intern",
        "org": "Employment Express Verband LLP",
        "location": "Remote — Lagos State, Nigeria",
        "period": "Aug 2025 – Present",
        "points": [
            "Conducted full-scope VAPT on partner projects including CrexBet and LTSU, identifying "
            "critical vulnerabilities across web application and network attack surfaces.",
            "Executed structured penetration tests using Burp Suite, OWASP ZAP, and Nmap, documenting "
            "findings mapped to OWASP Top 10 with CVSS-scored risk ratings.",
            "Delivered pentest reports and security assessments directly to partner stakeholders.",
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
