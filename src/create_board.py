#!/usr/bin/env python3

import math
from enum import Enum

import click
import cv2
from cv2 import aruco

from src import logger, logger_timing

OUTPUT_DIR = "./outputs"

INCHES_TO_MM = 25.4
DEFAULT_DPI = 300


class PaperSize(Enum):
    A3 = (420, 297)
    A4 = (297, 210)
    A5 = (210, 148)


def get_size(width, height, dpi=DEFAULT_DPI):
    return (
        math.ceil(width * dpi / INCHES_TO_MM),
        math.ceil(height * dpi / INCHES_TO_MM),
    )


@click.command()
@click.option("--dpi", default=DEFAULT_DPI, help="DPI of the Output")
@click.option(
    "--paper",
    default="A3",
    type=click.Choice([e.name for e in PaperSize]),
    help="Paper size of the Output",
)
@logger_timing()
def main(dpi, paper):
    width, height = get_size(*PaperSize[paper].value, dpi=dpi)
    logger.debug(f"Creating board with size {width} x {height} [mm]")

    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
    board = aruco.CharucoBoard_create(7, 5, 1, 0.8, aruco_dict)
    cv2.imwrite(f"{OUTPUT_DIR}/board.png", board.draw((width, height)))
    logger.info("Done!")


if __name__ == "__main__":
    main()
