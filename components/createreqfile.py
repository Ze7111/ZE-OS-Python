def req(): 
    import os
    try:
        os.system("pip freeze > data\\requirements.txt")
        return "updated requirements file"
    except:
        return "failed to create a requiremnts file"