WINDOW_CONFIGS = {
    "main": {
        "title": "Main Window",
        "width": 800,
        "height": 500,
        "icon": "main_icon.png"
    },
    "extract": {
        "title": "Data Extractor",
        "width": 800,
        "height": 500,
        "icon": "extract_icon.png"
    },
    "batch": {
        "title": "Batch Processor",
        "width": 900,
        "height": 600,
        "modal": False
    },
    "results": {
        "title": "Processing Results",
        "width": 1000,
        "height": 700,
        "resizable": False
    }
}

def get_window_config(window_type, overrides=None):
    config = WINDOW_CONFIGS.get(window_type, {}).copy()
    if overrides:
        config.update(overrides)
    return config