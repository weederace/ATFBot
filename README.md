# ATF Auto-Clicker Bot 🤖

> **English documentation**
> برای مشاهده توضیحات فارسی به بخش [نسخه فارسی](#ربات-کلیکر-خودکار-atf-) مراجعه کنید.

A simple and dynamic Python automation bot designed to automate clicking on the ATF coin and claiming rewards.

The bot uses **multi-threading**, **dynamic coordinate detection**, and **slight randomized click offsets** to provide more natural click behavior.

---

## 🌟 Features

* **⛏️ Automated Mining**
  Automatically clicks the ATF coin every **9 seconds**.

* **🎁 Automated Claiming**
  Automatically clicks the **Claim** button every **10 minutes**.

* **📍 Dynamic Coordinates**
  Uses a **5-second countdown** to capture the position of the ATF coin and Claim button, making the bot usable on different screen sizes and resolutions.

* **🖱️ Randomized Click Offset**
  Adds a small random pixel offset to click positions instead of clicking the exact same pixel every time.

* **⚡ Multi-threading**
  Mining and claiming tasks run independently in separate threads.

* **🛑 Easy Stop**
  The bot can be stopped at any time using `Ctrl+C`.

---

## 📋 Requirements

* Python **3.x**
* `pyautogui`

### Supported Platforms

The bot should work on operating systems supported by Python and PyAutoGUI, including:

* Windows
* Linux
* macOS

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Or simply download the repository as a ZIP file and extract it.

### 2. Install Dependencies

Open a terminal or Command Prompt inside the project directory and run:

```bash
pip install pyautogui
```

If your system uses `pip3`:

```bash
pip3 install pyautogui
```

---

## 🚀 How to Use

### 1. Start the Bot

Run:

```bash
python bot.py
```

### 2. Select the ATF Coin

The terminal will ask you to move your mouse cursor over the **ATF coin**.

You will have **5 seconds** to position your mouse.

The bot will automatically save the cursor coordinates.

### 3. Select the Claim Button

Next, the bot will ask you to move your mouse over the **CLAIM** button.

Again, you will have **5 seconds** to position your cursor.

### 4. Bot Starts Automatically

After both coordinates are captured, the bot will start running automatically.

The default behavior is:

```text
ATF Coin     → Click every 9 seconds
Claim Button → Click every 10 minutes
```

### 5. Stop the Bot

To stop the bot, press:

```text
Ctrl + C
```

in the terminal.

---

## ⚙️ Default Timings

| Action                  |   Interval |
| ----------------------- | ---------: |
| 🪙 ATF Coin Click       |  9 seconds |
| 🎁 Claim Button Click   | 10 minutes |
| 📍 Coordinate Detection |  5 seconds |

---

## 📁 Project Structure

```text
ATF-Auto-Clicker-Bot/
│
├── bot.py
├── README.md
└── LICENSE
```

---

## ⚠️ Important Notes

* Make sure the ATF coin and **Claim** button are visible when capturing their coordinates.
* Do not move the application window after setting the coordinates.
* Changing the screen resolution or display scaling may require capturing the coordinates again.
* PyAutoGUI controls the physical mouse cursor, so avoid manually moving the mouse while the bot is running.
* The randomized click offset is intended to make click positions less repetitive, but **it does not guarantee that the bot cannot be detected**.

---

## ⚠️ Disclaimer

This project is provided for **educational and automation purposes only**.

Using automation or bots on third-party platforms may violate their Terms of Service or other rules. You are responsible for checking and complying with the rules of the platform where you use this software.

The author is not responsible for:

* Account restrictions or bans
* Loss of rewards
* Platform-related issues
* Any damage or loss resulting from the use of this software

**Use it at your own risk.**

---

# ربات کلیکر خودکار ATF 🤖

یک ربات اتوماسیون ساده و پویا با زبان **Python** که برای کلیک خودکار روی سکه ATF و دریافت خودکار پاداش‌ها (**Claim**) طراحی شده است.

این ربات از **Multi-threading**، مختصات‌یابی پویا و جابه‌جایی تصادفی جزئی موقعیت کلیک استفاده می‌کند تا کلیک‌ها کاملاً روی یک پیکسل ثابت انجام نشوند.

---

## 🌟 امکانات

* **⛏️ استخراج خودکار**
  کلیک خودکار روی سکه ATF هر **۹ ثانیه**.

* **🎁 دریافت خودکار پاداش**
  کلیک خودکار روی دکمه **Claim** هر **۱۰ دقیقه**.

* **📍 مختصات‌یابی پویا**
  با استفاده از شمارش معکوس **۵ ثانیه‌ای** می‌توانید موقعیت سکه و دکمه Claim را به‌راحتی مشخص کنید.

* **🖱️ جابه‌جایی تصادفی موقعیت کلیک**
  در هر کلیک، چند پیکسل جابه‌جایی تصادفی ایجاد می‌شود تا کلیک‌ها همیشه دقیقاً روی یک نقطه ثابت انجام نشوند.

* **⚡ اجرای هم‌زمان وظایف**
  عملیات Mining و Claim در Threadهای جداگانه اجرا می‌شوند.

* **🛑 توقف آسان**
  برای متوقف کردن ربات کافی است `Ctrl+C` را در ترمینال فشار دهید.

---

## 📋 پیش‌نیازها

* Python نسخه **3.x**
* کتابخانه `pyautogui`

### سیستم‌عامل‌های قابل استفاده

این ربات روی سیستم‌عامل‌هایی که Python و PyAutoGUI را پشتیبانی می‌کنند قابل اجرا است، از جمله:

* Windows
* Linux
* macOS

---

## 🛠️ نصب و راه‌اندازی

### ۱. دریافت پروژه

مخزن را Clone کنید:

```bash
git clone https://github.com/weederace/ATFBot
cd ATFBot
```

یا پروژه را به‌صورت ZIP دانلود کرده و Extract کنید.

### ۲. نصب کتابخانه مورد نیاز

ترمینال یا CMD را در پوشه پروژه باز کرده و دستور زیر را اجرا کنید:

```bash
pip install pyautogui
```

در بعضی سیستم‌ها ممکن است لازم باشد از `pip3` استفاده کنید:

```bash
pip3 install pyautogui
```

---

## 🚀 نحوه استفاده

### ۱. اجرای ربات

دستور زیر را اجرا کنید:

```bash
python bot.py
```

### ۲. انتخاب سکه ATF

ربات از شما می‌خواهد نشانگر ماوس را روی **سکه ATF** قرار دهید.

شما **۵ ثانیه** فرصت دارید تا ماوس را در موقعیت مناسب قرار دهید.

پس از پایان شمارش معکوس، مختصات ماوس به‌صورت خودکار ذخیره می‌شود.

### ۳. انتخاب دکمه Claim

در مرحله بعد، ربات از شما می‌خواهد نشانگر ماوس را روی دکمه **CLAIM** قرار دهید.

دوباره **۵ ثانیه** برای قرار دادن ماوس فرصت خواهید داشت.

### ۴. شروع خودکار

پس از ثبت هر دو مختصات، ربات به‌صورت خودکار شروع به کار می‌کند.

تنظیمات پیش‌فرض:

```text
سکه ATF       → هر ۹ ثانیه
دکمه Claim    → هر ۱۰ دقیقه
```

### ۵. متوقف کردن ربات

برای متوقف کردن ربات، در محیط Terminal یا CMD کلیدهای زیر را فشار دهید:

```text
Ctrl + C
```

---

## ⚙️ زمان‌بندی پیش‌فرض

| عملیات              |     زمان |
| ------------------- | -------: |
| 🪙 کلیک روی سکه ATF |  ۹ ثانیه |
| 🎁 کلیک روی Claim   | ۱۰ دقیقه |
| 📍 ثبت مختصات       |  ۵ ثانیه |

---

## 📁 ساختار پروژه

```text
ATF-Auto-Clicker-Bot/
│
├── bot.py
├── README.md
└── LICENSE
```

---

## ⚠️ نکات مهم

* هنگام ثبت مختصات، مطمئن شوید سکه ATF و دکمه **Claim** قابل مشاهده باشند.
* بعد از ثبت مختصات، پنجره برنامه را جابه‌جا نکنید.
* در صورت تغییر رزولوشن یا Scale نمایشگر، بهتر است مختصات را مجدداً ثبت کنید.
* PyAutoGUI نشانگر واقعی ماوس را کنترل می‌کند؛ بنابراین هنگام اجرای ربات از حرکت دادن دستی ماوس خودداری کنید.
* جابه‌جایی تصادفی مختصات کلیک صرفاً باعث می‌شود کلیک‌ها کاملاً روی یک پیکسل ثابت نباشند و **تضمینی برای جلوگیری از شناسایی ربات نیست**.

---

## ⚠️ سلب مسئولیت

این پروژه صرفاً برای **اهداف آموزشی و اتوماسیون** ارائه شده است.

استفاده از ربات یا ابزارهای اتوماسیون در پلتفرم‌های شخص ثالث ممکن است با قوانین یا شرایط استفاده آن پلتفرم مغایرت داشته باشد.

مسئولیت بررسی قوانین و نحوه استفاده از این نرم‌افزار بر عهده کاربر است.

سازنده مسئول موارد زیر نخواهد بود:

* محدود یا مسدود شدن حساب کاربری
* از دست رفتن پاداش‌ها
* مشکلات ایجادشده توسط پلتفرم
* هرگونه خسارت یا ضرر ناشی از استفاده از این نرم‌افزار

**استفاده از این پروژه کاملاً با مسئولیت خود کاربر است.**

---

## 📜 License

This project is provided for educational purposes.

See the `LICENSE` file for more information.
