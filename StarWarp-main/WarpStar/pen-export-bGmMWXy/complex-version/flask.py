from flask import Flask, render_template, request, send_file
from ips import apply_ips_patch
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    rom_file = request.files['rom']
    mod_file = request.files['mod']

    if not rom_file or not mod_file:
        return 'Please select both a ROM file and a mod file.'
    # Validate file types
    if rom_file.content_type != 'application/octet-stream' or mod_file.content_type != 'application/octet-stream':
        return 'Please select valid binary files.'

    # Read binary data from files
    rom_data = rom_file.read()
    mod_data = mod_file.read()

    # Apply mod patch to ROM
    try:
        patched_data = apply_ips_patch(rom_data, mod_data)
    except Exception as e:
        return 'Failed to apply mod patch: ' + str(e)

    # Return patched ROM file as a download
    file_obj = io.BytesIO(patched_data)
    file_obj.seek(0)
    return send_file(file_obj, attachment_filename='smw_modded.smc', as_attachment=True)
from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

   
