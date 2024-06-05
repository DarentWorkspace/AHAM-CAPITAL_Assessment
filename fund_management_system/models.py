class Fund:
    def __init__(self, fund_id, name, manager_name, description, nav, date_of_creation, performance):
        self.fund_id = fund_id
        self.name = name
        self.manager_name = manager_name
        self.description = description
        self.nav = nav
        self.date_of_creation = date_of_creation
        self.performance = performance

    def to_dict(self):
        return {
            "fund_id": self.fund_id,
            "name": self.name,
            "manager_name": self.manager_name,
            "description": self.description,
            "nav": self.nav,
            "date_of_creation": self.date_of_creation,
            "performance": self.performance
        }
