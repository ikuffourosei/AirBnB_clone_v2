#!/usr/bin/env bash
# a Bash script that sets up web servers for the deployment of web_static

# Install Nginx if not already installed
command -v nginx >/dev/null || {
    sudo apt-get update
    sudo apt-get install -y nginx
}

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
sudo tee /data/web_static/releases/test/index.html >/dev/null <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is a fake text</h1>
</body>
</html>
EOF

# Remove existing symbolic link if it exists
[ -L /data/web_static/current ] && sudo rm /data/web_static/current

# Create symbolic link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
sudo sed -i 's|^\(\s*location /hbnb_static {\).*|\1\n\t\talias /data/web_static/current/;|' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
