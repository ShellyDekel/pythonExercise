import os, json


def split_data(data, limit):
    for i in range(0, len(data), limit):
        yield data[i : i + limit]


def to_json(data, destination, base_filename, file_limit):
    if not data:
        raise ValueError("no data to load")
    else:
        os.makedirs(destination, exist_ok=True)

        if len(data) <= file_limit:
            with open(os.path.join(destination, base_filename + ".json"), "w") as json_file:
                json.dump(data, json_file, indent=2)
        else:
            splitted_data = list(split_data(data, file_limit))
            index = 1
            for chunk in splitted_data:
                with open(
                    os.path.join(destination, base_filename + str(index) + ".json"), "w"
                ) as json_file:
                    json.dump(chunk, json_file, indent=2)
                index += 1
