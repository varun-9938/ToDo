from fastapi import FastAPI,Depends,status,HTTPException
from schemas import Schema
from models import Model
from database.Db_Conn import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Model.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/todo',status_code=status.HTTP_201_CREATED)
def create(request: Schema.Task,db:Session=Depends(get_db)):
    new_task=Model.Task(body=request.body)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.get('/todo/{id}')
def show(id,db:Session=Depends(get_db)):
    task=db.query(Model.Task).filter(Model.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'no task found for the id {id}')
    return task

@app.delete('/todo/{id}')
def destroy(id,db:Session=Depends(get_db)):
    db.query(Model.Task).filter(Model.Task.id == id).delete(synchronize_session=False)
    db.commit()
    return f'deleted the data with id {id}'


@app.put('/todo/{id}')
def update(id:int,request:Schema.Task, db:Session=Depends(get_db)):
    try:
        t=db.query(Model.Task).filter(Model.Task.id == id).first()
        t.body=request.body
        db.add(t)
        db.commit()
        return request
    except:
        return HTTPException(status_code=404,detail="task not found")
        


@app.get('/todo')
def all(db:Session=Depends(get_db)):
    tasks=db.query(Model.Task).all()
    return tasks



    