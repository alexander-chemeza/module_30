from typing import List

from fastapi import FastAPI, HTTPException
from sqlalchemy.future import select

import models
import schemas
from database import engine, session

# run with command uvicorn main:app --reload


app = FastAPI()


@app.on_event("startup")
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get("/recipes", response_model=List[schemas.RecipeShorOut])
async def recipes() -> List[models.Recipe]:
    res = await session.execute(
        select(models.Recipe).order_by(models.Recipe.views, models.Recipe.time)
    )
    return res.scalars().all()


@app.get("/recipes/{id}", response_model=schemas.RecipeOut)
async def recipe_info(id: int) -> models.Recipe:
    res = await session.execute(
        select(models.Recipe).where(models.Recipe.id == int(id))
    )
    if not res.scalars().first():
        raise HTTPException(status_code=404, detail="Recipe not found")
    return res.scalars().first()
