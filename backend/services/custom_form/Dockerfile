# Base Image
FROM node:16-alpine  

# Working Directory
WORKDIR /app

# Copy Dependency Files 
COPY package.json package-lock.json ./

# Install Dependencies
RUN npm install

# Copy the Rest of Your Application Code
COPY . .

# Expose the Application Port
EXPOSE 5012

# Start the Application in Debug Mode
CMD ["node", "--inspect=0.0.0.0:9229", "index.js"] 