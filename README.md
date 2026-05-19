# Income & Spending Survey App

A Flask web application that collects participant income and spending data for healthcare product market research. Data is stored in MongoDB, exported to CSV, and analyzed in a Jupyter notebook.

## Live App

The application is deployed on AWS EC2 and can be accessed at:

**http://13.51.70.161:5000**

---

## Project Structure

```
Final project/
├── app.py              # Flask web application
├── user.py             # User class for data modeling
├── export_csv.py       # Exports MongoDB data to CSV
├── requirements.txt    # Python dependencies
├── templates/
│   ├── index.html      # Survey form
│   └── success.html    # Confirmation page
├── static/
│   └── style.css       # Page styling
├── data/
│   └── users.csv       # Generated after running export_csv.py
└── analysis/
    └── analysis.ipynb  # Jupyter notebook with charts
```

---

## Requirements

- Python 3.8+
- MongoDB (running locally on port 27017)
- pip

---

## Setup Instructions

**1. Clone the repository**

```bash
git clone https://github.com/EzekielDada/Final-project.git
cd Final-project
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Start MongoDB**

Make sure MongoDB is running locally:

```bash
mongod
```

**4. Run the Flask app**

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

---

## Collecting Data

Fill out the survey form. Each submission stores the following in MongoDB (`survey_db.users`):

- Age
- Gender
- Total Monthly Income
- Expense amounts for: Utilities, Entertainment, School Fees, Shopping, Healthcare

---

## Exporting Data to CSV

After collecting responses, run:

```bash
python export_csv.py
```

This loops through all MongoDB records using the `User` class and writes them to `data/users.csv`.

---

## Data Analysis

Open the Jupyter notebook:

```bash
cd analysis
jupyter notebook analysis.ipynb
```

Run all cells to generate:

- **Chart 1** (`charts/income_by_age.png`): Top ages by average income
- **Chart 2** (`charts/gender_spending.png`): Average spending by gender across categories

Both charts are saved to `analysis/charts/` for use in a PowerPoint presentation.

---

## AWS Deployment (EC2)

1. Launch an Ubuntu EC2 instance (t2.micro is fine for testing)
2. Open port 5000 in the security group inbound rules
3. SSH into the instance and run:

```bash
sudo apt update && sudo apt install python3-pip mongodb -y
sudo systemctl start mongod
git clone https://github.com/EzekielDada/Final-project.git
cd Final-project
pip3 install -r requirements.txt
python3 app.py
```

4. Access the app at `http://<your-ec2-public-ip>:5000`

For production, use Gunicorn behind Nginx and set `debug=False` in `app.py`.

---

## Notes

- Unchecking an expense checkbox sets that category's value to 0 in the database.
- The CSV export script can be re-run at any time to refresh `users.csv` with the latest data.
