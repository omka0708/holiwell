from pydantic import BaseModel, Field

from app.trainer import schemas as trainer_schemas


class LessonCreate(BaseModel):
    title: str
    description: str
    trainer_id: int
    course_id: int | None


class LinkedLessonRead(BaseModel):
    id: int
    lesson_id: int
    linked_lesson_id: int


class LessonRead(BaseModel):
    id: int
    title: str
    description: str
    trainer: trainer_schemas.TrainerRead | None
    course_id: int | None
    path_to_cover: str | None
    path_to_video: str | None
    path_to_audio: str | None
    links_before: list[LinkedLessonRead]
    links_after: list[LinkedLessonRead]


class LessonUpdate(BaseModel):
    title: str | None
    description: str | None
    trainer_id: int | None
    course_id: int | None
