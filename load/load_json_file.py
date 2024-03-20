import os, json, logging

logger = logging.getLogger(__name__)


def to_json(data, destination, base_filename, file_limit):
    if not data:
        logger.error("data list given is empty")
        raise ValueError("no data to load")
    else:
        if not os.path.isdir(destination):
            logger.info("generating directories")
            os.makedirs(destination)

        if len(data) <= file_limit:
            logger.info("loading data into json file")
            with open(
                os.path.join(destination, base_filename + ".json"), "w"
            ) as json_file:
                json.dump(data, json_file, indent=2)

            logger.info("file generated: " + json_file.name)
        else:
            logger.info("data extends file limit, creating multiple files")
            splitted_data = [
                data[i : i + file_limit] for i in range(0, len(data), file_limit)
            ]
            index = 1
            for chunk in splitted_data:
                with open(
                    os.path.join(destination, base_filename + str(index) + ".json"), "w"
                ) as json_file:
                    json.dump(chunk, json_file, indent=2)
                logger.debug("file generated: " + json_file.name)
            index += 1

            logger.info("files generated at '" + destination + "'. file count: " + str(len(splitted_data)))
