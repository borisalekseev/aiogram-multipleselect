import dataclasses


@dataclasses.dataclass
class Topic:
    id: int
    url: str


topics = {
    1: Topic(1, "url1"),

    2: Topic(2, "url2"),

    3: Topic(3, "url3"),

    4: Topic(4, "url4"),

    5: Topic(5, "url5"),
}
