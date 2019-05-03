def filter(to_filter, filter_to_apply):
    """Filters a list or tuple

    Examples:
        users = [
                {"user": "barney", "age": 36, "active": True},
                {"user": "fred", "age": 40, "active": False},
            ]

        # Using a lambda function
        result = _.filter(users, lambda x: not x.get("active"))
        result == [{"user": "fred", "age": 40, "active": False}]

        # Using partial dictionary
        result = _.filter(users, {"age": 36, "active": True})
        result == [{"user": "barney", "age": 36, "active": True}]

        # Using a list with a property name and value
        result = _.filter(users, ["active", False])
        result == [{"user": "fred", "age": 40, "active": False}]

        # Using a list with a property name. The value must be truthy.
        result = _.filter(users, ["active"])
        result == [{"user": "barney", "age": 36, "active": True}]

    :param to_filter: the tuple or list to filter
    :param filter_to_apply: A function or list that defies the filter
    :return: A filtered list or tuple with the same type as to_filter
    """
    type_to_return = type(to_filter)

    if hasattr(filter_to_apply, "__call__"):
        return type_to_return([x for x in to_filter if filter_to_apply(x)])

    if isinstance(filter_to_apply, dict):
        filtered = []
        for x in to_filter:
            matched = 0
            keys_in_filter = filter_to_apply.keys()
            total_to_find = len(keys_in_filter)
            for key in keys_in_filter:
                if filter_to_apply[key] == x[key]:
                    matched += 1

            if total_to_find == matched:
                filtered.append(x)

        return type_to_return(filtered)

    if isinstance(filter_to_apply, list):
        if len(filter_to_apply) == 2:
            property_name = filter_to_apply[0]
            property_value = filter_to_apply[1]
            result = [x for x in to_filter if x.get(property_name) == property_value]
            return type_to_return(result)

        if len(filter_to_apply) == 1:
            property_name = filter_to_apply[0]
            result = [x for x in to_filter if bool(x.get(property_name))]
            return type_to_return(result)
