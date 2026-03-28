# 🌧️ Rain Alert System (Python + APIs)
A Python-based automation project that checks upcoming weather conditions and sends an SMS alert when rain is expected helping users stay prepared before stepping outside.

## 📌 Overview
This project demonstrates how to work with **real-world APIs** by integrating:

* OpenWeatherMap API → for weather forecast data
* Twilio API → for sending SMS notifications

The system fetches weather data for the next few hours and automatically sends an alert if rain is predicted.

---

## 🚀 Features

* 🌍 Fetches real-time weather forecast data
* ⏱️ Monitors upcoming hours (`cnt = 4`, i.e., next 12 hours)
* 🌧️ Detects rain using weather condition codes
* 📲 Sends SMS alerts using Twilio
* ⚙️ Fully automated workflow

---

## 🛠️ Tech Stack

* Python
* `requests`
* `python-dotenv`
* Twilio API
* OpenWeatherMap API

---

## 📂 Project Structure

```
├── main.py
├── .env (not included here)
```
---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ahsanali18/Rain Alert System.git
cd Rain Alert System
```

---

### 2. Install Dependencies

```bash
pip install requests twilio python-dotenv
```
---

### 3. Create a `.env` File

Create a `.env` file in your project root and add:

```
OWM_API_KEY=your_openweathermap_api_key
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

---

### 4. Configure the Script

Open `main.py` and update:

* 📍 **Latitude & Longitude** (of your desired city)
* 📲 **Phone Numbers**

  * `from_` → Your Twilio number
  * `to` → Your verified number

---

### 5. Run the Program

```bash
python main.py
```

---

## 📍 Example Location

Currently configured for:

* Hyderabad, Sindh, Pakistan 🇵🇰

You can change this by updating latitude & longitude values.

---

## 📸 Example Output

### If rain is expected:

```
SMS Sent: queued
```

📩 Message:

> 🌧️ Rain expected today. Don't forget to bring an umbrella!

---

### If no rain:

```
No rain expected.
```

---

## 🎯 Learning Outcomes

Through this project, you will learn:

* How APIs work in real-world applications
* Handling and parsing JSON data
* Automating tasks using Python
* Integrating third-party services

---

## 🔮 Future Improvements

* Support multiple locations
* Schedule automatic execution (cron jobs)
* Add email notifications
* Build a web interface

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and improve it.

---

## 📄 License

This project is open-source and available under the MIT License.

---
