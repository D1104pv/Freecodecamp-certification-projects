test_settings = {"theme": "light", "volume" : "high"}

# adds settings while also checking if settings is already present
def add_setting(settings: dict, new_setting: tuple):
    newsetting = []
    # converting all items to lower case for uniformity
    for new in new_setting:
        newsetting.append(new.lower())
    
    setting = newsetting[0]
    value = newsetting[1]

    if setting in settings.keys():
        return f"Setting \'{setting}\' already exists! Cannot add a new setting with this name."
    else:
        settings[setting] = value
        return f"Setting \'{setting}\' added with value \'{value}\' successfully!"

# updates existing settings or retirns message if setting not found
def update_setting(settings: dict, update: tuple):
    updates =  []
    for i in update:
        updates.append(i.lower())
    
    setting = updates[0]
    value = updates[1]

    if setting in settings.keys():
        settings[setting] = value
        return f"Setting \'{setting}\' updated to \'{value}\' successfully!"
    else:
        return f"Setting \'{setting}\' does not exist! Cannot update a non-existing setting."

# deletes existing setting or returns message if setting not found
def delete_setting(settings: dict, key: str):
    key = key.lower()

    if key in settings.keys():
        settings.pop(key)
        return f"Setting \'{key}\' deleted successfully!"
    else:
        return "Setting not found!"

# displays current setting configurations
def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result