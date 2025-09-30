# Portfolio Django Web Application

A modern, responsive personal portfolio website built with Django, featuring dynamic animations, professional design, and interactive elements.

## 🌟 Features

- **Responsive Design**: Fully responsive layout that works on all devices
- **Dynamic Animations**: Smooth scroll animations and interactive elements
- **Skills Visualization**: Animated skill bars and circular progress indicators
- **Project Filtering**: Interactive project portfolio with filtering capabilities
- **Contact Form**: Functional contact form with Django backend processing
- **Modern UI**: Clean, professional design with neon accents and smooth transitions
- **SEO Optimized**: Proper meta tags and semantic HTML structure

## 🛠 Technologies Used

### Backend
- **Django 4.x**: Web framework
- **Python 3.8+**: Programming language
- **SQLite**: Default database (easily configurable)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom styling with CSS variables and animations
- **JavaScript**: Interactive functionality and animations
- **Boxicons**: Icon library
- **MixItUp.js**: Project filtering library

### Features
- Django Templates
- Static Files Management
- Form Handling
- Responsive Design
- Cross-browser Compatibility

## 📂 Project Structure

```
portfolio_project/
├── portfolio_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/
│   ├── templates/
│   │   └── 
│   │       ├── base.html
│   │       └── index.html
│   ├── static/
│   │   └── 
│   │       ├── css/
│   │       │   └── stylesheet.css
│   │       ├── js/
│   │       │   ├── script.js
│   │       │   └── mixitup.min.js
│   │       └── images/
│   │           └── (portfolio images)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/portfolio-django.git
cd portfolio-django
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv portfolio_env

# Activate virtual environment
# On Windows:
portfolio_env\Scripts\activate
# On macOS/Linux:
source portfolio_env/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Django Setup
```bash
# Apply migrations
python manage.py migrate

# Collect static files (for production)
python manage.py collectstatic

# Create superuser (optional)
python manage.py createsuperuser
```

### Step 5: Add Your Content
1. Replace placeholder images in `static/portfolio/images/`
2. Update personal information in `templates/portfolio/index.html`
3. Customize styling in `static/portfolio/css/stylesheet.css`

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view your portfolio!

## 📋 Requirements

Create a `requirements.txt` file with:
```
Django>=4.2.0
```

## ⚙️ Configuration

### Settings Configuration
Key settings in `Personal_Portfolio/settings.py`:

```python
# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Environment Variables (Recommended)
For production, use environment variables for sensitive settings:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- Database credentials

## 🎨 Customization

### Personal Information
Update the following in `index.html`:
- Name and title in hero section
- About me description
- Skills and percentages
- Project information
- Contact details
- Social media links

### Styling
Customize the look in `stylesheet.css`:
- Color scheme (CSS variables in `:root`)
- Fonts and typography
- Animation timings
- Responsive breakpoints

### Adding New Sections
1. Add HTML structure in `index.html`
2. Style in `stylesheet.css`
3. Add JavaScript functionality in `script.js`
4. Update navigation links

## 📱 Sections Included

1. **Hero/Home**: Introduction with animated text and personal info
2. **About**: Personal background and story
3. **Services**: Professional services offered
4. **Skills**: Technical and professional skills visualization
5. **Projects**: Portfolio showcase with filtering
6. **Contact**: Contact form and information
7. **Footer**: Social links and additional navigation



## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Paras Singh Adhikari**
- Email: parasadhikari132@gmail.com
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)

## 🎉 Acknowledgments

- Thanks to the Django community for the amazing framework
- Boxicons for the beautiful icons
- MixItUp.js for the portfolio filtering functionality
- Google Fonts for typography

## 📞 Support

If you have any questions or need help with setup, feel free to:
- Open an issue on GitHub
- Send an email to parasadhikari132@gmail.com
- Connect on LinkedIn

---

⭐ If you found this project helpful, please give it a star on GitHub!