# WHOIS Domain Lookup

**WHOIS-Domain-Lookup** is a simple Python tool that allows users to query WHOIS data for domain names — returning registration and ownership information such as registrar, creation date, expiration date, name servers, and more. WHOIS is a protocol used to look up publicly available domain registration records maintained by registries worldwide.

## 📌 Features

- 🔍 Performs WHOIS lookups for one or more domains
- 📅 Returns key information such as:
  - Registrar name
  - Creation and expiration dates
  - Name servers
  - Registrant info (where available)
- 🐍 Built with Python using the `whois` library
- 🧠 Easy to extend for bulk domain checks

## 🧰 Requirements

Before using this project, ensure you have:

* Python 3.6+
* `pip` package manager

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MatheusSabaudo/WHOIS-Domain-Lookup.git
   cd WHOIS-Domain-Lookup
   ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 💡 Usage

* Basic

 - Run the script and pass one or more domains to query:
    ```bash
    python main.py
    ```

You’ll be prompted to enter domain(s) for lookup (e.g., example.com, github.com, etc.).

**Example Output:**
```bash
Domain: example.com
Registrar: Example Registrar, LLC
Created: 1995-08-13
Expires: 2026-08-12
Name Servers:
- ns1.example.com
- ns2.example.com
```
(Actual output depends on the whois library API and domain queried.)

## 📁 Code Structure

```text
.
├── main.py            # Main Python script
├── README.md          # Project documentation (this file)
├── requirements.txt   # Python dependencies (if present)
└── .gitignore
```

## 🛠️ How It Works

* The project uses the third-party Python WHOIS library to perform lookups:

```python
import whois

domain_info = whois.whois('example.com')
print(domain_info)
```

The script collects details such as registrar, creation and expiration dates, and name servers, and formats them for easy reading.

## 🧪 Contributing

* Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/my-awesome-feature
```

3. Commit your changes
4. Push to your fork and open a pull request

Please ensure your code follows standard Python style and includes comments where helpful.

## 📜 License

Released under the **MIT License**.

## 👤 Author

Created by **Matteo Sabaudo**

Feel free to fork, modify, and improve this project.
