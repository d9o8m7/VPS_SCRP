# **VPS Price Tracker Bot**

A Python-based bot that scrapes VPS hosting websites to track the latest prices, detect discounts, and identify the best deals. This project is community-driven, and contributions are welcome!

---

## **Features**
- Scrapes VPS hosting prices from multiple providers.
- Detects price changes and alerts when discounts are available.
- Saves data to a local SQLite database for historical tracking.
- Easy to schedule periodic updates using `APScheduler`.
- Modular and customizable scraping logic.

---

## **Prerequisites**
- Python 3.8+
- Basic knowledge of web scraping and Python.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/vps-price-tracker.git
cd vps-price-tracker

### **2. Install Required Libraries**
```bash
pip install -r requirements.txt
```

### **3. Initalize the Database**
Run the script to set up the database:
```bash
python tracker.py
```

---

## **Usage**

### **1. Start the Bot**
Run the main script to start scraping and detecting price updates:
```bash
python tracker.py
```

### **2. Schedule the Scraper**
Modify the [schedule.every(6).hours.do(scrape_vps_prices)] line in the script to adjust the scraping frequency.

### **3. Add/Modify Providers**
Edit the [providers] dictionary in [tracker.py] to include new VPS hosting providers and their plan pages:
```python
providers = {
	"ProviderA": "https://example.com/plans",
	"ProviderB": "https://otherexample.com/vps"
}
```

### **4. View Logs**
The bot prints updates about price changes and newly added plans directly in the console.

---

### **Contributing**

We welcome contributions to improve and expand this project! Here's how you can get involved:
	1. Fork the repository.
	2. Create a new branch for your feature or fix.
	3. Submit a pull request with a clear description of your changes.

### **Ideas for Contributions**

 - Add support for new providers.
 - Integrate Telegram/Email notifications.
 - Optimize the scraping logic (e.g., use Selenium for dynamic content).
 - Add a web-based dashboard for price tracking.
 - Support cloud database options (MySQL/PostgreSQL).

---

### **License**

This project is licensed under the MIT License. See the [LICENSE]() file for details.

---

### **Acknowledgments**

Special thanks to the open-source community fot their inspiration adn tools like [BeautifullSoup], [request], and [sqlite3] that made this project possible.

---

### **Suport**
Have questions, or need help? Open an issue in the repository or contact [your-email/username].
