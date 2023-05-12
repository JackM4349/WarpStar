[Unit]
Description=Super Mario World Mods
After=network.target

[Service]
User=flaskuser
Group=www-data
WorkingDirectory=/home/flaskuser/smw-mods
Environment="PATH=/home/flaskuser/smw-mods/venv/bin"
ExecStart=/home/flaskuser/smw-mods/venv/bin/gunicorn --workers 4 --bind unix:smw-mods.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
