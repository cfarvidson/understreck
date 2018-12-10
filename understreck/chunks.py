import math


def calculate_size(to_chunk, num_chunks):
    """Calculate the max chunk size for each new chunk of a list.
    
    Arguments:
        to_chunk {list} -- [description]
        num_chunks {int} -- [description]
    
    Returns:
        int -- The max size for each chunk
    """

    chunk_max_size = float(len(to_chunk)) / float(num_chunks)
    return int(math.ceil(chunk_max_size))


def split(to_chunk, num_chunks):
    """ split a list into evenly sized chunks

    Args:
        to_chunk: The original list to turn in to chunks
        num_chunks: The total number of chunks to create

    Returns: A new list with the

    """
    chunk_max_size = calculate_size(to_chunk, num_chunks)
    chunked_list = [
        to_chunk[i : i + chunk_max_size]
        for i in range(0, len(to_chunk), chunk_max_size)
    ]

    return chunked_list
