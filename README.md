# pyshop

pyshop is a simple, basic e-commerce site built with **Django**. This project serves as a playground for exploring Django features and concepts related to building a shopping platform.

---

## Features

* **Product Listing:** View a catalog of available products.
* **Shopping Cart:** Add products to a cart and manage quantities.
* **Checkout Process:** A basic checkout flow (without real payment integration).
* **User Authentication:** Simple user login and registration.

---

## Getting Started

### Prerequisites

* **Python 3.8+**
* **pip**

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Longman-max/py-shop.git
    cd pyshop
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

You can now access the site at `http://127.0.0.1:8000/`.

---

## Project Structure
`pyshop/`
├── `manage.py`
├── `pyshop/`             `# Main Django project directory`
│   ├── `settings.py`
│   └── `urls.py`
└── `shop/`               `# E-commerce app`
    ├── `models.py`       `# Product and cart models`
    ├── `views.py`        `# Logic for product pages and cart management`
    ├── `templates/`      `# HTML templates`
    └── `static/`         `# CSS, JS, and images`

---

## License

This project is licensed under the **MIT License**.
