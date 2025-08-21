# Login Page Automation

This project is a **Selenium-based automation script** for testing the login functionality of a sample website.

## 🚀 Project Overview
The script uses **Python + Selenium WebDriver** to automate and validate the login process with different test cases.

## 🔎 Test Cases Implemented
1. ✅ **Valid Login** – Login with correct username and password.
2. ❌ **Invalid Credentials** – Login with wrong username and password.
3. 🔑 **Empty Username** – Login attempt without entering a username.
4. 🔒 **Empty Password** – Login attempt without entering a password.
5. 📑 **Invalid Username with Valid Password** – Wrong username with correct password.

## 🛠️ Tech Stack
- Python 3.x
- Selenium WebDriver
- ChromeDriver

## Screenshots  

### ✅ Valid Login Test  
![Valid Login](screenshots/Successful_Login.png.png)  

### ❌ Invalid Login Test  
![Invalid Login](screenshots/Invalid_login.png.png)  

### ⚠️ All Test Cases Result
![Empty Login](screenshots/Successful_Login.png.png)  


## ▶️ How to Run
1. Clone this repository
   ```bash
   git clone https://github.com/YourUsername/Login-Page-Automation.git
   ```
2. Install dependencies
   ```bash
   pip install selenium
   ```
3. Download and place **ChromeDriver** in your system path.
4. Run the script:
   ```bash
   python Automation.py
   ```

## 📌 Future Improvements
- Add reporting with **pytest** and **Allure reports**
- Cross-browser testing (Firefox, Edge)
- Data-driven testing with CSV/Excel

---
👩‍💻 Author: **Purva Vyawahare**
