#!/usr/bin/env python3

import sys
import struct
import argparse

__author__ = "Marcel Hecko"
__email__ = "maco@blava.net"


def sht2x_temp(raw):
    return -46.85 + 175.72 * raw / 65536


def sht3x_temp(raw):
    return -45 + 175 * float(raw) / (2**16 - 1)


def sht2x_rh(raw):
    return -6 + 125 * raw / 65536


def sht3x_rh(raw):
    return 100 * float(raw) / (2**16 - 1)


def show_data(temp_in, rh_in):
    for unp in ['>H', '<H']:
        t_raw = struct.unpack(unp, bytes.fromhex(temp_in))[0]
        rh_raw = struct.unpack(unp, bytes.fromhex(rh_in))[0]
        if args.sht2x:
            print("Calculating for SHT2x")
            t = sht2x_temp(t_raw)
            rh = sht2x_rh(rh_raw)
        elif args.sht3x:
            print("Calculating for SHT3x")
            t = sht3x_temp(t_raw)
            rh = sht3x_rh(rh_raw)
        else:
            sys.exit("Problem")
        print("{} {}  Temperature: {:.2f}".format(unp, temp_in, t))
        print("{} {} Rel humidity: {:.2f}".format(unp, rh_in, rh))
        print('--------------')


def main():
    show_data(args.temp, args.rh)
    print("Switching temp input data for rh and vice versa")
    show_data(args.rh, args.temp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-2', '--sht2x', action='store_true', help="SHT2x")
    parser.add_argument('-3', '--sht3x', action='store_true', help="SHT3x")
    parser.add_argument('-t', '--temp', action='store', help="Temp HEX")
    parser.add_argument('-r', '--rh', action='store', help="RH HEX")
    args = parser.parse_args()

    main()
