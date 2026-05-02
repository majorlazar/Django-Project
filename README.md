# 🐝 GadgetHive

> **Your buzzing hub for all things tech** — buy, sell, and trade computers, laptops, peripherals, and gadgets.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Hosted on PythonAnywhere](https://img.shields.io/badge/Hosted-PythonAnywhere-orange)](https://christylazar.pythonanywhere.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌐 Live Demo

👉 **[https://christylazar.pythonanywhere.com/](https://christylazar.pythonanywhere.com/)**

---

## 📖 About

**GadgetHive** is a full-stack Django e-commerce web application designed for buying, selling, and trading used computers and gadgets. It connects tech enthusiasts with quality hardware at competitive prices — making the process simple, fast, and reliable.

---

## ✨ Features

- 🛒 **Product Listings** — Browse used laptops, HDDs, SSDs, RAM, and more
- 🔐 **User Authentication** — Register, login, and manage your account
- 📦 **Product Management** — Add, edit, and remove listings
- 🔄 **Buy / Sell / Trade** — Multi-mode transaction support
- 🚚 **Fast & Free Shipping** — Seamless delivery integration
- 📞 **24/7 Support** — Dedicated help section
- ↩️ **Hassle-Free Returns** — Simple return flow
- 📱 **Responsive Design** — Mobile-friendly UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite / MySQL |
| Hosting | PythonAnywhere |
| Version Control | Git & GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip
- virtualenv (recommended)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/majorlazar/gadgethive.git
cd gadgethive

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (optional, for admin access)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
gadgethive/
├── gadgethive/          # Project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/               # Main app (products, views, models)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/              # CSS, JS, images
├── templates/           # Base HTML templates
├── manage.py
└── requirements.txt
```

---

## 📸 Screenshots

| Home Page | Product Listing |
|---|---|
| ![Home](https://christylazar.pythonanywhere.com/static/images/pc.png) | *Login to explore products* |

---

## 🔧 Configuration

Create a `.env` file in the root directory for sensitive settings:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=your-database-url
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Christylazar Antony**

- 🌐 Portfolio: [christylazar.pythonanywhere.com](https://christylazar.pythonanywhere.com/)
- 💼 LinkedIn: [linkedin.com/in/christylazarantony](https://linkedin.com/in/christylazarantony/)
- 🐙 GitHub: [github.com/majorlazar](https://github.com/majorlazar)

---

> Copyright © Christylazar Antony. All Rights Reserved.
