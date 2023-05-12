from pysondb import getDb


class Database:
    def __init__(self, database_path: str) -> None:
        self.database = getDb(database_path)

    def __call__(self) -> str:
        return str(self.database)
    
    def push(self, model: dict[str, any]) -> None:
        self.database.add(model)

    def update(self, id: int, key: str, value: any) -> None:
        self.database.updateById(id, {key : value})

    def update_model(self, id: int, model: dict[str, any]) -> None:
        self.database.updateById(id, model)

    def get(self, key: str, value: str, parameter: str) -> any:
        return self.database.getByQuery({key : value})[0][parameter]
    
    def get_instance(self, key: str, value: any) -> dict[str, any]:
        return self.database.getByQuery({key : value})[0]
    
    def get_all(self) -> list[dict[str, any]]:
        return self.database.getAll()

    def contains(self, key: str, value: any) -> bool:
        return True if self.database.getByQuery({key : value}) != [] else False
