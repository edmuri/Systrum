# Use a small Node image
FROM node:20-alpine

WORKDIR /app

# Copy package files first for caching
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of your frontend code
COPY . .

# Expose Vite port
EXPOSE 5173

# Disable automatic browser opening
ENV BROWSER=none

# Start Vite dev server accessible outside container
CMD ["npm", "run", "dev", "--", "--host"]