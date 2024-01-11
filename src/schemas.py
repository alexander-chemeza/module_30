from pydantic import BaseModel


class BaseRecipe(BaseModel):
    name: str
    views: int
    time: int
    ingredients: str
    description: str


class RecipeIn(BaseRecipe):
    ...


class RecipeOut(BaseRecipe):
    id: int

    class Config:
        orm_mode = True


class BaseRecipeShort(BaseModel):
    name: str
    views: int
    time: int


class RecipeShortIn(BaseRecipeShort):
    ...


class RecipeShorOut(BaseRecipeShort):
    id: int

    class Config:
        orm_mode = True
