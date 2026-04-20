# Samkelo Qonda - Data Portfolio (Streamlit Version)

A fully responsive Streamlit web app version of your professional data portfolio. Built with the same dark theme, cyan accent color, and all your real content preserved exactly as in the HTML version.

## Features

✅ **All Content Preserved**
- Hero section with name, roles, and CTA buttons
- About section with biography and technical skills
- 6 Featured projects with GitHub links
- 11 Certifications from DataCamp, Forage, and other platforms
- 3 Work experience entries with detailed descriptions
- Contact section with all social links

✅ **Dark Theme**
- Cyan accent color (#00e5ff) matching your original design
- Professional styling with hover effects
- Fully responsive layout

✅ **Interactive Features**
- All GitHub project links are clickable
- LinkedIn and email contact buttons
- **CV Download Button** - generates a downloadable text file with your complete resume
- Smooth section navigation

## Installation & Setup

### 1. Install Python (if not already installed)
Download from [python.org](https://www.python.org/downloads/)

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## File Structure

```
Portfolio/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **Framework:** Streamlit
- **Styling:** Custom CSS with markdown
- **Data Format:** HTML5 content converted to Streamlit components

## Download Your CV

The app includes a dedicated CV download button that generates a formatted text file (Samkelo_Qonda_CV.txt) containing:
- Contact information
- Professional summary
- Technical skills breakdown
- Work experience with bullet points
- Featured projects with links
- Complete certifications list
- Languages

Click the "📥 Download CV" button in the contact section to download.

## Customization Tips

To modify content, edit `app.py`:

- **Update project links:** Search for `github.com/samkeloqonda205-wq/` and replace URLs
- **Change colors:** Modify the CSS variables in the `st.markdown()` style section:
  - `--accent: #00e5ff` (cyan)
  - `--bg: #080b12` (dark background)
- **Update skills:** Modify the skill chips under the About section
- **Add new projects:** Copy the project card template and update with new data

## Deployment Options

### Deploy to Streamlit Cloud (Free & Recommended)

1. Push your files to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account and deploy your repo
4. Your portfolio will be live with a public URL

### Deploy to Heroku, AWS, or other platforms
The app is compatible with any platform that supports Python and Streamlit.

## Features Comparison

| Feature | HTML Version | Streamlit Version |
|---------|-------------|------------------|
| Dark theme | ✅ | ✅ |
| Cyan accents | ✅ | ✅ |
| All projects | ✅ | ✅ |
| All certifications | ✅ | ✅ |
| All experience | ✅ | ✅ |
| GitHub links | ✅ | ✅ |
| **CV Download** | ❌ | ✅ |
| Mobile responsive | ✅ | ✅ |
| Interactive elements | Partial | ✅ |
| Easy to customize | ❌ | ✅ |

## Troubleshooting

**App won't run?**
- Make sure Python 3.7+ is installed
- Run: `pip install streamlit --upgrade`

**CSS styling looks off?**
- Clear browser cache (Ctrl+Shift+Del)
- Refresh the page

**Can't download CV?**
- Check browser download permissions
- Try a different browser

## License

This portfolio is your personal property. Feel free to customize and deploy as needed.

---

**Need help?** Let me know and I can assist with further customizations or deployment!
