from pipeop import pipes
from prefect import task
from prefect.utilities.debug import raise_on_exception


@pipes
def flow_etl_kindle_clippings_to_folder():

    with Flow("Extract clippings from Kindle to files") as flow:

        clippings_local = _extract_kindle_clippings()
        clippings_by_book = (
            _load_clippings_to_string(clippings_local) 
            >> _transform_clippings_into_defaultdict 
        )

        _save_clippings_to_files(clippings_by_book)

    return flow


if __name__ == '__main__':
    flow = flow_etl_kindle_clippings_to_folder()

    with raise_on_exception():
        flow.run()
