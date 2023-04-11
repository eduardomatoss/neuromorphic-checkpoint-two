from typing import List
from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, Undefined, config


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=False)
class FeedBase:
    temperature: float = field(metadata=config(field_name="field1"), default=float)
    humedad: float = field(metadata=config(field_name="field2"), default=float)
    atmospheric_station: float = field(metadata=config(field_name="field3"), default=float)
    atmospheric_sea: float = field(metadata=config(field_name="field4"), default=float)
    wind: float = field(metadata=config(field_name="field5"), default=float)
    rain_mm: float = field(metadata=config(field_name="field6"), default=float)
    direction_wind: float = field(metadata=config(field_name="field7"), default=float)
    uv: float = field(metadata=config(field_name="field8"), default=float)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=False)
class ThingspeakResponse:
    feeds: List[FeedBase] = field(default=None)
