import datetime
from models.models import TableItem


class FilterManagers:

    @staticmethod
    def get_table_items_include_user_input(user_input: str, column: str) -> list:
        """ Function take user_input and column and return list of table items match user input """
        table_items_include_input = []
        query = TableItem.query.all()
        all_items = [item.json() for item in query]
        for item in all_items:
            if user_input in str(item[column]):
                table_items_include_input.append(item)
        return table_items_include_input

    @staticmethod
    def get_table_items_with_condition(user_input: str, column: str, condition: str) -> list:
        """ Function take user_input, column and condition, make search table for data according to conditions and
        return result as list of table items"""
        if column == 'date':
            user_datetime_obj = datetime.datetime.strptime(user_input, '%d-%m-%Y')
            if condition == 'equal':
                query = TableItem.query.filter(TableItem.date == user_datetime_obj).all()
            elif condition == 'more':
                query = TableItem.query.filter(TableItem.date > user_datetime_obj).all()
            elif condition == 'less':
                query = TableItem.query.filter(TableItem.date < user_datetime_obj).all()
        elif column == 'title':
            if condition == 'equal':
                query = TableItem.query.filter(TableItem.title == user_input).all()
            elif condition == 'more':
                query = TableItem.query.filter(TableItem.title > user_input).all()
            elif condition == 'less':
                query = TableItem.query.filter(TableItem.title < user_input).all()
        elif column == 'amount':
            if condition == 'equal':
                query = TableItem.query.filter(TableItem.amount == int(user_input)).all()
            elif condition == 'more':
                query = TableItem.query.filter(TableItem.amount > int(user_input)).all()
            elif condition == 'less':
                query = TableItem.query.filter(TableItem.amount < int(user_input)).all()
        elif column == 'distance':
            if condition == 'equal':
                query = TableItem.query.filter(TableItem.distance == float(user_input)).all()
            elif condition == 'more':
                query = TableItem.query.filter(TableItem.distance > float(user_input)).all()
            elif condition == 'less':
                query = TableItem.query.filter(TableItem.distance < float(user_input)).all()
        result = [item.json() for item in query]
        return result

