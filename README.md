# AppliMessagerie

AppliMessagerie is a messaging platform developed by Romain JAHIER, Célian Loisel, and Sacha Harel. It allows users to communicate within groups and manage conversations seamlessly.

## Key Features

- Real-time group messaging.
- Group creation and management.
- Display of messages with timestamps.
- User-friendly interface for sending and managing messages.

## Installation

To install AppliMessagerie, follow these steps:

1. Ensure you have Python and pip installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the directory where you cloned the repo:

```bash
cd AppliMesssagerie
```

4.Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

Create a .env file in the root directory and set up the following environment variables:
- SECRET_KEY: A secret key for your application.
- SQLALCHEMY_DATABASE_URI: The URI for connecting to your MySQL database.

### Example:

```bash
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@host/db_name
```

Replace the placeholders with your actual MySQL settings.

### Run the application using:
## Usage

To run the application:

1. Open `main.py` and replace `host='172.20.10.4'` with the IP address of the machine where you want to run the server.
2. Replace `port=5000` with your desired port number if necessary.

Run the application using:

```bash
python main.py
```
