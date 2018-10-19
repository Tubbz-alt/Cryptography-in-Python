import struct

from bitarray import bitarray

def rotate_left(val, r_bits, max_bits=16):
    '''
    cicular shift to left for r_bits
    from https://www.falatic.com/index.php/108/python-and-bitwise-rotation
    '''
    return (val << r_bits % max_bits) & (2 ** max_bits - 1) | \
    ((val & (2 ** max_bits - 1)) >> (max_bits -(r_bits % max_bits)))
 
def rotate_right(val, r_bits, max_bits=16):
    '''
    cicular shift to right for r_bits
    from https://www.falatic.com/index.php/108/python-and-bitwise-rotation
    '''
    return ((val & (2 ** max_bits - 1)) >> r_bits % max_bits) | \
    (val << (max_bits -(r_bits % max_bits)) & (2 ** max_bits - 1))

def string_to_bitarray(string:str) -> bitarray:
    '''
    convert string to bit arrays
    '''
    string_in_bytes = string.encode("utf-8")
    bit_array       = bitarray()

    return bit_array.frombytes(string_in_bytes)

def expand_bitarray_to_n_bits(bit_array:bitarray, new_size:int) -> bitarray:
    '''
    expand the bitarray to n bits
    '''
    if len(bit_array) > new_size:
        raise ValueError("the new size is smaller than the bit array")

    elif len(bit_array) == new_size:
        return bit_array

    else:
        bits = [False for i in range(new_size - len(bit_array))]
        bit_array.extend(bits)
        return bit_array    

def split_data_to_every_n_bits(bit_array:bitarray, slice_size:int):
    '''
    split the data into slices with each slice = [slice size]
    '''
    slice_num     = (len(bit_array) // slice_size)
    slice_num     = slice_num + 1 if len(bit_array) % slice_size else slice_num

    bit_array_cpy = bit_array.copy()
    bit_array_cpy = expand_bitarray_to_n_bits(bit_array_cpy, slice_num * slice_size)

    current_ptr = 0
    while current_ptr < len(bit_array_cpy):
        yield bit_array_cpy[current_ptr:current_ptr + slice_size]
        current_ptr += slice_size
