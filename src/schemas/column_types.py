from pydantic import Field
from typing import Annotated

Name = Surname = Patronymic = Annotated[
    str, Field(pattern="[\w'.]+", examples=["Ibram", "Prostoviy", "Evegenievich"])
]
Teacher = Annotated[
    str,
    Field(
        pattern=r"([\w'.]+ ){1,2}\w*",
        examples=[
            "Bibov Ibrahim Aranovich",
            "Dadayanow Abrham",
        ],
    ),
]
Cabinet = Annotated[str, Field(pattern=r"\d{1,4}\w*", examples=["2134т"])]
timeHHMM = Annotated[str, Field(pattern=r"([0-1]\d|2[0-3]):[0-5]\d")]
