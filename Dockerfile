FROM python:3.11-slim
WORKDIR /app
COPY inventory_manager.py .
COPY Product.py .
COPY Inventory.py .
COPY DigitalProduct.py .
COPY PhysicalProduct.py .
COPY CanBeShipped.py .
COPY Order.py .
COPY OrderLine.py .
COPY Supplier.py .
COPY test.py .
CMD [ "python", "inventory_manager.py" ]