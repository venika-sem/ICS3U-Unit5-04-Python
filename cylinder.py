#!/usr/bin/env python3

# Created by : Venika Sem
# Created on : Dec 2022
# This program finds cylinder volume


import math


def volume_cylinder(radius: int, height: int) -> float:
    # Calculates a cylinder's volume

    if radius < 0 or height < 0:
        return -1
    else:
        volume = math.pi * radius**2 * height
        return volume


def main():
    # Gets input and calculate  volume of the cylinder
    try:
        radius_as_int = input("Enter radius of a cylinder (cm): ")
        radius_integer = float(radius_as_int)
        height_as_int = input("Enter height of a cylinder (cm): ")
        height_integer = float(height_as_int)
        cylinder_volume = volume_cylinder(radius_integer, height_integer)
        print("\nThis cylinder's volume is {} cm³".format(cylinder_volume))
    except ValueError:
        print("\nInvalid Input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
