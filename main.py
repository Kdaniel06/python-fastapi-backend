import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Course(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    level: str
    duration: int # Hours
    
## Simulate db
courses_db = []

# C(R)UD: READ
@app.get("/courses/", response_model=List[Course])
def get_all_courses():
    return courses_db

# C(R)UD: READ
@app.get("/courses/{searched_id}", response_model=Course)
def get_course(searched_id: str):
    course = next((course for course in courses_db if course.id == searched_id), None) # Next => First appearance in the array
    if course is None:
        raise HTTPException(status_code=404, detail="Course Not founded")
    return course

# (C)RUD: CREATE
@app.post("/courses/", response_model=Course)
def create_courses(course:Course):
    course.id = str(uuid.uuid4()) # Create an unique id
    courses_db.append(course)
    return course
    

# CR(U)D: UPDATE
@app.put("/courses/{searched_id}", response_model=Course)
def update_course(searched_id: str, updated_course: Course):
    course = next((course for course in courses_db if course.id == searched_id), None) # Next => First appearance in the array
    if course is None:
        raise HTTPException(status_code=404, detail="Course Not founded")
    updated_course.id = course.id
    index = courses_db.index(course) # Find the exact position of the course
    courses_db[index] = updated_course
    return updated_course
    

# CRU(D): DELETE
@app.delete("/courses/{searched_id}", response_model=Course)
def delete_course(searched_id: str):
    course = next((course for course in courses_db if course.id == searched_id), None) # Next => First appearance in the array
    if course is None:
        raise HTTPException(status_code=404, detail="Course Not founded")
    courses_db.remove(course) # Delete the founded course
    return course