import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime
import schedule
import time

# Database setup
db_name = "vps_prices.db"
def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            provider TEXT,
            plan TEXT,
            price REAL,
            last_updated DATETIME,
            url TEXT
        )
    """)
    conn.commit()
    conn.close()

# Scraping logic
def scrape_vps_prices():
    providers = {
        "ProviderA": "https://example.com/plans",
        "ProviderB": "https://anotherexample.com/vps"
    }
    new_data = []
    for provider, url in providers.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Example: Customize based on website's structure
        plans = soup.select(".plan-card")
        for plan in plans:
            name = plan.select_one(".plan-title").text.strip()
            price = float(plan.select_one(".price").text.replace("$", "").strip())
            new_data.append((provider, name, price, datetime.now(), url))

    # Save data
    save_to_db(new_data)

# Save to database and detect changes
def save_to_db(new_data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for provider, name, price, last_updated, url in new_data:
        cursor.execute("""
            SELECT price FROM prices WHERE provider = ? AND plan = ? AND url = ?
        """, (provider, name, url))
        result = cursor.fetchone()
        
        if result:
            old_price = result[0]
            if price != old_price:
                print(f"Price change detected for {provider} {name}: {old_price} -> {price}")
                cursor.execute("""
                    UPDATE prices SET price = ?, last_updated = ? WHERE provider = ? AND plan = ? AND url = ?
                """, (price, last_updated, provider, name, url))
        else:
            print(f"New plan added: {provider} {name} - ${price}")
            cursor.execute("""
                INSERT INTO prices (provider, plan, price, last_updated, url)
                VALUES (?, ?, ?, ?, ?)
            """, (provider, name, price, last_updated, url))
    conn.commit()
    conn.close()

# Schedule the scraper
def main():
    init_db()
    scrape_vps_prices()
    schedule.every(6).hours.do(scrape_vps_prices)  # Adjust frequency as needed

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

