@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404
