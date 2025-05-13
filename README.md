# Secure Product Catalog API


## Overview
A secure microservice API for managing a product catalog, built with FastAPI. Features include JWT-based authentication, RSA encryption for sensitive fields, and CRUD operations.


## Technologies Used
- FastAPI
- SQLAlchemy
- SQLite
- JWT (via python-jose)
- RSA Encryption (via cryptography)


## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/product_catalog.git
   cd product_catalog


Create a virtual environment and activate it:

 bash
CopyEdit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install dependencies:

 bash
CopyEdit
pip install -r requirements.txt
3. Run the application:

 bash
CopyEdit
uvicorn app.main:app --reload
4. 5. Access the API documentation:

   * Swagger UI: http://127.0.0.1:8000/docs

   * ReDoc: http://127.0.0.1:8000/redoc

API Endpoints
      * POST /token: Obtain JWT token.

      * POST /products/: Create a new product.

      * GET /products/{product_id}: Retrieve product details.

      * PUT /products/{product_id}: Update product information.

      * DELETE /products/{product_id}: Delete a product.

Security Measures Implemented
         * Authentication: JWT-based authentication for secure access.

         * Encryption: RSA encryption for sensitive fields like description and category.

         * Input Validation: Pydantic models ensure data integrity.

         * Error Handling: Comprehensive error responses for various scenarios.

Future Improvements
            * Implement pagination and search functionality.

            * Add user roles and permissions.

            * Integrate with a more robust database like PostgreSQL.

            * Deploy using Docker and set up CI/CD pipelines.
``
