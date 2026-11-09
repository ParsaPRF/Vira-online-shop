# Vira Online Shop

A comprehensive Django-based e-commerce platform with RTL (Right-to-Left) support, specifically designed for Persian/Arabic markets.

## 🌟 Features

- **Multi-language Support**: Persian (RTL) and English interfaces
- **Advanced Admin Panel**: Customized with Unfold theme
- **User Management**: 
  - Custom user authentication
  - User profiles
  - Order history
- **Product Management**:
  - Category and subcategory system
  - Product variants
  - Image gallery
  - Stock management
- **Shopping Features**:
  - Shopping cart
  - Wishlist
  - Order tracking
  - ZarinPal payment integration
- **Support System**:
  - Ticket system
  - Customer support
- **Blog/Articles Section**

## 🛠 Technical Stack

### Core Technologies
- Python 3.13 (recommended; see the note in the setup section)
- Django 4.2.x
- Database: SQLite for local development (MySQL/PostgreSQL supported via `.env`)

## 🚀 Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/parhamIH/Vira-online-shop.git
cd Vira-online-shop
```

2. **Set Up Virtual Environment**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

> **Python version:** use Python 3.12 or 3.13. `pillow==11.0.0` has no wheel for
> Python 3.14, so on 3.14 pip falls back to building Pillow from source and
> fails with `The headers or library files could not be found for zlib`.

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment & Database Setup**
```bash
# Create your local .env from the template and edit it
copy .simple.env .env    # Windows
cp .simple.env .env      # Linux/Mac
```
The project runs on **SQLite by default** — no database server needed; the
default `.env` already points at `db.sqlite3`, so just run the migrations.

To use MySQL instead, set these keys in `.env` and create the database:
```sql
CREATE DATABASE shahan_shop CHARACTER SET utf8mb4;
```
```
DB_ENGINE=django.db.backends.mysql
DB_NAME=shahan_shop
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
```
(For PostgreSQL, set `DB_ENGINE=django.db.backends.postgresql` and install `psycopg`.)

5. **Run Migrations**
```bash
python manage.py migrate
```

6. **Create Superuser**
```bash
python manage.py createsuperuser
```

7. **Run Development Server**
```bash
python manage.py runserver
```

## 🌐 Available URLs

### Public URLs
- `/`: Homepage
- `/shop/`: Products listing
- `/shop/category/<slug>/`: Category products
- `/shop/product/<slug>/`: Product detail
- `/cart/`: Shopping cart
- `/provider/` : Provider dashboard
- `/account/`: User dashboard
- `/blog/`: Articles section

### User Account URLs
- `/account/login/`: User login
- `/account/register/`: User registration
- `/account/profile/`: User profile
- `/account/orders/`: Order history

### User Account URLs
- `/provider/register/`: Provider registration


### Admin URLs
- `/admin/`: Admin dashboard
- `/admin/products/`: Product management
- `/admin/orders/`: Order management
- `/admin/users/`: User management
- `/admin/support/`: Support tickets

## 💡 Key Features in Detail

### Security Features
- CSRF protection
- XSS prevention
- Secure password hashing
- SSL/HTTPS support
- Session security

### E-commerce Features
- Real-time inventory management
- Multiple payment methods
- Order tracking system
- Discount system
- Rating and review system

### Admin Features
- Custom admin dashboard
- Sales analytics
- User management
- Product management
- Order processing
- Support ticket system

## 📦 Project Structure
```
Vira Online Shop
├── frontend
│   ├── template
│   └── templateAdmin
├── main
│   ├── __pycache__
│   └── config
├── shop
│   ├── __pycache__
│   ├── account
│   ├── adminpanel
│   ├── articles
│   ├── cart
│   ├── categories
│   ├── home
│   ├── order
│   ├── products
│   ├── providers
│   ├── public
│   ├── reviews
│   ├── sitesettings
│   ├── support
│   └── utils
└── uploads
    ├── brands
    ├── categories
    ├── color-images
    ├── product-images
    └── uploads
```

## 🔧 Configuration

Key configuration files:
- `main/settings.py`: Main Django settings
- `main/urls.py`: URL routing
- `.env`: Environment variables (create it from `.simple.env` with `copy .simple.env .env`)

## 📝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

For support, email [parham.ilaghi@gmail.com] or open an issue in the repository.
