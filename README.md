# AppleAccountManager

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge&logo=github)](https://github.com/xx36Mostafa/AppleAccountManager)

A Python-based automation script for managing Apple accounts. This tool provides efficient solutions for handling account-related tasks such as logging in, updating passwords, changing security questions, modifying regions, and more.

---

## Features

- **Automated Login**  
  Securely logs in to Apple accounts using credentials.

- **Region Updates**  
  Easily change the region of your accounts with predefined configurations.

- **Password Management**  
  Generate strong passwords or use custom ones and update accounts accordingly.

- **Security Questions**  
  Modify security questions and answers for enhanced account protection.

- **Multithreading**  
  Handles multiple accounts simultaneously for faster processing.

- **Error Logging**  
  Logs errors and exceptions for debugging and tracking purposes.

- **Custom Configuration**  
  Works seamlessly with a `config.ini` file for customizable behavior.

---

## Requirements

To run this script, ensure you have the following installed:

- **Python 3.x** (Tested on Python 3.7+)
- Required Python libraries:
  - `requests`
  - `faker`
  - `beautifulsoup4`
  - `colorama`
  - `rich`
  - `getmac`
  - `configparser`

Install dependencies using the following command:

```bash
pip install -r requirements.txt
```
## 🛠 Installation

1. **Clone the Repository:**
```bash
   git clone https://github.com/xx36Mostafa/AppleAccountManager.git
   cd AppleAccountManager
```
2. **Install Dependencies**:
   Make sure you have Python installed. Then, install the required libraries using pip:
  ```bash
  pip install -r requirements.txt
  ```
3. **Add Your Configuration**:
  Create a `config.ini` file in the project directory with your desired settings. Use the template provided below for reference.
4. **Prepare Your Input File**:
  Ensure your `.csv` file contains account details in the following format:
  ```bash
  email,password,birthday,security_question_1,security_question_2,security_question_3
  ```
5. **Run Script**:
  Execute the script with:
  ```bash
  python main.py
  ```

## ⚙️ Configuration
The script requires a `config.ini` file to define customizable settings. Below is an example configuration template:
```bash
[settings]
change_password = true
change_questions = true
change_region = true

[password]
password_random = true
password = YourDefaultPassword

[questions]
qusetions_random = true
qusetions = Answer1,Answer2,Answer3
```
## 🚀 Usage
1. Enter the name of your `.csv` file containing the account details when prompted.
2. Follow the on-screen instructions for account processing.
3. Outputs and logs will be saved in `.csv` files for successful, locked, or problematic accounts.

## 📬 Contact
Author: Mustafa Nasser
For queries or updates, feel free to contact me at:
📧 discord: johnwickk__
📱 telegram: @itz36BoDa
