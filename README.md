# GitHub Analyzer

A fast, modern React + Tailwind CSS web app that analyzes a GitHub user’s public repositories and visualizes insights like top languages, commit activity, and repo popularity with clean, responsive charts.


## Project Overview

GitHub Analyzer lets you enter any GitHub username and instantly see:

- A quick profile overview (avatar, name, bio, location, links)
- Repo insights (counts, top repo, activity overview)
- Visualizations for languages, weekly commits, and stars/forks
- Interactive modals for followers/following and repositories (with README preview)

It integrates with the GitHub REST API, handles common errors (rate limits, not found), and ships with a polished dark theme powered by Tailwind CSS.


## Features

- User-friendly UI with keyboard-friendly search
- GitHub API integration (public data)
- Data visualization with Chart.js (via react-chartjs-2)
- Dark mode by default (Tailwind utilities)
- Responsive layout for desktop and mobile
- Followers/Following exploration and repo list with README preview
- Error handling and informative messages (e.g., rate limits)


## Tech Stack

- React 18
- Tailwind CSS 3 (with PostCSS + Autoprefixer)
- Axios (API requests)
- Chart.js 4 + react-chartjs-2 5


## File Structure

```
github-analyzer/
├─ frontend/                     # React + Tailwind web app
│  ├─ public/
│  │  └─ index.html
│  ├─ src/
│  │  ├─ assets/
│  │  │  └─ images/
│  │  │     └─ Background.jpeg   # Optional background for intro page
│  │  ├─ components/             # Reusable UI + charts
│  │  │  ├─ UsernameForm.jsx
│  │  │  ├─ UserProfile.jsx
│  │  │  ├─ StatsCards.jsx
│  │  │  ├─ LanguageChart.jsx
│  │  │  ├─ CommitChart.jsx
│  │  │  ├─ StarForkChart.jsx
│  │  │  └─ CommitTrendChart.jsx
│  │  ├─ App.jsx                 # App shell, views, layout
│  │  ├─ index.css               # Tailwind directives + utility classes
│  │  └─ index.js                # React entry
│  ├─ package.json
│  ├─ tailwind.config.js
│  └─ postcss.config.js
│
├─ backend/ (optional)           # Flask API server (if running locally)
│  ├─ app.py
│  ├─ services/
│  │  └─ github_api.py
│  └─ requirements.txt
└─ README.md
```


## Installation & Setup

Prerequisites:

- Node.js (LTS) and npm  
- Python 3.9+ for the Flask backend

### Quick Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Vishesh0-7/Github-Analyzer.git
cd Github-Analyzer
```

2. **Setup GitHub Token (Important!):**
```bash
# Run the setup script for easy configuration
python setup.py

# OR manually create backend/.env with:
# GITHUB_TOKEN=your_github_token_here
```

3. **Install and run the backend:**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

4. **Install and run the frontend:**
```bash
cd frontend
npm install
npm start
```

### GitHub Token Setup

To avoid rate limits, you need a GitHub Personal Access Token:

1. Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
2. Generate new token → Token (classic)
3. Select scope: `public_repo` (or `repo` for private repos)
4. Copy the token and add it to `backend/.env`:

```env
GITHUB_TOKEN=your_token_here
```

### Production Build

```bash
# Frontend build
cd frontend
npm run build

# Backend with environment
cd backend
python app.py
```

Optional: Avoid GitHub rate limits using a Personal Access Token (no scopes required):

```powershell
# Set for this shell only
$env:GITHUB_TOKEN = 'ghp_your_personal_token_here'

# Or set persistently for future shells
setx GITHUB_TOKEN "ghp_your_personal_token_here"
```


## Usage

1) Start the frontend dev server:

```powershell
cd frontend
npm start
```

2) If you’re using the local API, start the Flask backend in another terminal:

```powershell
cd backend
$env:FLASK_APP = 'app.py'
flask run
```

3) Open http://localhost:3000 in your browser.

4) Enter a GitHub username. The app will fetch and render:

- Profile information (avatar, name, bio)
- Language distribution and weekly commit activity
- Stars vs forks per repo
- Commit trend across repositories
- Followers/following lists and a repository list with README preview

Tips:

- Click the app title to return to the intro page.
- The top navigation search appears after you’ve viewed results, so you can quickly analyze another user.


## Future Improvements

- GitHub OAuth authentication for higher rate limits
- Custom dashboards and saved views per user
- Markdown-rendered READMEs with safe sanitization
- Client-side and/or server-side caching to reduce API calls
- Pagination and filtering for large repo lists
- PWA support and offline view for previously fetched data
- AI-assisted summaries and code metrics for repositories


## License

This project is licensed under the MIT License. See the LICENSE file for details.