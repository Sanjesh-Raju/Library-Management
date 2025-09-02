# Use Frappe/Bench official image
FROM frappe/bench:latest

# Set working directory inside the container
WORKDIR /home/frappe/frappe-bench/apps/library_management

# Copy the app code into the container
COPY . .

# Optional: Copy README.md explicitly
COPY README.md /home/frappe/frappe-bench/apps/library_management/README.md

# Install Python requirements if any
RUN pip install -e .

# Default command to start bench
CMD ["bench", "start"]
