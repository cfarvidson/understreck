def filter(to_filter, filter_to_apply):
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
