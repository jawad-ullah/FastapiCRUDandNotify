from fastapi import FastAPI
from winotify import Notification , audio
Notes={
    1:{"Title":"Physics", "description": "This is Physics"},
    2:{"Title":"Chemistry", "description": "This is Chemistry"},
    3:{"Title":"Maths", "description": "This is Maths"},
    4:{"Title":"Commerce", "description": "This is Commerce"},
}

icons_rel_path=r"C:\Users\O Consulting\Desktop\FastApi\Icons/"

def notification(title:str, msg:str, icon:str):
    notify=Notification(
        app_id="Notes App",
        title=title,
        msg=msg,
        duration="long",
        icon=icons_rel_path+icon

    )
    notify.set_audio(audio.Reminder, loop=False)
    notify.show()


app =  FastAPI()

#get -movies
@app.get("/")
def get_all_notes():
    return Notes
# get movie
@app.get("/{id}")
def get_all_notes(id:int):
    note=Notes[id]
    return note

# post  - Note
@app.post("/")
def post_note(name,desc):
    obj={"name":name, "description":desc}
    key=len(Notes)+1
    Notes[key]=obj
    notification("Create","New Note is added","create.png")
    return Notes

# Put  - Note
@app.put("/")
def post_note(id:int , Title: str, desc: str):
    keys=Notes.keys()
    if id in keys:
        Notes[id]["Title"]=Title
        Notes[id]["description"]=desc
        notification("Update","Note is Updated","update.png")
        return Notes
    else:
        notification("Not Found","Note is not found","not.png")

# delete - Note
@app.delete("/")
def delete_note(id:int):
    if not id in Notes.keys():
        notification("Not Found","Note is not found","not.png")
    else:
        del Notes[id]
        notification("Deleted","Note is Deleted Successfully","delete.jpg")
    return Notes