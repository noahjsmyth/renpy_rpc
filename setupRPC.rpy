init python:
    import os
    import subprocess
    import io
    discordrun = False
    if renpy.windows:
        try: process_listdis = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n") # Finds list of all running applications
        except:
                try:
                    process_listdis = subprocess.check_output("powershell (Get-Process).ProcessName", shell=True).lower().replace("\r", "").split("\n") # For W11 builds > 22000
                    
                    for x in range(len(process_listdis)):
                        process_listdis[x] += ".exe" # Adds .exe for compatibility
                except: pass            
        try:
            discord_list = ['Discord.exe', 'discord.exe']
            if list(set(process_listdis).intersection(discord_list)): # check if Discord.exe is in "process_list"
                discordrun = True # if successfully - turn discord_rpc on
                try: # unzip python3.6 to "game" folder, if "python.zip" exists
                    import zipfile
                    with zipfile.ZipFile('game/python.zip', "r") as z:
                        z.extractall("game/")
                    os.remove('game/python.zip') # delete "python.zip" for next getting "except"
                except:
                    pass
                state = "sp"
                try: 
                    open("{0}\game\state.txt".format(os.getcwd()), 'r')
                except:
                    io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
                else:
                    io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
                p = subprocess.Popen('cd {0}\game\PPython && python "{0}\game\discord.py"'.format(os.getcwd()), shell=True)
        except:
            pass
    whathere = None
    texthere = None
    textthere = None
    day = ""
    st = ""


label rpc: # callable label to set state. 
    if discordrun:
        python:
            import io
            io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
    return
