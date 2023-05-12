import os

@app.route('/download/<mod_id>')
def download(mod_id):
    try:
        mod_path = os.path.join(app.config['MOD_DIR'], f'{mod_id}.zip')
        return send_file(mod_path, as_attachment=True)
    except FileNotFoundError:
        return 'Mod not found', 404
