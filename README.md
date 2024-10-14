
# Simon Says Telegram Bot

This project is a **Telegram bot** for a "Simon Says" game, designed to be used for orientation week activities at a university. The bot allows users (students) to register, join or create groups, and participate in a team-based game where they complete tasks for points. Admins can manage the game, create tasks, and monitor group progress.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Admin Commands](#admin-commands)
- [Task Flow](#task-flow)

## Features

1. **User Registration**: Users can register by providing their full name and ID number.
2. **Group Management**: Users can create or join groups (up to 8 members per group).
3. **Task Assignment**: Users receive tasks with different difficulty levels (easy, medium, hard) to complete and submit.
4. **Admin Panel**: Admins can add tasks, start the game, view group progress, and track task submissions.
5. **Game Tracking**: The bot automatically tracks each group's score and updates task statuses.

## Project Structure

```
simon_says_bot/
│
├── db/
│   └── bot_db.sqlite           # SQLite database file
├── src/
│   ├── bot.py                  # Main bot logic
│   ├── admin.py                # Admin-related commands
│   ├── registration.py         # User registration flow
│   ├── tasks.py                # Task management logic
│   └── utils.py                # Database helpers and utilities
├── requirements.txt            # Dependencies for the project
├── README.md                   # This file
└── .env                        # Environment variables (e.g., Telegram Bot Token)
```

### Description of Files:

- `bot.py`: This file contains the main logic of the bot, including command handlers and conversation flow for user registration, group joining, and task assignment.
- `admin.py`: This file contains the functionality for admin commands such as adding tasks, viewing teams, and starting the game.
- `registration.py`: Handles the user registration process, including input validation and database updates.
- `tasks.py`: Handles the logic for fetching and assigning tasks to groups.
- `utils.py`: Contains utility functions like database connection management.

## Installation

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8+
- Telegram Bot Token (which you can get by talking to [@BotFather](https://core.telegram.org/bots#botfather) on Telegram).
- SQLite (already included with Python)

### Steps to Install:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/simon_says_bot.git
    cd simon_says_bot
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your Telegram bot token:
    ```
    TOKEN=your-telegram-bot-token
    ```

5. **Run the bot**:
    ```bash
    python src/bot.py
    ```

The bot will start and begin polling Telegram for updates.

## Usage

### 1. Start the Bot

Once the bot is running, users can interact with it via Telegram by using the following commands:

- `/start` – Begins interaction with the bot and presents the main menu.
- `Register for the game` – Registers a new user by asking for their full name and ID number.
- `Join a group` – Allows users to join an existing group using a group ID.
- `Login as admin` – Allows admins to authenticate and manage the game.

### 2. Admin Commands

Admins have access to the following special commands:

- `/addtask <description> <difficulty> <points>`: Adds a new task to the game.
- `/viewteam <team_name>`: Shows the details of a specific team, including the team's score and members.
- `/startgame`: Starts the game for all teams, enabling task submissions.

### 3. Task Completion Flow

1. **Assign Tasks**: Once the game starts, tasks are randomly assigned to groups based on difficulty.
2. **Submit Tasks**: Users submit task files (photos or videos) for approval.
3. **Admin Review**: Admins approve or reject submissions, and points are awarded accordingly.

## Database Schema

Here is an overview of the tables created in the SQLite database:

- **Teams**: Stores team details (name, points, etc.).
  ```sql
  CREATE TABLE IF NOT EXISTS Teams (
      team_id INTEGER PRIMARY KEY AUTOINCREMENT,
      team_name TEXT NOT NULL,
      points INTEGER DEFAULT 0
  );
  ```

- **Tasks**: Stores tasks with difficulty levels and points.
  ```sql
  CREATE TABLE IF NOT EXISTS Tasks (
      task_id INTEGER PRIMARY KEY AUTOINCREMENT,
      task_name TEXT NOT NULL,
      difficulty TEXT NOT NULL,
      points INTEGER
  );
  ```

- **Submissions**: Stores task submissions by teams.
  ```sql
  CREATE TABLE IF NOT EXISTS Submissions (
      submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
      team_id INTEGER,
      task_id INTEGER,
      status TEXT DEFAULT 'pending',
      file_path TEXT,
      FOREIGN KEY (team_id) REFERENCES Teams (team_id),
      FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
  );
  ```

- **Admins**: Stores admin login information.
  ```sql
  CREATE TABLE IF NOT EXISTS Admins (
      admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      password TEXT NOT NULL
  );
  ```

- **TeamMembers**: Stores team member details linked to their team.
  ```sql
  CREATE TABLE IF NOT EXISTS TeamMembers (
      member_id INTEGER PRIMARY KEY AUTOINCREMENT,
      team_id INTEGER,
      member_name TEXT NOT NULL,
      FOREIGN KEY (team_id) REFERENCES Teams (team_id)
  );
  ```

## Admin Commands

Admins can use the following commands to manage the game:

1. **/login <username> <password>**: Log in as an admin using predefined credentials.
2. **/addtask <description> <difficulty> <points>**: Add a task to the game.
3. **/viewteam <team_name>**: View the details of a specific team, including members and current points.
4. **/startgame**: Start the game and allow groups to begin completing tasks.

## Task Flow

1. Admins add tasks to the database using the `/addtask` command.
2. Groups complete tasks and submit them for review.
3. Admins approve or reject task submissions.
4. The group with the most points at the end of the game wins.

## Future Improvements

- Implement scoring visualization via the bot.
- Create a web dashboard for admin management.
- Add more security for admin login, such as token-based authentication.

