# Ren'Py RPC
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=10)](https://github.com/qwertyquerty/pypresence) 

[Download python.zip](https://drive.google.com/file/d/1Oubxytg3W_AzHJ4jVwCT-Aa3rjB-8FeX/view?usp=drivesdk)

Originally created by FUFSoB.

## Instructions:
   1. Put `discord.py`, `setupRPC.rpy` and `python.zip` in your `game` folder.
   2. Edit your splash.rpy __[all labels currently exist, you just need to add code]__ *(code below)*
   3. Create your own Rich Presence application on [Discord API page](https://discordapp.com/developers/applications/), [Video Guide](https://youtu.be/jGF-L0iEBH4?t=8s) (till 0:58)
   4. Edit `discord.py`, using your `application id`; adding `assets` and `text` you wanted.
   5. In `discord.py` add your own new states (make sure the names are memorable).
   6. Add `$ state = "state name"` everywhere you wanted status to change.
   7. Just run your game. First of all - it'll unzip `python.zip` and delete it after that. Then it will rewrite status to "Loading" and run `discord.py`.
<details>
  <summary>splash.rpy</summary>
  
  ```renpy
label after_load:
    # ...
    if discordrun:
        python:
            try:
                import io
                import os
                io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
            except:
                import io
                open("game/state.txt", 'w+')
                io.open("game/state.txt", 'w+', encoding = "utf-8").write("err3")
                state = "err3"
    # ...
    return

label before_main_menu:
    # ...
    if discordrun:
        python:
            import io
            state = "mm"
            io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
    # ...
    return

label quit:
    # ...
    if discordrun:
        python:
            import os
            os.popen('taskkill /f /im python.exe')
    # ...
    return
  ```
  
</details>


